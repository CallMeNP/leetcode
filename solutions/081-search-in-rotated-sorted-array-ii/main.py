#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
todo 需要整理代码
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
        if nums[left-1] > nums[left]:
            return left
        else:
            return right
    if nums[left] > nums[mid]:
        return find_min(nums, left, mid)
    if nums[mid] > nums[right]:
        return find_min(nums, mid, right)
    l = find_min(nums, left, mid)
    r = find_min(nums, mid, right)
    if nums[l-1] > nums[l]:
        return l
    return r


class Solution:
    """
    >>> s=Solution()
    >>> find_min([1,1,1,1,3],0,4)
    0
    >>> s.search([1,1,1,1,3],3)
    True
    >>> s.search([1,1,3,1,1],3)
    True
    >>> s.search([1,1,1,3,1,1],3)
    True
    >>> s.search([2,5,6,0,0,1,2],0)
    True
    """

    def bin_search(self, left, right):
        """
        :param left: int
        :param right: int
        :return: int
        """
        if left == right:
            if self.nums[self.new_index(left)] == self.target:
                return self.new_index(left)
            return -1
        mid = (left + right) >> 1
        if self.nums[self.new_index(mid)] == self.target:
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
            return False
        self.nums = nums
        self.target = target
        len_nums = len(nums)
        min_index = find_min(nums, 0, len(nums) - 1)
        self.new_index = lambda x: (x + min_index) % len_nums
        return self.bin_search(0, len_nums - 1) != -1


if __name__ == '__main__':
    import doctest

    doctest.testmod()
