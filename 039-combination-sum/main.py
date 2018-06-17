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
    def combinationSum(self, candidates, target):
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
            while index_list and index_list[-1]>=len(candidates)-1:
                index_list.pop()
            if index_list:
                index_list[-1]+=1
            return

        res = []
        stack = [0]
        while True:
            if not stack:
                break
            s = sum_them(stack)
            if s == target:
                res.append([candidates[i] for i in stack])
                stack.pop()
                build_next(stack)
            if s < target:
                stack.append(stack[-1])
            if s > target:
                stack.pop()
                build_next(stack)
        return res


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
