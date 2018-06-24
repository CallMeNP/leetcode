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
    >>> nums=[1,1,1,2,2,3]
    >>> l=s.removeDuplicates(nums)
    >>> nums[:l]
    [1, 1, 2, 2, 3]
    >>> nums=[0,0,1,1,1,1,2,3,3]
    >>> l=s.removeDuplicates(nums)
    >>> nums[:l]
    [0, 0, 1, 1, 2, 3, 3]
    """

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        insert = 0
        check = 0
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        while check < len_nums:
            if check + 1 < len_nums and check + 2 < len_nums and nums[check] == nums[check + 1] == nums[check + 2]:
                check += 1
                continue
            if check + 1 < len_nums and nums[check] == nums[check + 1]:
                nums[insert] = nums[check]
                insert += 1
                check += 1
            nums[insert] = nums[check]
            insert += 1
            check += 1
        return insert


if __name__ == '__main__':
    import doctest

    doctest.testmod()
