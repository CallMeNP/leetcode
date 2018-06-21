#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
tags: greedy
"""


class Solution:
    def jump(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        step = 0
        last_pos = -1
        furthest = 0
        while furthest < len(nums) - 1:
            step += 1
            next_furthest = furthest
            for i in range(last_pos + 1, furthest + 1):
                if i + nums[i] > next_furthest:
                    next_furthest = i + nums[i]
            last_pos = furthest
            furthest = next_furthest
        return step


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
