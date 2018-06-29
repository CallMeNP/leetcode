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
    def minDistance(self, word1, word2):
        """
        >>> s=Solution()
        >>> s.minDistance("horse","ros")
        3
        >>> s.minDistance("intention", "execution")
        5
        >>> s.minDistance("zoologicoarchaeologist", "zoogeologist")
        10

        :type word1: str
        :type word2: str
        :rtype: int
        """

        max_x = len(word1) + 1
        max_y = len(word2) + 1
        board = [[i] + list(range(1, max_x)) for i in range(max_y)]
        for y in range(1, max_y):
            for x in range(1, max_x):
                board[y][x] = min(board[y - 1][x] + 1,  # 一波操作之后，word2 插入一个字符变 word1
                                  board[y][x - 1] + 1,  # 一波操作之后，word1 插入一个字符变 word2
                                  board[y - 1][x - 1] + int(word1[x - 1] != word2[y - 1]))  # 替换
        return board[-1][-1]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
