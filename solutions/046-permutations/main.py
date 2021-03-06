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
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def find_last_incr(nums):
            if not nums:
                return -1
            for i in range(len(nums) - 1, 0, -1):
                if nums[i - 1] < nums[i]:
                    return i - 1
            return -1

        def find_swap_place(nums, i):
            for j in range(i + 1, len(nums)):
                if nums[j] <= nums[i]:
                    return j - 1
            return j

        def reverse(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        res = []
        nums.sort()
        res.append(nums[:])
        i = find_last_incr(nums)
        while i != -1:
            j = find_swap_place(nums, i)
            nums[i], nums[j] = nums[j], nums[i]
            reverse(nums, i + 1, len(nums) - 1)
            res.append(nums[:])
            i = find_last_incr(nums)
        return res


if __name__ == '__main__':
    s = Solution()
    data = [
        [[], [[]]],
        [[1], [[1]]],
        [[1, 2], [[1, 2], [2, 1]]],
        [[1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]],
    ]
    for d in data:
        answer = s.permute(d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
