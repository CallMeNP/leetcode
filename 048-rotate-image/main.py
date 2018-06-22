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
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for x in range(len(matrix)):
            for y in range(x+1, len(matrix)):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
        for row in matrix:
            row.reverse()
