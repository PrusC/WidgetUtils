#
# @File: colormap.py
#
# Author: Konstantin Prusakov <konstatnin.prusakov@phystech.edu>
#

import numpy
from PySide2.QtGui import qRgb
from WidgetUtils.utils.colormaps.seismic_data import _seismic_data256
import WidgetUtils.utils.colormaps.cet_tables as tables
from inspect import getmembers


def _to_rgb(colormap):
    colormap = numpy.array(colormap)
    cm = []
    for color in colormap:
        cm.append(qRgb(color[0], color[1], color[2]))
    return cm


def _generate_colormap(minvalue, maxvalue, colormap=_seismic_data256):
    return _to_rgb(colormap[minvalue:maxvalue+1])


def _generate_colormap_interp(minvalue, maxvalue, color_map=_seismic_data256):
    points = numpy.array(color_map)
    interp = numpy.empty((maxvalue + 1 - minvalue, 3))
    x = numpy.linspace(minvalue, maxvalue, interp.shape[0])
    for c in range(points.shape[1]):
        interp[:, c] = numpy.interp(x, numpy.linspace(0, points.shape[0], points.shape[0]), points[:, c])
    return _to_rgb(interp)


grey = [qRgb(i, i, i) for i in range(256)]
seismic = _generate_colormap_interp(0, 255)


colormap_dict = {
    'None': None,
    'Grey': grey,
    'Seismic': seismic,
}


def _my_dir(oo):
    return [o for o in dir(oo) if not o.startswith('__')]


def _my_getmembers(oo):
    return [o for o in getmembers(oo) if not o[0].startswith('__')]


for name, table in _my_getmembers(tables):
    colormap_dict.update({name: _generate_colormap_interp(0, 255, table)})
