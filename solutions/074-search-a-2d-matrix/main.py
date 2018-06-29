#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
tags: 二分查找, 坐标转换
"""


class Solution:
    """
    >>> s=Solution()
    >>> s.searchMatrix([ [1,   3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50] ],3)
    True
    >>> s.searchMatrix([ [1,   3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50] ],13)
    False
    """

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        max_x = len(matrix[0])
        max_y = len(matrix)

        def get_val(n):
            y = n // max_x
            x = n % max_x
            return matrix[y][x]

        left = 0
        right = max_x * max_y
        while left < right:
            mid = (left + right) >> 1
            k = get_val(mid)
            if k == target:
                return True
            if k < target:
                left = mid + 1
            if k > target:
                right = mid
        return False


if __name__ == '__main__':
    import doctest

    doctest.testmod()
