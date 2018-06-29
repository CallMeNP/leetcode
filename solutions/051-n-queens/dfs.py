#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
brute force, TLE but maybe short enough
"""
import itertools


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        res_str = []
        nn = list(range(n))
        for i in itertools.permutations(nn):
            ip = set([x - i[x] for x in range(n)])
            im = set([x + i[x] for x in range(n)])
            if len(im) == len(ip) == n:
                res.append(i)

        for a in res:
            f = [["Q" if x == y else "." for x in a] for y in range(n - 1, -1, -1)]
            # print("\n".join(["".join(s_) for s_ in f]))
            res_str.append(["".join(line) for line in f])

        return len(res)
        return res_str


if __name__ == '__main__':
    s = Solution()
    data = [
        [1, 1],
        [2, 0],
        [4, 2],
        [5,10],
        [6,4],
        [7,40],
        # [8, 92],
        # [9, 352],
    ]
    for d in data:
        answer = s.solveNQueens(d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
