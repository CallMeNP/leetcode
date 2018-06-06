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
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ab_table = [("DCCCC", "CM"), ("LXXXX", "XC"), ("VIIII", "IX"), ("CCCC", "CD"), ("XXXX", "XL"), ("IIII", "IV")]
        for i in ab_table:
            s = s.replace(i[1], i[0])
        code_dict = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }
        num = 0
        for i in s:
            num += code_dict[i]
        return num


if __name__ == "__main__":

    s = Solution()
    data = [
        [3, "III"],
        [1994, "MCMXCIV"]
    ]

    for d in data:
        answer = s.romanToInt(d[1])
        if answer != d[0]:
            print(answer)
        else:
            print(True)
