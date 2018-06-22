#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: list[Interval]
        :rtype: list[Interval]
        """
        # Method I
        # intervals.sort(key=lambda a: a.start, reverse=True)
        # for i in range(len(intervals) - 1, 0, -1):
        #     if intervals[i].end >= intervals[i - 1].start:
        #         intervals[i - 1].start = intervals[i].start
        #         intervals[i - 1].end = max(intervals[i].end, intervals[i - 1].end)
        #         intervals.pop(i)
        # return intervals

        # Method II
        # intervals.sort(key=lambda a: a.start)
        # i = 0
        # while i < len(intervals) - 1:
        #     if intervals[i].end >= intervals[i + 1].start:
        #         # intervals[i + 1].start = intervals[i].start
        #         intervals[i].end = max(intervals[i].end, intervals[i + 1].end)
        #         intervals.pop(i + 1)
        #     else:
        #         i += 1
        # return intervals

        # Method III
        if not intervals:
            return intervals
        res = []
        intervals.sort(key=lambda a: a.start)
        i = 0
        while i < len(intervals) - 1:
            if intervals[i].end >= intervals[i + 1].start:
                intervals[i + 1].start = intervals[i].start
                intervals[i + 1].end = max(intervals[i].end, intervals[i + 1].end)
            else:
                res.append(intervals[i])
            i += 1
        res.append(intervals[i])
        return res
