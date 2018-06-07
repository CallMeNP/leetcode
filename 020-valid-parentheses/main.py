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
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = {"{": 0, "[": 1, "(": 2}
        right = {"}": 0, "]": 1, ")": 2}
        for c in s:
            if c in left:
                stack.append(left[c])
            elif c in right:
                if not stack or right[c] != stack.pop():
                    return False
        if not stack:
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    data = [
        ["", True],
        ["()", True],
        ["(])", False],
        ["])", False],
        ["()[]{}", True],
    ]

    for d in data:
        answer = s.isValid(d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
