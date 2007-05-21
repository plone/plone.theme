from zope.interface import alsoProvides
from zope.component import queryUtility

from zope.publisher.interfaces.browser import IBrowserSkinType
from zope.publisher.browser import applySkin

from Products.CMFCore.utils import getToolByName

def mark_layer(site, event):
    """Mark the request with a layer corresponding to the current skin,
    as set in the portal_skins tool.
    """
    portal_skins = getToolByName(site, 'portal_skins', None)
    if portal_skins is not None:
        skin_name = site.getCurrentSkinName()
        skin = queryUtility(IBrowserSkinType, name=skin_name)
        if skin is not None:
            applySkin(event.request, skin)