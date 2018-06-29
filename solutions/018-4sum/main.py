#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
time O(n^2)
space O(n^2)
"""
# todo 尝试空间消耗更小的方案？
import itertools


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        pair_dict = {}
        self.num_dict = {}
        for i in nums:
            if i in self.num_dict:
                self.num_dict[i] += 1
            else:
                self.num_dict[i] = 1
        answer = set()
        for c in itertools.combinations(nums, 2):
            s = sum(c)
            if s in pair_dict:
                pair_dict[s].append(c)
            else:
                pair_dict[s] = [c]
        # for half_a in pair_dict:
        while pair_dict:
            half_and_pair = pair_dict.popitem()
            half_a = half_and_pair[0]
            pairs_a = half_and_pair[1]

            half_b = target - half_a
            if half_b == half_a:
                if len(pairs_a) <= 1:
                    continue
                for a_i in range(len(pairs_a) - 1):
                    n4 = pairs_a[a_i] + pairs_a[a_i + 1]
                    if self.is_valid_4_nums(n4):
                        answer.add(tuple(sorted(n4)))
                continue
            if half_b not in pair_dict:
                continue
            for a_i in range(len(pairs_a)):
                for b_i in range(len(pair_dict[half_b])):
                    n4 = pairs_a[a_i] + pair_dict[half_b][b_i]
                    if self.is_valid_4_nums(n4):
                        answer.add(tuple(sorted(n4)))
        # print(self.num_dict)
        return sorted([list(i) for i in answer])

    def is_valid_4_nums(self, n4):
        n4_count = {}
        for i in n4:
            if i in n4_count:
                n4_count[i] += 1
            else:
                n4_count[i] = 1
        for i in n4_count:
            if n4_count[i] > self.num_dict[i]:
                return False
        return True


if __name__ == "__main__":
    import operator

    s = Solution()
    data = [
        [[1, 0, -1, 0, -2, 2], 0, [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]],
        [[1, 0, -1], 0, []],
        [[-1, -2, 1, 2], 0, [[-2, -1, 1, 2]]]
    ]

    for d in data:
        answer = s.fourSum(d[0], d[1])
        if operator.ne(answer, sorted(d[2])):
            print(answer)
        else:
            print(True)
