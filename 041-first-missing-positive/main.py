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
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        check = 0
        len_nums = len(nums)
        while check < len_nums:
            target = nums[check] - 1
            # target 超出范围
            if not 0 <= target < len_nums:
                check += 1
                continue
            # check 是合法值
            if target == check:
                check += 1
                continue
            # target 的值是合法值
            if nums[target] - 1 == target:
                nums[check] = 0
                check += 1
                continue
            # target 与 check 所在的值都不合法
            # 交换，使target合法。所以check不需要+1
            if 0 <= target < len_nums:
                nums[check], nums[target] = nums[target], nums[check]
                continue
        i = 0
        while i < len_nums:
            if nums[i] - 1 == i:
                i += 1
                continue
            break
        return i + 1


if __name__ == '__main__':
    s = Solution()
    data = [
        [[3, 4, -1, 1], 2],
        [[1, 2, 0], 3],
        [[7, 8, 9, 11, 12], 1],
        [[1, 2, 3], 4],
        [[1, 1], 2],
    ]
    for d in data:
        answer = s.firstMissingPositive(d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
