#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 np <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""

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
        if len(nums1) < len(nums2):
            longer, shorter = nums2, nums1
        len_longer = len(longer)
        len_shorter = len(shorter)
        if len_shorter == 0:
            if len_longer == 0:
                raise Exception("bad data")
            if len_longer % 2 == 1:
                return longer[(len_longer >> 1)]
            return (longer[len_longer >> 1] + longer[(len_longer >> 1) - 1]) / 2
        len_of_sum = len(longer) + len(shorter)
        len_of_left = len_of_sum >> 1
        imin = -1
        imax = len(shorter)

        while imin < imax:
            sl = imin + ((imax - imin) >> 1)  # type: int
            sr = sl + 1  # type: int
            ll = len_of_left - 1 - (sl + 1)  # type: int
            lr = ll + 1 + (len_of_sum % 2)  # type: int

            if 0 <= sl < len_shorter and 0 <= lr < len_longer:
                if shorter[sl] > longer[lr]:
                    imax = sl - 1
                    continue
            if 0 <= sr < len_shorter and 0 <= ll < len_longer:
                if longer[ll] > shorter[sr]:
                    imin = sl + 1
                    continue
            if sl < 0 and ll < 0:
                print("imin=", imin, "imax=",
                      imax, "longer_left=", ll, "longer_right=", lr, "shorter_left=", sl, "shorter_right=", sr)
                print(" if sl < 0 and ll < 0:")
                break
            if sr >= len_shorter and lr >= len_longer:
                print("imin=", imin, "imax=",
                      imax, "longer_left=", ll, "longer_right=", lr, "shorter_left=", sl, "shorter_right=", sr)
                print(" if sr > len_shorter and lr > len_longer:")
                # imin = sl + 1
                # continue
                break
            print("imin=", imin, "imax=",
                  imax, "longer_left=", ll, "longer_right=", lr, "shorter_left=", sl, "shorter_right=", sr)
            break

        sl = imin + ((imax - imin) >> 1)  # type: int
        sr = sl + 1  # type: int
        ll = len_of_left - 1 - (sl + 1)  # type: int
        lr = ll + 1 + (len_of_sum % 2)  # type: int
        print("imin=", imin, "imax=",
              imax, "longer_left=", ll, "longer_right=", lr, "shorter_left=", sl, "shorter_right=", sr)
        if ll < 0:
            max_left = shorter[sl]
        elif sl < 0:
            max_left = longer[ll]
        else:
            max_left = max(longer[ll], shorter[sl])
        if lr >= len_longer:
            min_right = shorter[sr]
        elif sr >= len_shorter:
            min_right = longer[lr]
        else:
            min_right = min(longer[lr], shorter[sr])

        if len_of_sum % 2 == 1:
            return min(max(longer[ll + 1], max_left), min_right)
        return (max_left + min_right) / 2


if __name__ == '__main__':
    s = Solution()
    d = [
        [[1], [0]],
        [[1], [2]],
        [[1, 2], [2, 3]],
        [[6, 7, 8], [2, 3, 4, 5]],
        [[1, 2, 4], [2, 3, 4, 5]],
        [[6], [2, 3, 4, 5]],
        [[1], [2, 3, 4, 5]],
        [[6], [2, 3, 4]],
        [[1], [2, 3, 4]],
        [[], [1]],
        [[], [2, 3]],
        [[], [1, 2, 3, 4, 5]],
        [[3, 4], [1, 2]],
        [[1, 5, 6, 8], [2, 3, 4, 7]]
    ]
    for i in range(len(d)):
        try:
            print(d[i], "\n", s.findMedianSortedArrays(d[i][0], d[i][1]), "\n")
        except Exception as e:
            print(d[i], e)
