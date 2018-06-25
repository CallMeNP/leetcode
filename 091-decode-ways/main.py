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
    def numDecodings(self, s):
        """
        >>> s=Solution()
        >>> s.numDecodings("0")
        0
        >>> s.numDecodings("12")
        2
        >>> s.numDecodings("226")
        3
        >>> s.numDecodings("2262")
        3
        >>> s.numDecodings("22621")
        6
        >>> s.numDecodings("226212")
        9
        >>> s.numDecodings("226012")
        0
        >>> s.numDecodings("0226")
        0
        >>> s.numDecodings("100226")
        0
        >>> s.numDecodings("101")
        1

        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":
            return 0
        illegal = ['00', '30', '40', '50', '60', '70', '80', '90']
        for i in illegal:
            if s.find(i) >= 0:
                return 0
        l = len(s)
        count = [1]
        for i in range(1, l):
            if int(s[i - 1:i + 1]) <= 26 and s[i - 1] != '0':
                if s[i] == '0':
                    count.append(count[i - 2])
                else:
                    count.append(count[i - 2] * 2 + count[i - 1] - count[i - 2])
            else:
                count.append(count[-1])
        return count[-1]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
