#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""

from mod.dfs import DFSTree


class Solution(DFSTree):
    def __init__(self):
        DFSTree.__init__(self)
        self.candidates = []
        self.stack = []
        self.result = []
        self.target = None

    def sum_current_choice(self):
        sum = 0
        for i in self.stack:
            sum += self.candidates[i]
        return sum

    def is_target(self):
        print([self.candidates[i] for i in self.stack])
        return self.sum_current_choice() == self.target

    def found(self):
        self.result.append([self.candidates[i] for i in self.stack])

    def has_children(self):
        return self.sum_current_choice() < self.target

    def visit_first_child(self):
        self.stack.append(self.stack[-1])

    def has_next_sibling(self):
        if not self.stack:
            return False
        return self.sum_current_choice() < self.target and self.stack[-1] < len(self.candidates) - 1

    def visit_next_sibling(self):
        self.stack[-1] += 1

    def has_parent(self):
        return len(self.stack)

    def back_to_parent(self):
        self.stack.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: list[int]
        :type target: int
        :rtype: list[list[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        self.__init__()
        self.candidates = candidates
        self.target = target
        self.stack.append(0)
        self.depth_first_search()
        return self.result


if __name__ == '__main__':
    s = Solution()
    data = [
        [([2, 3, 6, 7], 7), [[7], [2, 2, 3]]],
        [([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]]],
        [([], 8), []],
        [([7, 3, 2], 18),
         [[2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 3, 3], [2, 2, 2, 2, 3, 7], [2, 2, 2, 3, 3, 3, 3],
          [2, 2, 7, 7], [2, 3, 3, 3, 7], [3, 3, 3, 3, 3, 3]]],
    ]
    for d in data:
        answer = s.combinationSum(*d[0])
        if sorted(answer) == sorted(d[1]):
            print(True)
        else:
            print(d, answer)
