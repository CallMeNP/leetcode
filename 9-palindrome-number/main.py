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
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x > 0 and x % 10 == 0:
            return False
        k = x
        j = 0
        while k > 0:
            j *= 10
            j += k % 10
            k = int(k / 10)
        print(x, j)
        return x == j


if __name__ == "__main__":
    s = Solution()
    data = [
        [0, True],
        [1, True],
        [123, False],
        [-12321, False],
        [121, True],
        [1221, True],
        [1221000, False]
    ]
    for i in data:
        print(s.isPalindrome(i[0]) == i[1])
