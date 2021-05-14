#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def almost_equal(f1, f2, epsilon=10**-10):  # noqa: F811
    '''
    Эффективное равнество чисел с плавающей точкой через
    константу неразличимости

    >>> almost_equal(1 / 49 * 49, 1.0)
    True

    Дополнительное чтение:
    https://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/
    https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html
    '''
    return not_implemented


# =====================================================
# testing stuff

FUN_DIFFICULTY = 2
FUN_TAGS = ['float']

if __name__ == '__main__':
    import os        # noqa: E402
    import sys       # noqa: E402
    import unittest  # noqa: E402

    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    from funtests import CasesTestGen, not_implemented  # noqa: E402, F401

    class AlmostEqualTest(CasesTestGen):
        def test_almost_equal(self):
            cases = (
                ((1 / 49 * 49, 1.0), True),
                ((sum(1/11 for _ in range(11)), 1.0), True),
                ((sum(1/81 for _ in range(81)), 1.0), True),
                ((-1.0, 0.0), False),
            )
            self.execute_equal_subcases(almost_equal, cases)

    unittest.main(verbosity=2, exit=False)
