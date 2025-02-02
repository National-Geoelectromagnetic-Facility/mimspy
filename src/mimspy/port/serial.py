"""Serial port enumeration.

Console tool and backend selection.

This file is part of pySerial. https://github.com/pyserial/pyserial

This module will provide a function called comports that returns an
iterable (generator or list) that will enumerate available com ports. Note that
on some systems non-existent ports may be listed.

Additionally, a grep function is supplied that can be used to search for ports
based on their descriptions or hardware ID.
"""

import os

# chose an implementation, depending on os
if os.name == "nt":  # sys.platform == 'win32':
    from serial.tools.list_ports_windows import comports
elif os.name == "posix":
    from serial.tools.list_ports_posix import comports
else:
    raise ImportError("Sorry: no implementation for your platform ('{}') available".format(os.name))


class SerialNode:
    """Serial port information."""

    def __init__(self, port="", name="", desc="", hwid=""):
        self.port = port
        self.name = name
        self.desc = desc
        self.hwid = hwid

    def print_all(self):
        """Print all serial port information."""
        print("Serial Port: \t\t{}".format(self.port))
        print("Port Name: \t\t{}".format(self.name))
        print("Port Description: \t{}".format(self.desc))
        print("Port HW ID: \t\t{}".format(self.hwid))


def list_ports() -> list[SerialNode]:
    """List all available serial ports."""
    ports = []

    # get a list of sorted comports
    iterator = sorted(comports(include_links=False))

    for port, desc, hwid in iterator:
        node = SerialNode(port=port, desc=desc, hwid=hwid)
        # node.print_all()
        ports.append(node)

    return ports
