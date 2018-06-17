#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
todo 需要重写，去除find_min
"""


def find_min(nums, left, right):
    """
    :param nums: list[int]
    :param left: int
    :param right: int
    :return: int
    """
    mid = (left + right) >> 1
    if mid == left:
        if nums[left] < nums[right]:
            return left
        else:
            return right
    if nums[left] > nums[mid]:
        return find_min(nums, left, mid)
    if nums[mid] > nums[right]:
        return find_min(nums, mid, right)
    l = find_min(nums, left, mid)
    r = find_min(nums, mid, right)
    if nums[l] < nums[r]:
        return l
    return r


class Solution:
    def bin_search(self, left, right):
        """
        :param left: int
        :param right: int
        :return: int
        """
        if left == right:
            if self.nums[self.new_index(left)] == self.target:
                print(left, self.new_index(left))
                return self.new_index(left)
            print(-1)
            return -1
        mid = (left + right) >> 1
        if self.nums[self.new_index(mid)] == self.target:
            print(mid, self.new_index(mid))
            return self.new_index(mid)
        if self.target < self.nums[self.new_index(mid)]:
            return self.bin_search(left, mid)
        if self.nums[self.new_index(mid)] < self.target:
            return self.bin_search(mid + 1, right)

    def search(self, nums, target):
        """
        :type nums: list[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        self.nums = nums
        self.target = target
        len_nums = len(nums)
        min_index = find_min(nums, 0, len(nums) - 1)
        self.new_index = lambda x: (x + min_index) % len_nums
        return self.bin_search(0, len_nums - 1)


if __name__ == '__main__':
    s = Solution()
    data = [
        [([4, 5, 6, 7, 0, 1, 2], 0), 4],
        [([4, 5, 6, 7, 0, 1, 2], 3), -1],
        [([3, 3, 3, 3, 3, 3, 1, 2, 3], 3), 1],
        [([3, 3, 3, 3, 3, 3, 1, 2, 3], 1), 6],
        [([3, 3, 3, 3, 3, 3, 1, 2, 3], 2), 7],
    ]
    for d in data:
        answer = s.search(*d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
