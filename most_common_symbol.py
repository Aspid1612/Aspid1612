#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def most_common_symbol(string):
    """
    Функция, возвращающая самый часто встречающийся символ в заданной строке

    >>> most_common_symbol('Хладен, светел, День проснулся. Ранний петел Встрепенулся, Дружина, воспрянь!')
    'н'
    >>> most_common_symbol('Вставайте, о други! Бодрей, бодрей. На пир мечей. На брань!..')
    ' '
    >>> most_common_symbol('высокоуровневый язык программирования общего назначения с динамической строгой типизацией')
    'о'
    """
    from collections import Counter

    new_string=Counter(string).most_common(1)
    new_dict=dict(new_string)

    return max(new_dict,key=new_dict.get)


# =====================================================
# testing stuff
from funtests import CasesTestGen, not_implemented  # noqa: E402, F401
import unittest  # noqa: E402


class SymbolTest(CasesTestGen):
    def test_not_most_common_symbol(self):
        cases = (
            (('123.101.156.99',), '1'),
            (('Слов на «Й» совсем немного: Йогурт, йод, и слово йога. «Й» в конце обычно пишем: Чай, случайный, тайный, лишний.', ), ' '),
        )

        self.execute_equal_subcases(most_common_symbol, cases)


FUN_DIFFICULTY = 3
FUN_TAGS = ['string']


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
