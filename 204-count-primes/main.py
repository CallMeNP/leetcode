#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
note: 切片赋值
"""

class Solution:
    def countPrimes(self, n):
        """
        >>> s=Solution()
        >>> s.countPrimes(10)
        4
        >>> s.countPrimes(100)
        25
        >>> s.countPrimes(999983)
        78497
        >>> s.countPrimes(999983)
        78497
        >>> s.countPrimes(999983)
        78497
        >>> s.countPrimes(999983)
        78497
        >>> s.countPrimes(999983)
        78497
        >>> s.countPrimes(999983)
        78497
        >>> s.countPrimes(999983)
        78497
        >>> s.countPrimes(999983)
        78497
        >>> s.countPrimes(999983)
        78497
        >>> s.countPrimes(999983)
        78497
        >>> s.countPrimes(999983)
        78497
        >>> s.countPrimes(999983)
        78497
        >>> s.countPrimes(999983)
        78497
        >>> s.countPrimes(999983)
        78497
        >>> s.countPrimes(999983)
        78497
        >>> s.countPrimes(999983)
        78497
        >>> s.countPrimes(999983)
        78497
        
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [False, False] + [True] * (n - 2)
        q = int((n - 1) ** 0.5)
        for i in range(2, q + 1):
            if primes[i]:
                # j = i
                # while i * j < n:
                #     primes[i * j] = False
                #     j += 1

                # i*i 是因为，如果一个数是i的倍数，但小于i*i，那一定也整除一个小于i的素数。也就是已经被小于i的数标记过了。
                primes[i * i:n:i] = [False] * len(primes[i * i:n:i])
        return sum(primes)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
