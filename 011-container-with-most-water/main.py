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
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(area, max_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


if __name__ == "__main__":

    s = Solution()
    from data import data

    for d in data:
        answer = s.maxArea(d[0])
        if answer != d[1]:
            print(answer)
        else:
            print(True)
