# -*- coding: utf-8 -*-
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
import serial
from time import sleep
from portio.pyserial import list_ports
from PyQt5.QtCore import QThread, QRunnable, QMutex, pyqtSlot, pyqtSignal


class PortRead(QThread):
    serdata = pyqtSignal(bytes)

    def __init__(self, qport=None):
        QThread.__init__(self)
        self.qport = qport

        self.running = False

        # TODO: for testing
        # -------------------
        # self.path = '../test/NEL26a_data.nim'
        # self.path = '../test/NEW_GPS_data.BIN'
        # self.flepnt = open(self.path, 'rb')
        # -------------------

    def __del__(self):
        self.wait()

    def stop(self):
        # TODO: for testing
        # -------------------
        # self.flepnt.close()
        # -------------------
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            data = b''
            # TODO: for testing
            # -------------------
            # sleep(0.25)
            # for i in range(0, 25):
            #     data = self.flepnt.read(1)
            #     if data is not b'':
            #         self.serdata.emit(data)
            # -------------------

            # read port
            if self.qport.is_open:
                try:
                    data = self.qport.read()
                except serial.SerialException:
                    data = b''

            # emit the data
            if data is not b'':
                self.serdata.emit(data)


class PortMonitor(QThread):
    pyports = pyqtSignal(list)

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        while(1):
            sleep(3)
            ports = list_ports()
            self.pyports.emit(ports)


class PortWrite(QRunnable):

    def __init__(self, qport, _class, _id, _payload, mutex):
        super(PortWrite, self).__init__()
        # QThread.__init__(self)
        self.qmutex = mutex
        self.qport = qport
        self._class = _class
        self._id = _id
        self._payload = _payload
        self._sync = b'\xB5\x21'

    @pyqtSlot()
    def run(self):
        frame = self._compile_frame(self._class, self._id, self._payload)
        self.qmutex.lock()
        if self.qport.is_open:
            try:
                for i in range(0, len(frame), 512):
                    self.qport.write(frame[i:i + 512])
                    sleep(0.15)
            except serial.SerialException:
                pass
        self.qmutex.unlock()

    def _compile_frame(self, _class, _id, payload):
        """Compiler command frame with checksum.

        Args:
            _class (bytes): Cmd class identifier
            _id (bytes): Subclass identifier
            payload (bytes): Variable number of bytes to send

        Returns:
            bytes: Athena cmd frame
        """
        ck_a = 0
        ck_b = 0

        frame = _class + _id + self._get_length(len(payload)) + payload

        # Compute the checksum.
        for i in range(len(frame)):
            j = int.from_bytes(frame[i:i + 1], 'big')
            ck_a += j
            ck_b += ck_a

        return self._sync + frame + bytes([ck_a & 255]) + bytes([ck_b & 255])

    def _get_length(self, payload_length):
        _len = bytes([int(payload_length / 256), payload_length % 256])
        if len(_len) == 1:
            return b'\x00' + _len
        else:
            return _len
