# -*- coding: utf-8 -*-
import zope.deferredimport


zope.deferredimport.initialize()
zope.deferredimport.deprecated(
    "Import from Products.CMFPlone.interfaces.theme instead",
    IDefaultPloneLayer='Products.CMFPlone.interfaces:theme.IDefaultPloneLayer',
)
