from PySide2.QtWidgets import QWidget, QHBoxLayout, QDoubleSpinBox, QLabel
from PySide2.QtCore import Qt
from PySide2.QtCore import Signal as pyqtSignal

from FloatSlider import FloatSlider


class SliderSpinBoxWidget(QWidget):

    valueChanged = pyqtSignal(float)

    def __init__(self, parent=None, *args, **kwargs):
        super(SliderSpinBoxWidget, self).__init__(parent=parent, *args, **kwargs)

        self._outerLayout = QHBoxLayout(self)

        self._slider = FloatSlider(self)
        self._slider.setOrientation(Qt.Horizontal)
        self._spinBox = QDoubleSpinBox(self)
        self._labelMinValue = QLabel(self)
        self._labelMaxValue = QLabel(self)
        self._labelTittle = QLabel(self)

        self._outerLayout.addWidget(self._labelMinValue)
        self._outerLayout.addWidget(self._slider)
        self._outerLayout.addWidget(self._labelMaxValue)
        self._outerLayout.addWidget(self._spinBox)
        self._outerLayout.addWidget(self._labelTittle)

        self.setMinimum(self._slider.minimum())
        self.setMaximum(self._slider.maximum())

        self._connect()

    def _connect(self):
        self._slider.floatValueChanged.connect(self._spinBox.setValue)
        self._slider.floatValueChanged.connect(self.valueChanged)
        self._spinBox.valueChanged.connect(self._slider.setValue)

    def setValue(self, value):
        self._slider.setValue(value)
        # self.valueChanged.emit(self._slider.value())

    def setMinimum(self, value):
        self._slider.setMinimum(value)
        self._spinBox.setMinimum(value)
        self._labelMinValue.setText(str(value))

    def setMaximum(self, value):
        self._slider.setMaximum(value)
        self._spinBox.setMaximum(value)
        self._labelMaxValue.setText(str(value))

    def setTittle(self, value):
        self._labelTittle.setText(value)

    def setSliderFactor(self, value):
        self._slider.setFactor(value)
