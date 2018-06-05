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
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # 找第一个数字
        i = 0
        for i in range(len(str)):
            # 如果第一个非空字符是+-符号，判断后面是否为数字
            if str[i] == '-' or str[i] == '+':
                if i < len(str) - 1 and str[i + 1].isdigit():
                    continue
                # +-后面非数字，直接退出
                return 0
            if str[i].isdigit():
                break
            if not str[i].isspace():
                return 0
        # 没找到数字
        if i == len(str):
            return 0
        # 前面是否有负号
        is_negative = i > 0 and str[i - 1] == "-"  # 找最后一个数字
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        num = 0
        for j in range(i, len(str)):
            # 发现非数字终止循环
            if not str[j].isdigit():
                break
            # 将会溢出 返回INT_MAX or INT_MIN
            if num > INT_MAX / 10 or INT_MAX - num * 10 < int(str[j]):
                num = INT_MAX
                break
            if num < INT_MIN / 10 or num * 10 - INT_MIN < int(str[j]):
                num = INT_MIN
                break

            # x10+k
            num *= 10
            if is_negative:
                num -= int(str[j])
            else:
                num += int(str[j])

        return num


if __name__ == "__main__":
    s = Solution()
    data = [
        "",
        "0",
        "1",
        "-1",
        " -1 ",
        " -1234 ",
        " +1234 ",
        " +-1234 ",
        " --1234 ",
        " 1234 ",
        " 1 ",
        " -1234-123 ",
        " 2147483647 ",
        " 2147483648 ",
        " -2147483648 ",
        " -2147483649 ",
        "words and 987 ",
    ]
    for i in data:
        print(s.myAtoi(i))
