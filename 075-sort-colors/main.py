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
    """
    >>> s=Solution()
    >>> nums= [2,0,2,1,1,0]
    >>> s.sortColors(nums)
    >>> nums
    [0, 0, 1, 1, 2, 2]
    """

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        i = left
        # while 0 <= left <= i <= right < len(nums):
        #     if nums[left] == 0:
        #         left += 1
        #         i = left
        #         continue
        #     if nums[right] == 2:
        #         right -= 1
        #         continue
        #     if nums[i] == 0:
        #         nums[left], nums[i] = nums[i], nums[left]
        #     elif nums[i] == 2:
        #         nums[right], nums[i] = nums[i], nums[right]
        #     else:
        #         i += 1
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1


if __name__ == '__main__':
    import doctest

    doctest.testmod()
