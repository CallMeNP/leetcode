#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
使用公共变量的版本
"""


class Solution:
    def doit(self, unclosed, n, s):
        if unclosed > 0:
            self.doit(unclosed - 1, n, s + ")")
        if n > 0:
            self.doit(unclosed + 1, n - 1, s + "(")
        if unclosed == 0 and n == 0:
            self.answer.append(s)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.answer = []
        self.doit(0, n, "")
        return sorted(self.answer)


if __name__ == "__main__":
    s = Solution()
    data = [
        [3, ["((()))", "(()())", "(())()", "()(())", "()()()"]],
        [0, [""]],
        [1, ["()"]],
        [2, ["(())", "()()"]],
    ]
    for d in data:
        answer = s.generateParenthesis(d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
