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
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        index_stack = []
        heights.append(0)
        for right in range(len(heights)):
            # 一旦出现高度递减，通过计算，将队列中高于 heights[right] 的清除
            while len(index_stack) > 0 and heights[index_stack[-1]] >= heights[right]:
                h = heights[index_stack.pop()]
                if index_stack:
                    left = index_stack[-1]
                else:
                    left = -1
                # 坐标范围为开区间： (left,right)，不包括 left 和 right
                area = h * (right - left - 1)
                if area > max_area:
                    max_area = area
            # 高度递增的情况，入栈
            index_stack.append(right)
        return max_area


if __name__ == '__main__':
    s = Solution()
    from data import data

    for d in data:
        answer = s.largestRectangleArea(d[0])
        print(answer)
