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
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 常量
        negative_int_max = -(1 << 31)
        int_max = (1 << 31) - 1
        sign = 1
        # 非法
        if divisor == 0:
            raise Exception()
        # 溢出
        if dividend <= negative_int_max and divisor == -1:
            return int_max
        # sign
        if dividend < 0:
            sign *= -1
        if divisor < 0:
            sign *= -1
        answer = 0  # type: int
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            p_divisor = divisor
            p = 0
            while dividend >= p_divisor:
                p_divisor <<= 1
                p += 1
            p_divisor >>= 1
            dividend -= p_divisor
            answer += 1 << (p - 1)
            # print(p_divisor, 1 << p - 1, answer)
        answer *= sign
        return answer


if __name__ == '__main__':
    s = Solution()
    data = [
        [(1, 2), 0],
        [(2147483647, 1), int(2147483647 / 1)],
        [(-2147483648, 1), int(-2147483648 / 1)],
        [(-2147483648, 2), int(-2147483648 / 2)],
        [(-2147483648, 3), int(-2147483648 / 3)],
    ]
    for d in data:
        answer = s.divide(*d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
