#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
bfs bad solution: TLE
"""


class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        class Node:
            def __init__(self, max_jump=0, color='white', distance=-1, pre=None, value=0):
                self.max_jump = max_jump
                self.color = color
                self.distance = distance
                self.pre = pre
                self.value = value

            def __str__(self):
                return "max_jump=%s,color=%s,distance=%s,value=%s" % (
                    self.max_jump, self.color, self.distance, self.value)

        queue = []
        len_nums = len(nums)
        obj_nums = []
        i = 0
        for n in nums:
            o = Node(max_jump=n, value=i)
            obj_nums.append(o)
            i += 1

        o = obj_nums[0]
        o.color = 'gray'
        o.distance = 0
        queue.append(o)
        while queue:
            # print([str(i) for i in queue])
            o = queue.pop(0)
            # print(o)
            if o.value == len_nums - 1:
                return o.distance
            for i in range(o.value + 1, o.value + o.max_jump + 1):
                if i > len_nums - 1:
                    break
                no = obj_nums[i]
                if no.color == 'white':
                    no.distance = o.distance + 1
                    no.color = 'gray'
                    no.pre = o
                    queue.append(no)
            o.color = 'black'


if __name__ == '__main__':
    s = Solution()
    data = [
        [[2, 3, 1, 1, 4], 2],
        [[2, 1], 1],
        [[1, 2, 1, 1, 1], 3],
    ]
    for d in data:
        answer = s.jump(d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
