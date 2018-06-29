#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
note: [0]*n 生成数组，但是[[0]*n]不能生成矩阵，生成的是一个数组的多个引用
"""


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        matrix = [[0] * n for i in range(n)]
        min_x = min_y = 0
        max_y = n - 1
        max_x = n - 1
        k = 1

        while True:
            if min_x > max_x or min_y > max_y:
                break
            for x in range(min_x, max_x + 1):
                matrix[min_y][x] = k
                k += 1
            min_y += 1
            if min_x > max_x or min_y > max_y:
                break
            for y in range(min_y, max_y + 1):
                matrix[y][max_x] = k
                k += 1
            max_x -= 1
            if min_x > max_x or min_y > max_y:
                break
            for x in range(max_x, min_x - 1, -1):
                matrix[max_y][x] = k
                k += 1
            max_y -= 1
            if min_x > max_x or min_y > max_y:
                break
            for y in range(max_y, min_y - 1, -1):
                matrix[y][min_x] = k
                k += 1
            min_x += 1
        return matrix


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(3))
