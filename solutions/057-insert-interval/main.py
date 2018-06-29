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
    def insert(self, intervals, newInterval):
        """
        :type intervals: list[Interval]
        :type newInterval: Interval
        :rtype: list[Interval]
        """

        # if not intervals:
        #     return [newInterval]
        # i = 0
        # while i < len(intervals):
        #     # for i in range(len(intervals)):
        #     if intervals[i].start <= newInterval.start <= intervals[i].end \
        #             or newInterval.start <= intervals[i].start <= newInterval.end:
        #         newInterval.start = min(intervals[i].start, newInterval.start)
        #         newInterval.end = max(intervals[i].end, newInterval.end)
        #         intervals.pop(i)
        #     else:
        #         i += 1
        # intervals += [newInterval]
        # return sorted(intervals, key=lambda x: x.start)
        intervals+=[newInterval]
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
