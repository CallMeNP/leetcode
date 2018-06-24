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
    >>> board=[ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ]
    >>> s.exist(board,"ABCCED")
    True
    >>> s.exist(board,"SEE")
    True
    >>> s.exist(board,"ABCB")
    False
    >>> s.exist(board,"CESEEC")
    True
    >>> s.exist(board,"CESEECC")
    False
    >>> s.exist([],"CESEECC")
    False
    >>> s.exist([[]],"CESEECC")
    False
    >>> s.exist([],"")
    True
    """

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board:
            return False
        path = []
        max_x = len(board[0])
        max_y = len(board)

        def find(x, y, i):
            # 三种不匹配
            if not 0 <= x < max_x or not 0 <= y < max_y:
                return False
            if (x, y) in path:
                return False
            if board[y][x] != word[i]:
                return False

            # 匹配
            path.append((x, y))
            i += 1
            # 已经是最后一个字符
            if i >= len(word):
                return True

            # 还有剩余字符
            # 测试周围四个坐标
            a = find(x - 1, y, i)
            b = find(x, y + 1, i)
            c = find(x + 1, y, i)
            d = find(x, y - 1, i)

            # 因为仅当完全匹配剩余字符才会返回True
            # 所以只要有一个返回True，即向上传递True
            if a or b or c or d:
                return True
            # 如果四个坐标都失败（因为上面三种不匹配）
            # 将本次增加的路径跟踪点弹出
            # 返回False
            path.pop()
            return False

        for y in range(max_y):
            for x in range(max_x):
                i = 0
                if find(x, y, i):
                    return True
        return False


if __name__ == '__main__':
    import doctest

    doctest.testmod()
