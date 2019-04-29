#!/opt/local/bin/python3.6

# ************************************************************************
#  File Name: pyserial.py
#
#  Created By: Brady Fry (frybr)
#
#  Purpose:
# ************************************************************************
#
# Serial port enumeration. Console tool and backend selection.
#
# This file is part of pySerial. https://github.com/pyserial/pyserial
# (C) 2011-2015 Chris Liechti <cliechti@gmx.net>
#
# SPDX-License-Identifier:    BSD-3-Clause
"""\
This module will provide a function called comports that returns an
iterable (generator or list) that will enumerate available com ports. Note that
on some systems non-existent ports may be listed.

Additionally a grep function is supplied that can be used to search for ports
based on their descriptions or hardware ID.
"""

# ***********************************************************************/
# imports
# ***********************************************************************/
from time import sleep
from collections import namedtuple

# ***********************************************************************/
# global variables
# ***********************************************************************/


class Cmd:

    def __init__(self, port):
        self.null = b'\x00'
        self.port = port
        self.parse = Parsecmd()

        Cmd = namedtuple("Cmd", ["clss", "id", "payload"])
        # NIMS command(s)
        Nimid = namedtuple("Nimid", ["gain", "shortcycle", "packet"])
        Nimpl = namedtuple("Nimpl", ["null", "xlyl", "xhyl", "xlyh", "xhyh"])
        nimid = Nimid(gain=b'\x01', shortcycle=b'\x02', packet=b'\x03')
        nimpl = Nimpl(null=b'\x00', xlyl=b'\x00', xhyl=b'\x01',
                      xlyh=b'\x02', xhyh=b'\x03')
        self.nim = Cmd(clss=b'\x01', id=nimid, payload=nimpl)
        # Battery command(s)
        Batid = namedtuple("Batid", ["voltage"])
        Batpl = namedtuple("Batpl", ["null"])
        batid = Batid(voltage=b'\x01')
        batpl = Batpl(null=b'\x00')
        self.bat = Cmd(clss=b'\x02', id=batid, payload=batpl)
        # Mag light command(s)
        Magid = namedtuple("Magid", ["light"])
        Magpl = namedtuple("Magpl", ["null", "off", "on"])
        magid = Magid(light=b'\x01')
        magpl = Magpl(null=b'\x00', off=b'\x00', on=b'\x01')
        self.mag = Cmd(clss=b'\x03', id=magid, payload=magpl)
        # uSD Card command(s)
        Usdid = namedtuple("Usdid", ["start", "stop", "list", "dfname",
                                     "download", "downpos", "append",
                                     "delete", "state"])
        Usdpl = namedtuple("Usdpl", ["null"])
        usdid = Usdid(start=b'\x01', stop=b'\x02', list=b'\x03',
                      dfname=b'\x04', download=b'\x05', downpos=b'\x06',
                      append=b'\x07', delete=b'\x08', state=b'\x09')
        usdpl = Usdpl(null=b'\x00')
        self.usd = Cmd(clss=b'\x04', id=usdid, payload=usdpl)

    def process(self, data):
        return self.parse.process(data)


class Parsecmd:

    def __init__(self):
        self._Cmd = namedtuple("Cmd", ["clss", "id"])
        self._cmd_esp = b'\x03'
        self._parse = self._check_sync
        self._temp = self._null
        self._cmd_len = 4
        self._sync_a = b'\xb5'
        self._sync_b = b'\x21'
        self._clear()

    def _clear(self):
        self._i = 0
        self._cmd = bytearray(self._cmd_len)
        self._checksum = bytearray(2)

    def _payload_init(self):
        self._payload_len = int.from_bytes(self._cmd[2:], 'big')
        self._payload = bytearray(self._payload_len)

    def _null(self, byte):
        pass

    def process(self, byte):
        null = (None, None)

        if self._parse is not self._checksum_receive_b:
            if byte == self._sync_a:
                self._temp = self._parse
                self._parse = self._check_sync
                return null

        cmd = self._parse(byte)

        if cmd is None:
            return null

        return cmd

    def _check_sync(self, byte):
        try:
            if byte == self._sync_b:
                self._clear()
                self._parse = self._cmd_receive
            else:
                self._parse = self._temp
                self._parse(self._sync_a)
                return self._parse(byte)
        except RecursionError:
            self._clear()
            self._parse = self._null

    def _cmd_receive(self, byte):
        self._cmd[self._i:self._i + 1] = byte
        self._i += 1

        if self._i == self._cmd_len:
            self._i = 0
            self._payload_init()
            self._parse = self._payload_receive

    def _payload_receive(self, byte):
        self._payload[self._i:self._i + 1] = byte
        self._i += 1

        if self._i == self._payload_len:
            self._i = 0
            self._parse = self._checksum_receive_a

    def _checksum_receive_a(self, byte):
        self._checksum[0:1] = byte

        self._parse = self._checksum_receive_b

    def _checksum_receive_b(self, byte):
        cmd = None
        self._checksum[1:] = byte

        # Verify the cmd via checksome
        if self._checksum_compute():
            cmd = (self._Cmd(clss=bytes(self._cmd[:1]),
                             id=bytes(self._cmd[1:2])),
                   bytes(self._payload))
        else:
            cmd = (None, None)

        self._parse = self._null

        return cmd

    def _checksum_compute(self):
        """Compute the 2 byte checksum of the cmd frame.

        Returns:
            Bool: 16-bit checksum comparison
        """
        ck_a = 0
        ck_b = 0
        check = False

        # Compute first part of the checksum.
        for i in range(len(self._cmd)):
            j = int.from_bytes(self._cmd[i:i + 1], 'big')
            ck_a += j
            ck_b += ck_a

        # Compute second part of the checksum.
        for i in range(len(self._payload)):
            j = int.from_bytes(self._payload[i:i + 1], 'big')
            ck_a += j
            ck_b += ck_a

        # self.uart.write('{}\n'.format(bytearray([ck_a, ck_b])))
        # Compare the checksum.
        if self._checksum == bytearray([ck_a & 255, ck_b & 255]):
            check = True

        return check
