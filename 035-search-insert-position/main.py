#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
tags:二分法
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right = mid
            else:
                left = mid + 1
        # target不存在时，left可能为0或len
        # 根据题目要求，返回0而不用处理成-1
        return left


if __name__ == '__main__':
    s = Solution()
    data = [
        [([], 4), 0],
        [([1, 2, 3, 4, 5, 6, 7], 4), 3],
        [([1, 2, 3, 4, 5, 6, 7, 8], 4), 3],
        [([0, 0, 1, 2, 3, 4], 4), 5],
        [([0, 0, 1, 1, 2, 3, 4], 4), 6],
        [([0, 0, 1, 2, 3, 3, 3, ], 4), 7],
        [([0, 0, 1, 1, 2, 3], 4), 6],
        [([4, 5, 6, 7], 4), 0],
        [([4, 5, 6, 7, 8], 4), 0],
        [([5, 6, 7, 7, 8], 4), 0],
        [([5, 6, 7, 7, 8, 8], 4), 0],
    ]
    for d in data:
        answer = s.searchInsert(*d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
