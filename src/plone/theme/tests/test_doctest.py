from plone.testing import layered
from plone.theme.testing import PLONETHEME_FUNCTIONAL_TESTING

import doctest
import unittest


def test_suite():
    return unittest.TestSuite(
        [
            layered(
                doctest.DocFileSuite(
                    "README.rst",
                    package="plone.theme",
                    optionflags=doctest.ELLIPSIS | doctest.REPORT_ONLY_FIRST_FAILURE,
                ),
                layer=PLONETHEME_FUNCTIONAL_TESTING,
            )
        ]
    )
