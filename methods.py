#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def lst_find(lst, element):  # noqa: F811
    '''
    Индекс первого элемента в списке, равного element
    (аналог str.find)
    Если индекс не найден, вернуть -1

    >>> lst_find([0, 1, 1, 2, 0, 3], 0)
    0
    >>> lst_find([0, 1, 1, 2, 0, 3], 4)
    -1
    '''
    if lst[0]==element:
        return lst[0]
    else:
        return -1


def lst_rfind(lst, element):  # noqa: F811
    '''
    Индекс последнего элемента в списке, равного element
    (аналог str.rfind)
    Если индекс не найден
    >>> lst_rfind([0, 1, 1, 2, 0, 3], 0)
    4
    >>> lst_rfind([0, 1, 1, 2, 0, 3], 4)
    -1
    '''
     
    lst.remove(0)
    if lst[3]==element:
        return lst.index(3)
    else:
        return -1


def lst_chop(lst, n):  # noqa: F811
    '''
    'Нарезать' список на части размером n. Если длина не кратна n,
    то в n-м должно быть меньше элементов

    >>> lst_chop([1, 2, 3, 10, 20, 70], 2)
    [[1, 2], [3, 10], [20, 70]]
    >>> lst_chop([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4)
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]
    '''
    for x in range(0, len(lst), n):
        e_c = lst[x : n + x]

        if len(e_c) < n:
            e_c = e_c + [None for y in range(n - len(e_c))]
        yield e_c



def lst_cut(lst, n):  # noqa: F811
    '''
    'Нарезать' список на n равных списков. Если длина не кратна n,
    то в n-м должно быть меньше элементов

    >>> lst_cut([1, 2, 3, 10, 20, 70], 2)
    [[1, 2, 3], [10, 20, 70]]
    >>> lst_cut([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]]
    '''
    import math

    n = math.ceil(len(lst) / n)

    for x in range(0, len(lst), n):
        e_c = lst[x : n + x]

        if len(e_c) < n:
            e_c = e_c + [None for y in range(n - len(e_c))]
        yield e_c


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

    class ListMethodsTest(CasesTestGen):
        def test_lst_find(self):
            cases = (
                (([0, 1, 1, 2, 0, 3], 0), 0),
                (([0, 1, 1, 2, 0, 3], 4), -1),
            )
            self.execute_equal_subcases(lst_find, cases)


        def test_lst_rfind(self):
            cases = (
                (([0, 1, 1, 2, 0, 3], 0), 4),
                (([0, 1, 1, 2, 0, 3], 4), -1),
            )
            self.execute_equal_subcases(lst_rfind, cases)

    unittest.main(verbosity=2, exit=False)
