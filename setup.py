import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '3.0.2'

long_description = (
    read('README.rst')
    + '\n' +
    read('plone', 'theme', 'README.rst')
    + '\n' +
    read('CHANGES.rst')
    + '\n'
    )


setup(name='plone.theme',
      version=version,
      description="Tools for managing themes in CMF and Plone sites",
      long_description=long_description,
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: 5.0",
          "Framework :: Plone :: 5.1",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
      ],
      keywords='',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='https://pypi.python.org/pypi/plone.theme',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
          test=[
              'plone.app.testing',
          ]
      ),
      install_requires=[
          'setuptools',
          'zope.component',
          'zope.interface',
          'zope.publisher',
          'zope.traversing',
          'Products.CMFCore',
          'Zope2',
      ],
      )
