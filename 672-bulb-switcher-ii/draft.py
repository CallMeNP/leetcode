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
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        count = set()
        for a in range(m + 1):
            for b in range(a, m + 1):
                for c in range(b, m + 1):
                    w1 = a
                    w2 = b - a
                    w3 = c - b
                    w4 = m - c
                    #if w2 > w3:
                    #    w2 = w2 - w3
                    #    w3 = 0
                    #else:
                    #    w3 = w3 - w2
                    #    w2 = 0
                    w1%=2
                    w2%=2
                    w3%=2
                    w4%=2
                    count.add("{0}{1}{2}{3}".format(w1, w2, w3, w4));
        print(count)
        return len(count)
if __name__ == '__main__':
    s = Solution()
    print(s.flipLights(4, 1), 1)
    print(s.flipLights(4, 2), 2)
    print(s.flipLights(4, 3), 3)
    print(s.flipLights(5, 4), 4)
    print(s.flipLights(4, 5), 5)
    print(s.flipLights(4, 6), 6)
    print(s.flipLights(4, 7), 7)
    print(s.flipLights(4, 8), 8)
    print(s.flipLights2(1, 1))
    print(s.flipLights2(2, 1))
    print(s.flipLights2(2, 2))
    print(s.flipLights2(3, 1))
    print(s.flipLights2(3, 2))
    print(s.flipLights2(3, 3))
    print(s.flipLights2(4, 1))
    print(s.flipLights2(4, 2))
    print(s.flipLights2(4, 3))
    print(s.flipLights2(4, 4))
