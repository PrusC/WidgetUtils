#
# @File: imagesaver.py
#
# Author: Konstantin Prusakov <konstatnin.prusakov@phystech.edu>
#

from PySide2.QtWidgets import QFileDialog
from PySide2.QtCore import QObject
from PySide2.QtGui import QImage

import numpy

# from .numpy2qimage import to_qimage
# from .colormap import grey
from .image import Image


class ImageSaver(QObject):

    def __init__(self, image, color_table=None, parent=None):
        super(ImageSaver, self).__init__(parent)
        self._image = Image(image, colormap=color_table)

    def show_save_dialog(self):
        if self._image.matrix:
            _filter = "Images (*.png *.jpg *.bmp *.jpeg);;Raw images(*.csv);;All files (*.*)"
        else:
            _filter = "Images (*.png *.jpg *.bmp *.jpeg);;All files (*.*)"
        filename, _ = QFileDialog.getSaveFileName(
            self.parent(),
            "Save Image",
            filter=_filter)
        self._save_image(filename)

    def _save_image(self, filename):
        self._image.save_image_with_full_name(filename)
