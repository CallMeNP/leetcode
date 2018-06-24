#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""


def do_combine(start, end, k):
    if end - start + 1 < k or k < 1:
        pass
    elif k == 1:
        for i in range(start, end + 1):
            yield [i]
    else:
        for i in do_combine(start + 1, end, k - 1):
            yield [start] + i
        for i in do_combine(start + 1, end, k):
            yield i


class Solution:
    """
    >>> s=Solution()
    >>> s.combine(4,2)
    [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    >>> s.combine(4,0)
    []
    >>> s.combine(4,1)
    [[1], [2], [3], [4]]


    """

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        for i in do_combine(1, n, k):
            res.append(i)
        return res


if __name__ == '__main__':
    import doctest

    doctest.testmod()
