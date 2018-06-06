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
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        matrix = []
        if s == "" or numRows <= 0:
            return ""
        if numRows == 1:
            return s

        for i in range(numRows):
            matrix.append([])

        j = 0
        i = 0
        while i < len(s):
            matrix[j].append(s[i])
            i += 1
            if j == 0:
                delta = 1
            elif j == numRows - 1:
                delta = -1
            j += delta
        print(matrix)

        answer = ""
        for i in range(numRows):
            answer += "".join(matrix[i])
        return answer


if __name__ == "__main__":
    s = Solution()
    data = [
        ["", 3, ""],
        ["a", 3, "a"],
        ["ab", 1, "ab"],
        ["a", 0, ""],
        ["abcdefg", 3, "aebdfcg"],
        ["PAYPALISHIRING", 4, "PINALSIGYAHRPI"],
        ["PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"],
    ]
    for i in data:
        # todo 测试数据作为参数传入，元组会更方便么
        print(s.convert(i[0], i[1]) == i[2])
