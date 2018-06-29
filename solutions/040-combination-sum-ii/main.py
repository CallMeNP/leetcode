#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
tags:DFS,回溯
"""


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()

        def sum_them(index_list):
            sum = 0
            for i in index_list:
                sum += candidates[i]
            return sum

        # 主要逻辑在这里
        def build_next(index_list):
            # 从后向前找到第一个不是最大值的位置
            # 如果所有值为最大值，已经遍历所有可能，通过清空stack来退出
            while index_list and (
                    index_list[-1] >= len(candidates) - 1 or candidates[index_list[-1]] == candidates[-1]):
                index_list.pop()
            if index_list:
                old_value = candidates[index_list[-1]]
                while index_list[-1] < len(candidates) and candidates[index_list[-1]] == old_value:
                    index_list[-1] += 1
                if index_list[-1] >= len(candidates):
                    # build_next(index_list)
                    # index_list.pop()
                    index_list.clear()
            return

        res = []
        stack = [0]
        while True:
            # print(stack,[candidates[i] for i in stack])
            if not stack:
                break
            s = sum_them(stack)
            if s == target:
                res.append([candidates[i] for i in stack])
                stack.pop()
                build_next(stack)
            if s < target:
                if stack[-1] + 1 > len(candidates) - 1:
                    stack.pop()
                    build_next(stack)
                else:
                    stack.append(stack[-1] + 1)
            if s > target:
                stack.pop()
                build_next(stack)
        return res


if __name__ == '__main__':
    s = Solution()
    data = [
        [([2, 3, 6, 7], 7), [[7]]],
        [([2, 3, 5], 8), [[3, 5]]],
        [([], 8), []],
        [([1, 1], 2), [[1, 1]]],
        [([1, 1, 1, 1], 5), []],
        [([7, 3, 2], 18), []],
        [([10, 1, 2, 7, 6, 1, 5], 8), [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]],
        [([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]]],
        [([4, 4, 2, 1, 4, 2, 2, 1, 3], 6), [[1, 1, 2, 2], [1, 1, 4], [1, 2, 3], [2, 2, 2], [2, 4]]],
    ]
    for d in data:
        answer = s.combinationSum2(*d[0])
        if sorted(answer) == sorted(d[1]):
            print(True)
        else:
            print(d, answer)
