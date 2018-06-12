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
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_valid_len = 0
        # stack = [-1]
        stack = []
        s = ")" + s
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
                # count+=1
            elif s[i] == ")":
                if stack:
                    stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    current_len = i - stack[-1]
                    max_valid_len = max(current_len, max_valid_len)
        return max_valid_len


if __name__ == '__main__':
    s = Solution()
    data = [
        ["()", 2],
        ["(()", 2],
        ["(()()", 4],
        ["(()()(", 4],
        ["(()(()", 2],
        ["((())", 4],
        ["()(())", 6],
        ["())))(())", 4],
        [")()(())", 6],
        [")))()(())", 6],
        [")))())))(())", 4],
        [")))()(())(((", 6],
    ]
    for d in data:
        answer = s.longestValidParentheses(d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
