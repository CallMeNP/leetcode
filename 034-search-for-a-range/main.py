#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
STL equal_range
"""


def lower_bound(nums, target):
    """
    :type nums: list[int]
    :type target: int
    :rtype: list[int]
    """
    pass
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) >> 1
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1
    # 如果不存在，left可能=0和len
    if left < len(nums) and nums[left] == target:
        return left
    return -1


def upper_bound(nums, target):
    """
    :type nums: list[int]
    :type target: int
    :rtype: list[int]
    """
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) >> 1
        if target < nums[mid]:
            right = mid
        else:
            left = mid + 1
    # 如果不存在，left可能=0和len
    # 转为-1或len-1
    left -= 1
    if left >= 0 and nums[left] == target:
        return left
    return -1


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: list[int]
        :type target: int
        :rtype: list[int]
        """
        lower = lower_bound(nums, target)
        upper = upper_bound(nums, target)
        return [lower, upper]


if __name__ == '__main__':
    s = Solution()
    data = [
        [([], 4), -1],
        [([1, 2, 3, 4, 4, 4, 5, 6, 7], 4), 5],
        [([1, 2, 3, 4, 4, 4, 5, 6, 7, 8], 4), 5],
        [([0, 0, 1, 2, 3, 4, 4, 4], 4), 7],
        [([0, 0, 1, 1, 2, 3, 4, 4, 4], 4), 8],
        [([0, 0, 1, 2, 3, 3, 3, ], 4), -1],
        [([0, 0, 1, 1, 2, 3], 4), -1],
        [([4, 4, 4, 5, 6, 7], 4), 2],
        [([4, 4, 4, 5, 6, 7, 8], 4), 2],
        [([4, 5, 6, 7, 8], 4), 0],
        [([4, 5, 6, 7], 4), 0],
        [([5, 6, 7, 7, 8], 4), -1],
        [([5, 6, 7, 7, 8, 8], 4), -1],
    ]
    for d in data:
        answer = upper_bound(*d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
    data = [
        [([], 4), -1],
        [([1, 2, 3, 4, 4, 4, 5, 6, 7], 4), 3],
        [([1, 2, 3, 4, 4, 4, 5, 6, 7, 8], 4), 3],
        [([0, 0, 1, 2, 3, 4, 4, 4], 4), 5],
        [([0, 0, 1, 1, 2, 3, 4, 4, 4], 4), 6],
        [([0, 0, 1, 2, 3, 3, 3, ], 4), -1],
        [([0, 0, 1, 1, 2, 3], 4), -1],
        [([4, 4, 4, 5, 6, 7], 4), 0],
        [([4, 4, 4, 5, 6, 7, 8], 4), 0],
        [([4, 5, 6, 7, 8], 4), 0],
        [([4, 5, 6, 7], 4), 0],
        [([5, 6, 7, 7, 8], 4), -1],
        [([5, 6, 7, 7, 8, 8], 4), -1],
    ]
    for d in data:
        answer = lower_bound(*d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
