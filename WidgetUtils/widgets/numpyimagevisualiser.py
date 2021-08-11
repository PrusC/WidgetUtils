#
# @File: numpyimagevisualiser.py
#
# Author: Konstantin Prusakov <konstatnin.prusakov@phystech.edu>
#

from PySide2.QtWidgets import QGraphicsPixmapItem, QGraphicsScene, QGraphicsView
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt

from WidgetUtils.utils.image import Image


__all__ = ['ImageVisualiseScene', 'CustomGraphicsView']


class ImageVisualiseScene(QGraphicsScene):

    def __init__(self, parent=None, image=None):
        super(ImageVisualiseScene, self).__init__(parent)
        if image and isinstance(image, Image):
            self._image = image
        else:
            self._image = Image()
        self.pixmap_item = QGraphicsPixmapItem()
        self.addItem(self.pixmap_item)

    def update_image(self, im, scaled_size=None, ratio=0x1):
        self._image.set_image(im)
        if scaled_size:
            self.pixmap_item.setPixmap(QPixmap.fromImage(self._image.image.scaled(scaled_size, aspectMode=ratio)))
        else:
            self.pixmap_item.setPixmap(QPixmap.fromImage(self._image.image))

    def set_colormap(self, colormap):
        self._image.set_colormap(colormap)

    @property
    def image(self):
        return self._image


class CustomGraphicsView(QGraphicsView):
    
    def __init__(self, parent=None, scene=None, *args, **kwargs):
        super(CustomGraphicsView, self).__init__(parent, *args, **kwargs)
        self._scene = None
        if isinstance(scene, QGraphicsScene):
            self.setScene(scene)

    def update_image(self, im, colormap=None, scaled_size=None, ratio=0x1):
        if self._scene:
            self._scene.set_colormap(colormap)
            self._scene.update_image(im, scaled_size, ratio)
        
    def setScene(self, scene):
        if isinstance(scene, ImageVisualiseScene):
            self._scene = scene
            self._scene.setParent(self)
            super(CustomGraphicsView, self).setScene(self._scene)
        else:
            super(CustomGraphicsView, self).setScene(scene)

    def fit(self):
        if self.scene():
            rect = self.scene().itemsBoundingRect()
            self.resetTransform()
            self.fitInView(rect, Qt.KeepAspectRatio)
            self.centerOn(rect.center())
        
    def resizeEvent(self, event):
        self.fit()
        super(CustomGraphicsView, self).resizeEvent(event)    
