#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""

# todo 待尝试非递归的写法
class Solution:
    def __init__(self):
        self.keys = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digits = str(digits)
        answer = []
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(self.keys[int(digits[0])])
        for i in self.keys[int(digits[0])]:
            other = self.letterCombinations(digits[1:])
            for j in other:
                answer.append(i + j)
        return answer


if __name__ == "__main__":
    s = Solution()
    data = [
        [23, ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]]
    ]
    for d in data:
        answer = s.letterCombinations(d[0])
        answer.sort()
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
