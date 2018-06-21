#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
not good: time O(n), space O(n)
"""


class Solution:
    def jump(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        furthest_i = 0
        step = [0 for n in nums]
        for i in range(len(nums)):
            new_furthest_i = min(nums[i] + i, len(nums) - 1)
            d = step[i]
            if new_furthest_i > furthest_i:
                d = d + 1
                for j in range(furthest_i + 1, new_furthest_i + 1):
                    step[j] = d
                    if j == len(nums) - 1:
                        return d
                furthest_i = min(new_furthest_i, len(nums) - 1)
            if new_furthest_i == len(nums) - 1:
                return d


if __name__ == '__main__':
    s = Solution()
    data = [
        [[2, 3, 1, 1, 4], 2],
        [[2, 1], 1],
        [[0], 0],
        [[7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3], 2],
        [[1], 0],
        [[1, 2, 1, 1, 1], 3],
    ]
    for d in data:
        answer = s.jump(d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
