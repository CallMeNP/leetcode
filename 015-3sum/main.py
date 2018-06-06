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
    def twoSum(self, nums, target):
        """
        :type nums: List[int] **sorted**
        :type target: int
        :rtype: List[int]
        """
        answer = set()
        left = 0
        right = len(nums) - 1
        while right > left:
            sum = nums[left] + nums[right]
            if sum > target:
                # need smaller
                right -= 1
                # while right > left and nums[right + 1] == nums[right]:
                #     right -= 1
            elif sum == target:
                answer.add((left, right))
                left += 1
                # while right > left and nums[left - 1] == nums[left]:
                #     left += 1
                right -= 1
                # while right > left and nums[right + 1] == nums[right]:
                #     right -= 1
            elif sum < target:
                # need bigger
                left += 1
                # while right > left and nums[left - 1] == nums[left]:
                #     left += 1
        return sorted([list(i) for i in answer])

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = set()
        target = 0

        nums.sort()

        x = len(nums)
        match = nomatch = 0
        while 1 < x:
            x -= 1
            while x - 3 > 1 and nums[x - 3:x + 1] == [nums[x]] * 4:
                x -= 1
            answers_of_two = []
            if nums[0] + nums[1] + nums[x] <= target <= nums[x - 2] + nums[x - 1] + nums[x]:
                answers_of_two = self.twoSum(nums[:x], target - nums[x])
                match += 1
            else:
                nomatch += 1
            if answers_of_two:
                for i in answers_of_two:
                    answer.add(tuple(sorted([nums[x], nums[i[0]], nums[i[1]]])))

        print(nomatch, match)
        return sorted([list(i) for i in answer])


if __name__ == "__main__":
    import operator

    s = Solution()
    import data

    for d in data.data:
        answer = s.threeSum(d[0])
        if operator.ne(answer, sorted(d[1])):
            print(answer)
        else:
            print(True)
