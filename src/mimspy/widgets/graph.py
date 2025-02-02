"""A module to create a graph widget."""

from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMainWindow


class GraphWidget(QMainWindow):
    """A class to create a graph widget."""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.n_h = 0  # x value increments
        self.n_e = 0  # x value increments
        self.chart = QChart()
        self.chart.legend().hide()
        self.view = QChartView(self.chart)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(self.view)
        self.chart.layout().setContentsMargins(0, 0, 0, 0)
        self.axis_y_electrode: QValueAxis = QValueAxis()

    def set_title(self, title):
        """Set the title of the chart."""
        self.chart.setTitle(title)

    def add_data_e(
        self,
        xdata,
        ydata,
        ticks=20,
        color=Qt.GlobalColor.blue,
        align=Qt.AlignmentFlag.AlignRight,
    ):
        """Add data to the chart."""
        # define the x-axis
        axis_x = QValueAxis()
        axis_x.setTickCount(ticks)
        self.chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)

        # define the y-axis
        self.axis_y_electrode = QValueAxis()
        if color is not None:
            self.axis_y_electrode.setLinePenColor(color)
        self.chart.addAxis(self.axis_y_electrode, align)
        # set the range of the Y axis
        self.axisY_h.setMax(max(ydata) + 1)
        self.axisY_h.setMin(min(ydata) - 1)

        # define the dataset
        self.series_e = QLineSeries()
        # create the graph color
        pen = self.series_e.pen()
        # set the color of the graph
        if color is not None:
            pen.setColor(color)
        self.series_e.setPen(pen)
        # get the data series_e
        for x, y in zip(xdata, ydata, strict=False):
            self.n_e += 1
            self.series_e.append(x, y)
        # add the data to the chart
        self.chart.addSeries(self.series_e)

        # add the axis to the series
        self.series_e.attachAxis(self.axis_y_electrode)

    def add_data_h(
        self,
        xdata,
        ydata,
        ticks=20,
        color=Qt.GlobalColor.red,
        align=Qt.AlignmentFlag.AlignLeft,
    ):
        """Add data to the chart."""
        # define the x-axis
        axisX = QValueAxis()
        axisX.setTickCount(ticks)
        self.chart.addAxis(axisX, Qt.AlignmentFlag.AlignBottom)

        # define the y-axis
        self.axisY_h = QValueAxis()
        if color is not None:
            self.axisY_h.setLinePenColor(color)
        self.chart.addAxis(self.axisY_h, align)
        # set the axis limits
        self.axisY_h.setMax(max(ydata) + 1)
        self.axisY_h.setMin(min(ydata) - 1)

        # define the dataset
        self.series_h = QLineSeries()
        # create the graph color
        pen = self.series_h.pen()
        # set the color of the graph
        if color is not None:
            pen.setColor(color)
        self.series_h.setPen(pen)
        # get the data series
        for x, y in zip(xdata, ydata, strict=False):
            self.n_h += 1
            self.series_h.append(x, y)
        # add the data to the chart
        self.chart.addSeries(self.series_h)

        # add the axis to the series
        self.series_h.attachAxis(self.axisY_h)
        # series.attachAxis(axisX)

    def add_point_e(self, ydata):
        """Add a point to the chart."""
        # remove the series so that is can be updated
        self.chart.removeSeries(self.series_e)
        # remove the first value, far left
        self.series_e.remove(0)
        self.n_e += 1
        # add value to end, far right
        self.series_e.append(self.n_e, ydata[-1])
        self.chart.addSeries(self.series_e)

        # set the axis limits
        self.axis_y_electrode.setMax(max(ydata) + 1)
        self.axis_y_electrode.setMin(min(ydata) - 1)

    def add_point_h(self, ydata):
        """Add a point to the chart."""
        # remove the series so that is can be updated
        self.chart.removeSeries(self.series_h)
        # remove the first value, far left
        self.series_h.remove(0)
        self.n_h += 1
        # add value to end, far right
        self.series_h.append(self.n_h, ydata[-1])
        self.chart.addSeries(self.series_h)

        # set the axis limits
        self.axisY_h.setMax(max(ydata) + 1)
        self.axisY_h.setMin(min(ydata) - 1)
