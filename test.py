from FloatSlider import FloatSlider
from sliderspinbox import SliderSpinBox
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide2.QtCore import Qt
import sys


application = QApplication(sys.argv)

w = QWidget()
w.show()
lay = QVBoxLayout(w)
slider = FloatSlider(w)
slider.setOrientation(Qt.Horizontal)
sliderSpin = SliderSpinBox(w)
lay.addWidget(slider)
slider.setValue(0.5)
slider.setMaximum(2.5)
lay.addWidget(sliderSpin)
sliderSpin.valueChanged.connect(slider.setValue)
sliderSpin.setTitle("Value")
sliderSpin.setMaximum(2.0)
sliderSpin.setValue(1.5)
sys.exit(application.exec_())
