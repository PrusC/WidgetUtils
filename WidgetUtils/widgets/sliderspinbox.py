#
# @File: sliderspinbox.py
#
# Author: Konstantin Prusakov <konstatnin.prusakov@phystech.edu>
#

from PySide2.QtWidgets import QWidget, QHBoxLayout, QDoubleSpinBox, QLabel
from PySide2.QtCore import Signal, Slot, Qt
import sys

from .slider import Slider


class SliderSpinBox(QWidget):

    valueChanged = Signal(float)

    def __init__(self, parent=None, *args, **kwargs):
        super(SliderSpinBox, self).__init__(parent=parent, *args, **kwargs)

        self._outerLayout = QHBoxLayout(self)
        self._outerLayout.setSpacing(0)
        self._outerLayout.setMargin(0)

        self._slider = Slider(self)
        self._slider.setOrientation(Qt.Horizontal)
        self._spinBox = QDoubleSpinBox(self)
        self._labelMinValue = QLabel(self)
        self._labelMaxValue = QLabel(self)
        self._labelTitle = QLabel(self)

        self._outerLayout.addWidget(self._labelMinValue)
        self._outerLayout.addWidget(self._slider)
        self._outerLayout.addWidget(self._labelMaxValue)
        self._outerLayout.addWidget(self._spinBox)
        self._outerLayout.addWidget(self._labelTitle)

        self.setMinimum(self._slider.minimum())
        self.setMaximum(self._slider.maximum())
        self._spinBox.setSingleStep(self._slider.getRange()/10.0)
        self._connect()

    def _connect(self):
        self._slider.signalValueChanged.connect(self._on_slider_value_changed)
        self._spinBox.valueChanged.connect(self._on_spin_box_value_changed)
        self._spinBox.valueChanged.connect(self.valueChanged)

    @Slot(float)
    def _on_slider_value_changed(self, value):
        if abs(self._spinBox.value() - value) > sys.float_info.epsilon:
            self._spinBox.setValue(value)

    @Slot(float)
    def _on_spin_box_value_changed(self, value):
        if abs(self._slider.value() - value) > sys.float_info.epsilon:
            self._slider.setValue(value)

    def setValue(self, value):
        self._on_spin_box_value_changed(value)

    def setMinimum(self, value):
        self._slider.setMinimum(value)
        self._spinBox.setMinimum(value)
        self._labelMinValue.setText(str(value))
        self._spinBox.setSingleStep(self._slider.getRange()/10.0)

    def setMaximum(self, value):
        self._slider.setMaximum(value)
        self._spinBox.setMaximum(value)
        self._labelMaxValue.setText(str(value))
        self._spinBox.setSingleStep(self._slider.getRange()/10.0)

    def setRange(self, values):
        self.setMinimum(values[0])
        self.setMaximum(values[1])

    def setTitle(self, value):
        self._labelTitle.setText(value)

    def setSliderFactor(self, value):
        self._slider.setFactor(value)
