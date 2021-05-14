#!/usr/bin/evn python3
# -*- coding: utf-8 -*-


def word_count(string):
    """
    Количество слов

    Для заданного текста вернуть словарь, содержащий ключами слова из строки,
    а значениями: количество раз, сколько эта строка встретилась в строке

    Пример:
    >>> wd = word_count('''Beautiful is better than ugly.
    ... Explicit is better than implicit.
    ... Simple is better than complex.
    ... Complex is better than complicated.''')
    >>> import pprint
    >>> pprint.pprint(wd, indent=4)
    {   'beautiful': 1,
        'better': 4,
        'complex': 2,
        'complicated': 1,
        'explicit': 1,
        'implicit': 1,
        'is': 4,
        'simple': 1,
        'than': 4,
        'ugly': 1}
    """
    from collections import Counter
    

    new_replace=string.replace("."," ")
    new_register=new_replace.lower()
    new_string=new_register.split()


    update_string=Counter(new_string).most_common()
    new_dict=dict(update_string)

    return new_dict


# =====================================================
# testing stuff
from funtests import CasesTestGen, not_implemented  # noqa: E402, F401
import unittest  # noqa: E402


class WordCountTest(CasesTestGen):
    def test_word_count(self):
        cases = (
            ((
                """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.""",),
             {'beautiful': 1,
              'better': 4,
              'complex': 2,
              'complicated': 1,
              'explicit': 1,
              'implicit': 1,
              'is': 4,
              'simple': 1,
              'than': 4,
              'ugly': 1}),)
        self.execute_equal_subcases(word_count, cases)


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
