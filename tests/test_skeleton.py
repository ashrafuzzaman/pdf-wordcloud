# -*- coding: utf-8 -*-

import pytest
from pdf_wordcloud.skeleton import fib

__author__ = "A.K.M. Ashrafuzzaman"
__copyright__ = "A.K.M. Ashrafuzzaman"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
