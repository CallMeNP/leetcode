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
        last_sum = 0
        sum = 0
        while l < r:
            sum = nums[l] + nums[r]
            if sum == target:
                return sum
            if sum < target:
                l += 1
            else:
                r -= 1
            last_sum = sum
        if abs(last_sum - target) < abs(sum):
            print("pay attention")
            return last_sum
        return sum

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closet = math.inf
        nums = sorted(nums)
        x = len(nums)
        while 1 < x:
            x -= 1
            closet_2 = self.twoSumCloset(nums[:x], target - nums[x])
            diff = nums[x] + closet_2 - target
            if diff == 0:
                return diff
            closet = max(closet, diff)
        return closet


if __name__ == "__main__":

    s = Solution()

    data = [
        [[-1, 2, 1, -4], 1, 2],
        [[0, 0, 0, 0], 1, 0],
    ]

    for d in data:
        answer = s.threeSumClosest(d[0], d[1])
        if answer != d[2]:
            print(answer, d[2])
        else:
            print(True)
