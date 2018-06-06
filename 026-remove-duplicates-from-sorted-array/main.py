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
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        insert_point = 0
        check_point = 1
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        while check_point < len_nums:
            if nums[insert_point] == nums[check_point]:
                check_point += 1
                continue
            insert_point += 1
            nums[insert_point] = nums[check_point]
            check_point += 1
        return insert_point + 1


if __name__ == "__main__":
    s = Solution()
    nums = [0]
    print s.removeDuplicates(nums), nums

    nums = [0, 0, 1]
    print s.removeDuplicates(nums), nums

    nums = [1, 2, 3]
    print s.removeDuplicates(nums), nums

    nums = []
    print s.removeDuplicates(nums), nums
