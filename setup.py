import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '3.0.7'

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
          "Development Status :: 5 - Production/Stable",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: 5.0",
          "Framework :: Plone :: 5.1",
          "Framework :: Plone :: 5.2",
          "Framework :: Plone :: Core",
          "Framework :: Zope2",
          "Framework :: Zope :: 4",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
      ],
      keywords='plone theme manage',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='https://pypi.org/project/plone.theme',
      license='GPL version 2',
      packages=find_packages(),
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
