#
# @File: imagesaver.py
#
# Author: Konstantin Prusakov <konstantin.prusakov@phystech.edu>
#

from PySide2.QtWidgets import QFileDialog
from PySide2.QtCore import QObject, Signal

from .image import Image


class BaseSaver(QObject):

    filters = [
        "Images (*.png *.jpg *.bmp *.jpeg)",
        "Raw images(*.csv)",
        "All files (*.*)"
    ]

    def __init__(self, parent=None):
        super(BaseSaver, self).__init__(parent)
        self._filter = str()

    def update_filters(self, filters=None):
        if filters is None:
            self._filter = ";;".join(self.filters)
        else:
            self._filter = ";;".join(filters)

    def show_save_dialog(self):
        filename, _ = QFileDialog.getSaveFileName(
            self.parent(),
            "Save Image",
            filter=self._filter)
        self._save(filename)

    def _save(self, filename):
        raise NotImplementedError()


class ImageSaver(BaseSaver):

    def __init__(self, image, color_table=None, parent=None):
        super(ImageSaver, self).__init__(parent)
        self._image = Image(image, colormap=color_table)
        if self._image.matrix is not None:
            self.update_filters()
        else:
            self.update_filters([self.filters[0], self.filters[-1]])

    def _save(self, filename):
        self._image.save_image_with_full_name(filename)


class ImageSaverSignal(BaseSaver):

    signal_save_image = Signal(str)

    def __init__(self, is_matrix=True, parent=None):
        super(ImageSaverSignal, self).__init__(parent)
        if is_matrix:
            self.update_filters()
        else:
            self.update_filters([self.filters[0], self.filters[-1]])

    def _save(self, filename):
        self.signal_save_image.emit(filename)
