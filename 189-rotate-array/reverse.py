#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""


class Solution(object):
    def reverse(self, nums, start, end):
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0 or k <= 0:
            return
        k = k % len(nums)

        self.reverse(nums, 0, len(nums) - 1 - k)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    s.rotate(nums, 8)
    print nums

    nums = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(nums, 3)
    print nums

    nums = [1]
    s.rotate(nums, 3)
    print nums