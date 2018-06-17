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
    def reverse(self, nums, start, end):
        """
        :param nums: list [int]
        :param start: int
        :param end: int
        :return: None
        """
        len_nums = len(nums)
        if not (0 <= start < len_nums and 0 <= end < len_nums):
            return
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def nextPermutation(self, nums):
        """
        :type nums: list [int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        # 从后向前找到第一个相邻递增对儿
        # 或者说list尾部递减序列的前一个元素
        for i in range(len(nums) - 2, -2, -1):
            if i >= 0 and nums[i] < nums[i + 1]:
                # 从后向前找到第一个大于i的数
                # 即使i是倒数第二个元素，此过程也能找到j
                for j in range(len(nums) - 1, 0, -1):
                    if nums[j] > nums[i]:
                        break
                # 交换
                nums[i], nums[j] = nums[j], nums[i]
                break
        # 此时，将i前的递减序列逆序
        # 如果整个序列递增，此时i为-1
        self.reverse(nums, i + 1, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    data = [
        [[], []],
        [[1, 2, 3], [1, 3, 2]],
        [[1, 3, 2], [2, 1, 3]],
        [[3, 2, 1], [1, 2, 3]],
        [[3, 2], [2, 3]],
        [[1, 2], [2, 1]],
        [[4, 2, 0, 2, 3, 2, 0], [4, 2, 0, 3, 0, 2, 2]],
    ]
    for d in data:
        s.nextPermutation(d[0])
        if d[0] == d[1]:
            print(True)
        else:
            print(d)
