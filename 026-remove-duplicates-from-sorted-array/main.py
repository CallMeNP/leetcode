#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
leetcode 26
"""


class Solution:
    """
    >>> s=Solution()
    >>> nums=[1,1,1,2,2,3]
    >>> l=s.removeDuplicates(nums)
    >>> nums[:l]
    [1, 2, 3]
    >>> nums = [0]
    >>> l=s.removeDuplicates(nums)
    >>> nums[:l]
    [0]
    >>> nums = [0, 0, 1]
    >>> l=s.removeDuplicates(nums)
    >>> nums[:l]
    [0, 1]
    >>> nums = [1, 2, 3]
    >>> l=s.removeDuplicates(nums)
    >>> nums[:l]
    [1, 2, 3]
    >>> nums = []
    >>> l=s.removeDuplicates(nums)
    >>> nums[:l]
    []
    """

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        insert_point = 0
        check_point = 0
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        while check_point < len_nums:
            if check_point + 1 < len_nums and nums[check_point] == nums[check_point + 1]:
                check_point += 1
                continue
            nums[insert_point] = nums[check_point]
            insert_point += 1
            check_point += 1
        return insert_point


if __name__ == "__main__":
    import doctest

    doctest.testmod()
