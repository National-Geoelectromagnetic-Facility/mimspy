"""A module to create a graph widget."""

from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMainWindow, QWidget


class GraphWidget(QMainWindow):
    """A class to create a graph widget."""

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent=parent)
        self.n_h = 0  # x value increments
        self.n_e = 0  # x value increments
        self.chart = QChart()
        self.chart.legend().hide()
        self.view = QChartView(self.chart)
        self.view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setCentralWidget(self.view)
        self.chart.layout().setContentsMargins(0, 0, 0, 0)
        self.axis_y_electrode: QValueAxis = QValueAxis()
        self.series_electrode: QLineSeries = QLineSeries()
        self.series_mag: QLineSeries = QLineSeries()
        self.y_axis_h: QValueAxis = QValueAxis()

    def set_title(self, title: str) -> None:
        """Set the title of the chart."""
        self.chart.setTitle(title)

    def add_data_e(
        self,
        xdata: list[int],
        ydata: list[float],
        ticks: int = 20,
        color: Qt.GlobalColor = Qt.GlobalColor.blue,
        align: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignRight,
    ) -> None:
        """Add data to the chart."""
        # define the x-axis
        axis_x = QValueAxis()
        axis_x.setTickCount(ticks)
        self.chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)

        # define the y-axis
        self.axis_y_electrode = QValueAxis()
        self.axis_y_electrode.setLinePenColor(color)
        self.chart.addAxis(self.axis_y_electrode, align)
        # set the range of the Y axis
        self.y_axis_h.setMax(max(ydata) + 1)
        self.y_axis_h.setMin(min(ydata) - 1)

        # define the dataset
        # self.series_e = QLineSeries()
        # create the graph color
        pen = self.series_electrode.pen()
        # set the color of the graph
        pen.setColor(color)
        self.series_electrode.setPen(pen)
        # get the data series_e
        for x, y in zip(xdata, ydata, strict=False):
            self.n_e += 1
            self.series_electrode.append(x, y)
        # add the data to the chart
        self.chart.addSeries(self.series_electrode)

        # add the axis to the series
        self.series_electrode.attachAxis(self.axis_y_electrode)

    def add_data_h(
        self,
        xdata: list[int],
        ydata: list[float],
        ticks: int = 20,
        color: Qt.GlobalColor = Qt.GlobalColor.red,
        align: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignLeft,
    ) -> None:
        """Add data to the chart."""
        # define the x-axis
        x_axis = QValueAxis()
        x_axis.setTickCount(ticks)
        self.chart.addAxis(x_axis, Qt.AlignmentFlag.AlignBottom)

        # define the y-axis
        self.y_axis_h = QValueAxis()
        # if color is not None:
        self.y_axis_h.setLinePenColor(color)
        self.chart.addAxis(self.y_axis_h, align)
        # set the axis limits
        self.y_axis_h.setMax(max(ydata) + 1)
        self.y_axis_h.setMin(min(ydata) - 1)

        # define the dataset
        self.series_mag = QLineSeries()
        # create the graph color
        pen = self.series_mag.pen()
        # set the color of the graph
        pen.setColor(color)
        self.series_mag.setPen(pen)
        # get the data series
        for x, y in zip(xdata, ydata, strict=False):
            self.n_h += 1
            self.series_mag.append(x, y)
        # add the data to the chart
        self.chart.addSeries(self.series_mag)

        # add the axis to the series
        self.series_mag.attachAxis(self.y_axis_h)

    def add_point_e(self, ydata: list[float]) -> None:
        """Add a point to the chart."""
        # remove the series so that is can be updated
        self.chart.removeSeries(self.series_electrode)
        # remove the first value, far left
        self.series_electrode.remove(0)
        self.n_e += 1
        # add value to end, far right
        self.series_electrode.append(self.n_e, ydata[-1])
        self.chart.addSeries(self.series_electrode)

        # set the axis limits
        self.axis_y_electrode.setMax(max(ydata) + 1)
        self.axis_y_electrode.setMin(min(ydata) - 1)

    def add_point_h(self, ydata: list[float]) -> None:
        """Add a point to the chart."""
        # remove the series so that is can be updated
        self.chart.removeSeries(self.series_mag)
        # remove the first value, far left
        self.series_mag.remove(0)
        self.n_h += 1
        # add value to end, far right
        self.series_mag.append(self.n_h, ydata[-1])
        self.chart.addSeries(self.series_mag)

        # set the axis limits
        self.y_axis_h.setMax(max(ydata) + 1)
        self.y_axis_h.setMin(min(ydata) - 1)
