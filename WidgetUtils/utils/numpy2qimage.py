#
# @File: numpy2qimage.py
#
# Author: Konstantin Prusakov <konstatnin.prusakov@phystech.edu>
#

import numpy
import cv2
from PySide2.QtGui import QImage

from .colormaps.colormap import grey


def to_gray(img):
    if len(img.shape) == 2:
        return img
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


def to_qimage(im, color_table=grey, copy=True):
    if color_table is not None:
        im = to_gray(im)

    if len(im.shape) == 3:
        if im.shape[2] == 3:
            qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_RGB888)
        elif im.shape[2] == 4:
            qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_ARGB32)
        elif im.shape[2] == 1:
            qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_Indexed8)
            qim.setColorTable(color_table)

    elif len(im.shape) == 2:
        if im.dtype == numpy.uint8:
            qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_Indexed8)
            if color_table:
                qim.setColorTable(color_table)
        elif im.dtype == numpy.uint16:
            im = (im/16)
            im = numpy.require(im, dtype=numpy.uint8, requirements='C')
            qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_Indexed8)
            if color_table:
                qim.setColorTable(color_table)
        else:
            raise TypeError("Unsupported data type")

    else:
        raise TypeError("Wrong image shape {}".format(im.shape))

    return qim.copy() if copy else qim
