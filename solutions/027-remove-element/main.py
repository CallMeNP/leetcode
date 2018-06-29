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
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        insert_point = len(nums) - 1
        check_point = 0
        # while check_point <= insert_point:
        #     while insert_point >= 0 and nums[insert_point] == val:
        #         insert_point -= 1
        #     if insert_point < 0:
        #         break
        #     if nums[check_point] == val:
        #         nums[check_point], nums[insert_point] = nums[insert_point], nums[check_point]
        #     else:
        #         check_point += 1
        while 0 <= insert_point and check_point < len(nums) and check_point <= insert_point:
            if nums[check_point] == val:
                nums[check_point], nums[insert_point] = nums[insert_point], nums[check_point]
            while 0 <= insert_point and nums[insert_point] == val:
                insert_point -= 1
            while check_point < len(nums) and nums[check_point] != val:
                check_point += 1

        return insert_point + 1


if __name__ == '__main__':
    s = Solution()
    data = [
        [[3, 2, 2, 3], 3, [2, 2], 2],
        [[3, 2, 2, 3], 2, [3, 3], 2],
        [[3, 2], 3, [2], 1],
        [[3, 2], 2, [3], 1],
        [[3], 3, [], 0],
        [[], 3, [], 0],
    ]
    for d in data:
        anwser = s.removeElement(d[0], d[1])
        if d[0][:anwser] == d[2] and anwser == d[3]:
            print(True)
        else:
            print(d, anwser)
