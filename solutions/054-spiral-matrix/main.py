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
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return []
        min_x = min_y = 0
        max_y = len(matrix)-1
        max_x = len(matrix[0])-1

        while True:
            if min_x > max_x or min_y > max_y:
                break
            for x in range(min_x, max_x+1):
                res.append(matrix[min_y][x])
            min_y += 1
            if min_x > max_x or min_y > max_y:
                break
            for y in range(min_y, max_y+1):
                res.append(matrix[y][max_x])
            max_x -= 1
            if min_x > max_x or min_y > max_y:
                break
            for x in range(max_x, min_x-1, -1):
                res.append(matrix[max_y][x])
            max_y -= 1
            if min_x > max_x or min_y > max_y:
                break
            for y in range(max_y, min_y-1, -1):
                res.append(matrix[y][min_x])
            min_x += 1
        return res
