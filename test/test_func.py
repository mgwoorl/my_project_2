import pytest
from code.func import Vector

class TestVector:
    def test_length(self):
        v = Vector(3, 7)
        out = 7.615773105863909
        res = v.length()
        assert res == out
