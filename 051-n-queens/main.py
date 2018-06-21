#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
brute force, TLE but maybe short enough
update: 经过简单优化，竟然 AC 了。。。
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
            # note: set(list) 比下面这种快
            # ip = set()
            # for x in range(n):
            #     ip.add(x - i[x])

            # note: 提前退出，比把两个集合都算出来快一半
            if len(ip) != n:
                continue
            im = set([x + i[x] for x in range(n)])
            # im = set()
            # for x in range(n):
            #     im.add(x + i[x])
            if len(im) != n:
                continue
            res.append(i)

        # for a in res:
        #     f = [["Q" if x == y else "." for x in a] for y in range(n - 1, -1, -1)]
        #     # print("\n".join(["".join(s_) for s_ in f]))
        #     res_str.append(["".join(line) for line in f])

        return len(res)
        return res_str


if __name__ == '__main__':
    s = Solution()
    data = [
        [1, 1],
        [2, 0],
        [4, 2],
        [5, 10],
        [6, 4],
        [7, 40],
        [8, 92],
        [9, 352],
    ]
    for d in data:
        answer = s.solveNQueens(d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
