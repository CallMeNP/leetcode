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
    def grayCode(self, n):
        """
        >>> s=Solution()
        >>> s.grayCode(2)
        [0, 1, 3, 2]
        >>> s.grayCode(1)
        [0, 1]
        >>> s.grayCode(0)
        [0]
        >>> s.grayCode(3)
        [0, 1, 3, 2, 6, 7, 5, 4]

        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(0, n):
            res += [(1 << i) + x for x in reversed(res)]
        return res


if __name__ == '__main__':
    import doctest

    doctest.testmod()
