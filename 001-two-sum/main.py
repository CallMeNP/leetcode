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
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] = [nums[i], i]
        nums.sort();
        left = 0
        right = len(nums) - 1
        while right > left:
            sum = nums[left][0] + nums[right][0]
            if sum > target:
                # need smaller
                right -= 1
            elif sum == target:
                return [nums[left][1], nums[right][1]]
            elif sum < target:
                # need bigger
                left += 1
        return []
