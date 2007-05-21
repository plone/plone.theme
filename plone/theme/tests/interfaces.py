# A browser layer - you should make one of these for your own skin
# and register it with a name corresponding to a skin in portal_skins.
# See tests.zcml and README.txt for more.

from zope.publisher.interfaces.browser import IDefaultBrowserLayer

class IMyTheme(IDefaultBrowserLayer):
    """Marker interface used in the tests
    """