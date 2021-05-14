#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_precise_sum(n):  # noqa: F811
    """
    Функция, возвращающая точна ли сумма n дробей вида 1 / n

    >>> 1 / 2 + 1 / 2
    1.0
    >>> is_precise_sum(2)
    True
    >>> 1 / 6 + 1 / 6 + 1 / 6 + 1 / 6 + 1 / 6 + 1 /6
    0.9999
    >>> is_precise_sum(6)
    False
    """
    return not_implemented



# =====================================================
# testing stuff
from funtests import CasesTestGen, not_implemented  # noqa: E402, F401
import unittest  # noqa: E402


class IsPreciseSumTest(CasesTestGen):
    def test_is_precise_sum(self):
        cases = (
            ((2,), True),
            ((3,), True),
            ((6,), False),
            ((7,), False),
        )
        self.execute_equal_subcases(is_precise_sum, cases)


DIFFICULTY = 2
TAGS = ['arithm']


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
