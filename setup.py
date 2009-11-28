from setuptools import setup, find_packages
import os

version = '1.2'

setup(name='plone.theme',
      version=version,
      description="Tools for managing themes in CMF and Plone sites",
      long_description=open(os.path.join('plone', 'theme', 'README.txt')).read() + "\n" + \
                       open(os.path.join('docs', 'HISTORY.txt')).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Zope2",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Martin Aspeli',
      author_email='optilude@gmx.net',
      url='http://svn.plone.org/svn/plone/plone.theme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
