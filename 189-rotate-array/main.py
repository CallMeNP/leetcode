#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 gaohailong <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
leetcode 189 O(1) extra space
"""


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        # 将k>lenNums的情况化简
        k = k % len_nums
        if k == 0:
            return
        cycle_num = self.gcd(len_nums, k)
        for cycle_i in range(cycle_num):
            step_i = cycle_i
            step_j = step_i - k
            step_j %= len_nums
            tmp = nums[cycle_i]
            while step_j != cycle_i:
                nums[step_i] = nums[step_j]
                step_i -= k
                step_j -= k
                step_i %= len_nums
                step_j %= len_nums
            nums[step_i] = tmp

    def gcd(self, a, b):
        if a % b == 0:
            return b
        return self.gcd(b, a % b)


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
