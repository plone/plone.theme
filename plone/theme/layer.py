# -*- coding: utf-8 -*-
import zope.deferredimport


zope.deferredimport.initialize()
zope.deferredimport.deprecated(
    "Import from Products.CMFPlone.theme instead",
    default_layers='Products.CMFPlone:theme.default_layers',
    mark_layer='Products.CMFPlone:theme.marklayer',
)
