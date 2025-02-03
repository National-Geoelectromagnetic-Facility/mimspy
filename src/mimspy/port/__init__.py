"""Serial port utilities."""

from time import sleep

from PySide6.QtCore import QThread, Signal
from serial import Serial, SerialException

from .serial import SerialNode, list_ports


class PortRead(QThread):
    """Read data from a serial port."""

    SERIAL_DATA = Signal(bytes)

    def __init__(self, com_port: Serial | None = None):
        QThread.__init__(self)
        self.com_port = com_port

        self.running = False

    def stop(self):
        """Stop the thread."""
        self.running = False
        self.wait()

    def run(self):
        """Run the thread."""
        if self.com_port is None:
            return
        self.running = True
        while self.running:
            data = b""

            # read port
            if self.com_port.is_open:
                try:
                    data = self.com_port.read()
                except SerialException:
                    data = b""

            # emit the data
            if data != b"":
                self.SERIAL_DATA.emit(data)


class PortMonitor(QThread):
    """Monitor the serial ports."""

    pyports = Signal(list)

    def __init__(self):
        QThread.__init__(self)
        self.running = False

    def stop(self):
        """Stop the thread."""
        self.running = False
        self.wait()

    def run(self):
        """Run the thread."""
        self.running = True
        while self.running:
            sleep(1)
            ports = list_ports()
            self.pyports.emit(ports)


__all__ = ["PortMonitor", "PortRead", "SerialNode", "list_ports"]
