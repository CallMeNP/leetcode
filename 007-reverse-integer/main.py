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
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        is_negative = x < 0
        if is_negative:
            x = -x

        k = x
        j = 0
        while k > 0:
            if j > INT_MAX / 10 or INT_MAX - j * 10 < k % 10:
                return 0
            if j < INT_MIN / 10 or j * 10 - INT_MIN < k % 10:
                return 0
            j *= 10
            if is_negative:
                j -= k % 10
            else:
                j += k % 10
            k = int(k / 10)

        print(j)
        return j


if __name__ == "__main__":
    s = Solution()
    data = [
        [1, 1],
        [123, 321],
        [-123, -321],
        [-2147483648, 0],
        [-1534236469, 0]
    ]
    for i in data:
        print(s.reverse(i[0]) == i[1])
