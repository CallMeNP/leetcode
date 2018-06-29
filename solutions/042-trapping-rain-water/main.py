#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 np <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
todo try dp
"""


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        res = 0
        stack = [0]
        for i in range(1, len(height)):
            # 如果栈为空
            # 入栈，不用设置新地板高度
            if not stack:
                stack.append(i)
                continue
            # 如果当前高度低于栈顶高度
            # 入栈不用更新地板
            if height[i] < height[stack[-1]]:
                stack.append(i)
                continue
            # 如果当前高度高于栈顶高度
            # {计算面积，出栈，更新地板}直到栈顶高于当前高度
            while stack and height[i] >= height[stack[-1]]:
                floor = height[stack[-1]]
                stack.pop()
                if not stack:
                    break
                res += (min(height[stack[-1]], height[i]) - floor) * (i - stack[-1] - 1)
            stack.append(i)

        return res


if __name__ == '__main__':
    s = Solution()
    data = [
        [[], 0],
        [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6],
        [[4, 2, 3], 1]
    ]
    for d in data:
        answer = s.trap(d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
