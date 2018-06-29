#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
tags:dp
"""


# 原始版本
# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid):
#         """
#         :type obstacleGrid: List[List[int]]
#         :rtype: int
#         """
#         o = obstacleGrid
#         if len(o) < 1 or len(o[0]) < 1:
#             return 0
#         if o[0][0] == 1:
#             return 0
#         for y in range(len(o)):
#             for x in range(len(o[0])):
#                 if o[y][x] == 1:
#                     o[y][x] = 0
#                 elif x == 0 and y == 0:
#                     o[y][x] = 1
#                 elif x == 0:
#                     o[y][x] = o[y - 1][x]
#                 elif y == 0:
#                     o[y][x] = o[y][x - 1]
#                 elif o[y][x] == 0:
#                     o[y][x] = o[y][x - 1] + o[y - 1][x]
#         return o[y][x]

# 改了一下并没有变快
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        o = obstacleGrid
        if len(o) < 1 or len(o[0]) < 1:
            return 0
        if o[0][0] == 1:
            return 0
        o[0][0] = 1
        for y in range(1, len(o)):
            if o[y][0] == 0:
                o[y][0] = o[y - 1][0]
            else:
                o[y][0] = 0
        for x in range(1, len(o[0])):
            if o[0][x] == 0:
                o[0][x] = o[0][x - 1]
            else:
                o[0][x] = 0

        for y in range(1, len(o)):
            for x in range(1, len(o[0])):
                if o[y][x] == 0:
                    o[y][x] = o[y][x - 1] + o[y - 1][x]
                else:  # ==1
                    o[y][x] = 0

        return o[len(o) - 1][len(o[0]) - 1]


if __name__ == '__main__':
    s = Solution()
    data = [
        [[[0], [0]], 1],
        [[[0]], 1],
        [[[1]], 0],
        [[[1, 0]], 0],
        [[[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2]
    ]
    for d in data:
        answer = s.uniquePathsWithObstacles(d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
