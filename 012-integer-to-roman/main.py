#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ""
        code_table = [
            (1000, "M"),
            (500, "D"),
            (100, "C"),
            (50, "L"),
            (10, "X"),
            (5, "V"),
            (1, "I"),
        ]
        for i in code_table:
            k = int(num / i[0])
            roman += i[1] * k
            num %= i[0]
        ab_table = [("DCCCC", "CM"), ("LXXXX", "XC"), ("VIIII", "IX"), ("CCCC", "CD"), ("XXXX", "XL"), ("IIII", "IV")]
        for i in ab_table:
            roman = roman.replace(*i)
        return roman


if __name__ == "__main__":

    s = Solution()
    data = [
        [3, "III"],
        [1994, "MCMXCIV"]
    ]

    for d in data:
        answer = s.intToRoman(d[0])
        if answer != d[1]:
            print(answer)
        else:
            print(True)
