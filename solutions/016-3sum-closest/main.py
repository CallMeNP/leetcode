#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""
import math


class Solution:
    def twoSumCloset(self, nums, target):
        l = 0
        r = len(nums) - 1
        if len(nums) < 2:
            return 0
        closet = 0
        min_diff = math.inf
        while l < r:
            sum = nums[l] + nums[r]
            if sum == target:
                return sum

            diff = abs(target - sum)
            if diff < min_diff:
                min_diff = diff
                closet = sum

            if sum < target:
                l += 1
            else:
                r -= 1
        return closet

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_diff = math.inf
        closet = math.inf
        nums = sorted(nums)
        x = len(nums) - 1
        while 1 < x:
            closet_2 = self.twoSumCloset(nums[:x], target - nums[x])
            sum = nums[x] + closet_2
            if sum == target:
                return sum

            diff = abs(nums[x] + closet_2 - target)
            if diff < min_diff:
                min_diff = diff
                closet = sum

            x -= 1
        return closet


if __name__ == "__main__":

    s = Solution()

    data = [
        [[-1, 2, 1, -4], 1, 2],
        [[-3, 0, 1, 2], 1, 0],
        [[0, 0, 0, 0], 1, 0],
    ]

    for d in data:
        answer = s.threeSumClosest(d[0], d[1])
        if answer != d[2]:
            print(answer, d[2])
            print("----")
        else:
            print(True)
