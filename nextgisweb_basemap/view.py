# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, print_function, unicode_literals

from nextgisweb.resource import Widget
from nextgisweb.webmap import WebMap
from .model import BasemapLayer


class BasemapLayerWidget(Widget):
    resource = BasemapLayer
    operation = ('create', 'update')
    amdmod = 'ngw-basemap/LayerWidget'


class BasemapWebMapWidget(Widget):
    resource = WebMap
    operation = ('create', 'update')
    amdmod = 'ngw-basemap/WebMapWidget'
