#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 np <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
leetcode p4 O(log(min(len(nums1),len(nums2))))
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        longer = nums1
        shorter = nums2
        len_longer = len(longer)
        len_shorter = len(shorter)
        if len_longer < len_shorter:
            longer, shorter, len_longer, len_shorter = nums2, nums1, len_shorter, len_longer
        len_of_sum = len_longer + len_shorter
        is_odd = len_of_sum % 2  # type: int # 总元素数是否为奇数
        len_of_left = len_of_sum >> 1  # 应位于中位数左侧的元素个数

        # 长数组为空，短必然空，无定义
        if len_longer == 0:
            raise Exception("undefined")
        # 短为空，直接O(1)返回
        if len_shorter == 0:
            if is_odd:
                return longer[len_of_left]
            return (longer[len_of_left] + longer[len_of_left - 1]) / 2

        low = 0  # type:int # 短数组的下标下界
        high = len_shorter  # type:int # 短数组的下标上界
        while low <= high:
            sr = low + ((high - low) >> 1)  # type: int # shorter中，切分线右侧的元素下标
            sl = sr - 1  # type: int # shorter中，切分线左侧的元素下标
            ll = len_of_left - (sl + 1) - 1  # type: int # longer 中，中位数左侧的元素
            lr = ll + 1 + is_odd  # type: int # longer中，中位数右侧的元素

            if 0 <= sl < len_shorter and 0 <= lr < len_longer:
                if shorter[sl] > longer[lr]:
                    high = sr - 1
                    continue
            if 0 <= sr < len_shorter and 0 <= ll < len_longer:
                if longer[ll] > shorter[sr]:
                    low = sr + 1
                    continue
            break

        # ll sl 不会同时<0
        if ll < 0:
            max_left = shorter[sl]
        elif sl < 0:
            max_left = longer[ll]
        else:
            max_left = max(longer[ll], shorter[sl])

        # lr sr 不会同时>len
        if lr >= len_longer:
            min_right = shorter[sr]
        elif sr >= len_shorter:
            min_right = longer[lr]
        else:
            min_right = min(longer[lr], shorter[sr])

        if is_odd:
            return min(max(longer[ll + 1], max_left), min_right)
        return (max_left + min_right) / 2


if __name__ == '__main__':
    s = Solution()
    data = [
        [[1], [0], 0.5],
        [[1], [2], 1.5],
        [[1, 2], [2, 3], 2.0],
        [[6, 7, 8], [2, 3, 4, 5], 5],
        [[1, 2, 4], [2, 3, 4, 5], 3],
        [[6], [2, 3, 4, 5], 4],
        [[1], [2, 3, 4, 5], 3],
        [[6], [2, 3, 4], 3.5],
        [[1], [2, 3, 4], 2.5],
        [[], [1], 1],
        [[], [2, 3], 2.5],
        [[], [1, 2, 3, 4, 5], 3],
        [[3, 4], [1, 2], 2.5],
        [[1, 5, 6, 8], [2, 3, 4, 7], 4.5]
    ]
    for d in data:
        answer = s.findMedianSortedArrays(d[0], d[1])
        if answer == d[2]:
            print(True)
        else:
            print(d[0], d[1], answer, answer == d[2], "\n")
