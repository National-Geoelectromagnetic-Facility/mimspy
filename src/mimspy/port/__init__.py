"""Serial port utilities."""

import contextlib
from pathlib import Path
from time import sleep

from loguru import logger as log
from PySide6.QtCore import QThread, Signal
from serial import Serial, SerialException

from .serial import SerialNode, list_ports


class PortRead(QThread):
    """Read data from a serial port."""

    SERIAL_DATA = Signal(bytes)

    def __init__(self, com_port: Serial | None = None, debug: bool = False):
        QThread.__init__(self)
        self.com_port = com_port

        self._running = False
        self._debug = debug
        self._fle_ptr = None

    def stop(self):
        """Stop the thread."""
        self._running = False
        if self._debug and self._fle_ptr is not None:
            self._fle_ptr.close()
            log.debug(f"File closed: {self._fle_ptr.closed}")
        self.wait()

    def run(self):
        """Run the thread."""
        self._running = True
        if self._debug:
            self._read_file()
        else:
            self._read_port()

    def _read_file(self):
        """Read data from a file."""
        fle_path = Path(Path(__file__).parent.parent.parent.parent, "data", "data.nim")
        log.debug(f"Using file: {fle_path}")
        with open(fle_path, "rb") as fle:
            while self._running:
                sleep(0.25)
                for _ in range(0, 25):
                    data = fle.read(1)
                    if data == b"":
                        self._running = False
                        break
                    self.SERIAL_DATA.emit(data)

    def _read_port(self):
        """Read data from the serial port."""
        if self.com_port is None:
            return
        while self._running:
            data = b""
            if self.com_port.is_open:
                with contextlib.suppress(SerialException):
                    data = self.com_port.read()
            if data != b"":
                self.SERIAL_DATA.emit(data)


class PortMonitor(QThread):
    """Monitor the serial ports."""

    pyports = Signal(list)

    def __init__(self):
        QThread.__init__(self)
        self._running = False

    def stop(self):
        """Stop the thread."""
        self._running = False
        self.wait()

    def run(self):
        """Run the thread."""
        self._running = True
        while self._running:
            sleep(1)
            ports = list_ports()
            self.pyports.emit(ports)


__all__ = ["PortMonitor", "PortRead", "SerialNode", "list_ports"]
