from PySide2.QtWidgets import QSlider
from PySide2.QtCore import Signal as pyqtSignal
from PySide2.QtCore import Slot as pyqtSlot


class FloatSlider(QSlider):

    floatValueChanged = pyqtSignal(float)

    def __init__(self, *args, **kwargs):
        QSlider.__init__(self, *args, **kwargs)
        self._max_int_value = 10**4
        QSlider.setMinimum(self, 0)
        QSlider.setMaximum(self, self._max_int_value)
        self._max_value = 1.0
        self._min_value = 0.0
        self.valueChanged.connect(self._emitFloatValueChanged)

    @pyqtSlot()
    def _emitFloatValueChanged(self):
        self.floatValueChanged.emit(self.value())

    @property
    def _range(self):
        return self._max_value - self._min_value

    def value(self):
        return float(QSlider.value(self)) / self._max_int_value * self._range + self._min_value

    def setValue(self, value):
        float_value = (value - self._min_value) / self._range * self._max_int_value
        QSlider.setValue(self, int(float_value))

    def setMinimum(self, value):
        self._min_value = value
        self.setValue(self.value())

    def setMaximum(self, value):
        self._max_value = value
        self.setValue(self.value())

    def minimum(self):
        return self._min_value

    def maximum(self):
        return self._max_value

    def setFactor(self, value):
        self._max_int_value = value
        self.setValue(self.value())

    def getRange(self):
        return self._range
