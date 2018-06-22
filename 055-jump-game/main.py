#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
note: while i<end: i+=1  faster than for i in range()
"""


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        furthest = 0
        final = len(nums) - 1
        if not nums:
            return True
        i = 0
        while i <= furthest:
            nums[i] = nums[i] + i
            if nums[i] >= final:
                return True
            if furthest < nums[i]:
                furthest = nums[i]
            i += 1
        return False


if __name__ == '__main__':
    s = Solution()
    data = [
        [[1] * 10000, True],
        [[3, 2, 1, 0, 4], False],
    ]
    for d in data:
        answer = s.canJump(d[0])
        if answer == d[1]:
            print(True)
        else:
            print(False)
