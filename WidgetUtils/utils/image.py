#
# @File: image.py
#
# Author: Konstantin Prusakov <konstatnin.prusakov@phystech.edu>
#

import numpy
from PySide2.QtGui import QImage

from .numpy2qimage import to_qimage

__all__ = ['Image']


class Image(object):

    def __init__(self, im=None, colormap=None):
        self.im = None
        self.qim = None
        self.colormap = None
        if colormap:
            self.set_colormap(colormap)
        if im:
            self.set_image(im)

    def set_image(self, im):
        if isinstance(im, numpy.ndarray):
            self.im = im
            self.qim = to_qimage(self.im, self.colormap)
        elif isinstance(im, QImage):
            self.qim = im

    def set_colormap(self, colormap):
        self.colormap = colormap

    @property
    def image(self):
        return self.qim

    @property
    def matrix(self):
        return self.im

    def save_image(self, path, name):
        full_name = path + '\\' + name
        self.save_image_with_full_name(full_name)

    def save_image_with_full_name(self, full_name):
        if full_name.endswith('.csv'):
            if self.im and isinstance(self.im, numpy.ndarray):
                numpy.savetxt(full_name, self.im, fmt="%i", delimiter=";")
        else:
            if self.qim and isinstance(self.qim, QImage):
                self.qim.save(full_name)
