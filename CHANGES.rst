Changelog
=========

3.0.2 (2017-02-05)
------------------

Bug fixes:

- Fixed test when using Zope 4.  [maurits]


3.0.1 (2016-11-17)
------------------

Fixes:

- Remove ZopeTestCase traces.
  [gforcada]

3.0.0 (2015-06-10)
------------------

- 3.x is plone 5 only
  [vangheem]


2.1.4 (2015-04-28)
------------------

- Remove dependency on CMFDefault
  [tomgross]


2.1.3 (2015-03-27)
------------------

- Test layer is testing layer.
  [bloodbare]


2.1.2 (2015-03-21)
------------------

- Move tests from PloneTestCase to plone.app.testing.
  [sdelcourt,timo]


2.1.1 (2014-03-02)
------------------

- Remove hard dependency on CMFDefault.
  [davisagli]

2.1 - 2011-05-12
----------------

- Update to import BeforeTraverseEvent from zope.traversing instead of
  zope.app.publication.
  [davisagli]

- Add MANIFEST.in.
  [WouterVH]


2.0 - 2010-07-18
----------------

- Update license to GPL version 2 only.
  [hannosch]


2.0b2 - 2010-03-05
------------------

- Protect against running multiple times. This can happen when using ++skin++
  traversers or VirtualHostMonster.
  [wichert]


2.0b1 - 2010-01-02
------------------

- Fix an error introduced by my previous adjustment. If a skin layer
  extending the default layer was used (which is typical), then the
  default layer would end up with higher precedence than browser
  layers not extending the default layer.
  [davisagli]


2.0a2 - 2009-11-13
------------------

- Inherit from the CMFDefault layer again, for compatibility with products
  that depend only on CMF but are also usable within Plone, and register
  views to the CMFDefault layer.
  [davisagli]


2.0a1 - 2009-04-05
------------------

- Avoid inheriting from the CMFDefault browser layer and rather define our
  own. We don't have anything in common with the CMFDefault layer.
  [hannosch]

- Declare test dependencies in an extra.
  [hannosch]

- Specify package dependencies.
  [hannosch]


1.1 - 2009-04-04
----------------

- Make sure the theme layer takes precedence over other browser layers.
  [davisagli]


1.0 - 2007-08-15
----------------

- First stable release
  [wichert]
