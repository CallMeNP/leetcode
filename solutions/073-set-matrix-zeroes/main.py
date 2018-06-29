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
    """
    >>> s=Solution()
    >>> matrix=[ [1,1,1], [1,0,1], [1,1,1] ]
    >>> s.setZeroes(matrix)
    >>> matrix
    [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    >>> matrix=[ [0,1,2,0], [3,4,5,2], [1,3,1,5] ]
    >>> s.setZeroes(matrix)
    >>> matrix
    [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    """

    def setZeroes(self, matrix):
        """
        :type matrix: list[list[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return matrix
        max_y = len(matrix)
        max_x = len(matrix[0])
        x0 = 1
        for y in range(max_y):
            if matrix[y][0] == 0:
                x0 = 0
                break
        y0 = 1
        for x in range(max_x):
            if matrix[0][x] == 0:
                y0 = 0
                break
        for y in range(1, max_y):
            for x in range(1, max_x):
                if matrix[y][x] == 0:
                    matrix[y][0] = 0
                    matrix[0][x] = 0
        for y in range(1, max_y):
            for x in range(1, max_x):
                if matrix[y][0] == 0 or matrix[0][x] == 0:
                    matrix[y][x] = 0
        if x0 == 0:
            for y in range(max_y):
                matrix[y][0] = 0
        if y0 == 0:
            for x in range(max_x):
                matrix[0][x] = 0


if __name__ == '__main__':
    import doctest

    doctest.testmod()
