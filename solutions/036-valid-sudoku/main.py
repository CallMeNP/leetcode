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
    def remove_dot(self, l):
        return list(filter(lambda i: i != ".", l))

    def get_9_from_col(self, i):
        return [row[i] for row in self.board]

    def get_9_from_3x3(self, x, y):
        if not 0 <= y < 9:
            raise Exception("bad y")
        if not 0 <= x < 9:
            raise Exception("bad x")
        x = x // 3 * 3
        y = y // 3 * 3
        return [self.board[y + dy][x + dx] for dx in range(3) for dy in range(3)]

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        self.board = board
        for row in board:
            l = self.remove_dot(row)
            if self.containsDuplicate(l):
                return False
        for i in range(9):
            l = self.get_9_from_col(i)
            l = self.remove_dot(l)
            if self.containsDuplicate(l):
                return False
        for x in [0, 3, 6]:
            for y in [0, 3, 6]:
                l = self.get_9_from_3x3(x, y)
                l = self.remove_dot(l)
                if self.containsDuplicate(l):
                    return False
        return True

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) < len(nums)


if __name__ == '__main__':
    s = Solution()
    data = [
        [
            [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]], True],
        [
            [["8", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]], False],
        [
            [['3', '5', '1', '2', '8', '6', '4', '9', '7'],
             ['4', '9', '2', '1', '5', '7', '6', '3', '8'],
             ['7', '8', '6', '9', '3', '4', '5', '1', '2'],
             ['2', '7', '5', '4', '6', '9', '1', '8', '3'],
             ['9', '3', '8', '5', '2', '1', '7', '6', '4'],
             ['6', '1', '4', '8', '7', '3', '2', '5', '9'],
             ['8', '2', '9', '6', '4', '5', '3', '7', '1'],
             ['1', '6', '3', '7', '9', '2', '8', '4', '5'],
             ['5', '4', '7', '3', '1', '8', '9', '2', '6']], True]
    ]
    for d in data:
        answer = s.isValidSudoku(d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
