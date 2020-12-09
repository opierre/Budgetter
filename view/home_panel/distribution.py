from PySide2.QtCore import QObject, Qt
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter, QBrush, QColor, QCursor, QFont
from PySide2.QtWidgets import QGridLayout, QSizePolicy

from random import randrange
from functools import partial


class Distribution(QObject):
    """
    Distribution
    """

    def __init__(self, gui):
        super(Distribution, self).__init__()

        """ Store gui """
        self.uiSetup = gui

        """ Create ChartView and Chart """
        self.chartView = QtCharts.QChartView()
        self.chart = self.chartView.chart()

        """ Setup distribution QChart """
        self.setupDistribution()

        """ Apply Layout on GroupBox """
        self.layout = QGridLayout(self.uiSetup.distribution)
        self.layout.addWidget(self.chartView, 0, 0)
        self.uiSetup.distribution.setLayout(self.layout)

        """ Connect Distribution groupBox """
        self.connectDistribution()

    def connectDistribution(self):
        """
        Connect Accounts widgets
        :return: void
        """

        """ Connect click on groupBox to set always checked """
        # self.uiSetup.distribution.clicked.connect(self.checkGroupBox)

    def setupDistribution(self):
        """
        Setup distribution with QtChart
        :return: void
        """

        """ Set ChartView properties """
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chartView.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        """ Set Chart properties """
        self.chart.legend().setVisible(False)
        self.chart.setBackgroundBrush(QBrush(QColor("transparent")))
        self.chart.setAnimationOptions(QtCharts.QChart.GridAxisAnimations)

        self.setup_donuts()

    def setup_donuts(self):
        self.donut = []
        donut = QtCharts.QPieSeries()
        slicecount = randrange(3, 6)
        for j in range(slicecount):
            value = randrange(100, 200)

            slice = QtCharts.QPieSlice(str(value) + ' €', value)
            slice.setLabelVisible(True)
            slice.setBorderColor(QColor(37, 55, 70))
            slice.setLabelColor(Qt.white)
            slice.setLabelFont(QFont("Roboto Light", 10, QFont.Normal))
            slice.setLabelPosition(QtCharts.QPieSlice.LabelInsideTangential)
            # slc.label().setCursor(QCursor(Qt.PointingHandCursor))

            slice.hovered.connect(partial(self.explodeSlice, slc=slice))
            slice.clicked.connect(partial(self.centerSlice, slice))

            donut.append(slice)
            size = (1.5 - 0.1)/5
            donut.setHoleSize(0.1 + 1 * size)
            donut.setPieSize(0.1 + (1 + 1) * size)

        self.donut.append(donut)
        self.chartView.chart().addSeries(donut)

    def explodeSlice(self, exploded, slc):
        slc.setExploded(exploded)

    def centerSlice(self, slice):
        """
        Center slice on click
        :param slice: slice slicked
        :return: void
        """

        """ Get phase shift for clicked slice """
        phaseShift = slice.startAngle() + slice.angleSpan() / 2

        """ Rotate each slice """
        for donut in self.donut:
            donut.setPieStartAngle(donut.pieStartAngle() - phaseShift)
            donut.setPieEndAngle(donut.pieEndAngle() - phaseShift)

    def checkGroupBox(self):
        """
        Set checkbox always enabled
        :return: void
        """

        self.uiSetup.accounts.setChecked(True)
