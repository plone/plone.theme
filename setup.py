from setuptools import setup, find_packages

version = '2.0a2'

setup(name='plone.theme',
      version=version,
      description="Tools for managing themes in CMF and Plone sites",
      long_description=open("README.txt").read() + "\n" + \
                       open("CHANGES.txt").read(),
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Martin Aspeli',
      author_email='optilude@gmx.net',
      url='http://pypi.python.org/pypi/plone.theme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
        test=[
            'Products.PloneTestCase',
        ]
      ),
      install_requires=[
          'setuptools',
          'zope.component',
          'zope.interface',
          'zope.publisher',
          'zope.app.publication',
          'Products.CMFDefault',
          'Products.CMFCore',
          'Zope2',
      ],
      )
