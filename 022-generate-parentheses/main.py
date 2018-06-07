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
    def doit(self, unclosed, n, s):
        if unclosed > 0:
            for i in self.doit(unclosed - 1, n, s + ")"):
                yield i
        if n > 0:
            for i in self.doit(unclosed + 1, n - 1, s + "("):
                yield i
        if unclosed == 0 and n == 0:
            yield s

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = [i for i in self.doit(0, n, "")]
        return sorted(answer)


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
