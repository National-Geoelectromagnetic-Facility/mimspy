"""Custom widgets for displaying vertical text in the GUI."""

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPainter, QPaintEvent
from PySide6.QtWidgets import QWidget


class VerticalTextLabel(QWidget):
    """A custom widget to display text vertically."""

    def __init__(self, text: str = "default"):
        QWidget.__init__(self)
        self.text = text
        self.rotate_mag = -90
        self.rotate_electrode = 90

    def paintEvent(self, event: QPaintEvent) -> None:
        """Paint the text on the widget."""
        my_font = QFont()
        my_font.setPointSize(16)
        my_font.setBold(True)
        painter = QPainter(self)
        if self.text.startswith("E"):
            painter.translate(5, self.height() - 100)
            painter.rotate(self.rotate_electrode)
            painter.setPen(Qt.GlobalColor.blue)
        else:
            painter.translate(15, self.height() - 50)
            painter.rotate(self.rotate_mag)
            painter.setPen(Qt.GlobalColor.red)
        painter.setFont(my_font)
        painter.drawText(0, 0, self.text)
        painter.end()
