#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""


def do_combine(start, end, k):
    if end - start + 1 < k or k < 1:
        pass
    elif k == 1:
        for i in range(start, end + 1):
            yield [i]
    else:
        for i in do_combine(start + 1, end, k - 1):
            yield [start] + i
        for i in do_combine(start + 1, end, k):
            yield i


class Solution:
    """
    >>> s=Solution()
    >>> s.subsets([1,2,3])
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> s.subsets([3])
    [[], [3]]
    >>> s.subsets([])
    [[]]
    """

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        n = len(nums)
        res = [[], nums]
        for j in range(n):
            for i in do_combine(0, n - 1, j):
                res.append([nums[k] for k in i])

        return sorted(res)


# leetcode 一个漂亮的解
# class Solution:
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         results=[[]]
#         for i in nums:
#             results=results+[[i]+num for num in results]
#         return results
if __name__ == '__main__':
    import doctest

    doctest.testmod()
