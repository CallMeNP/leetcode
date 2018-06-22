#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
tags: 康托展开
## 康托展开
n=4
已知一个n元素的排列p，求p的序号：f(p)->int
f(p)=
(4-1)!, (3-1)!, (2-1)!, (1-1)!
l(p[0]) l(p[1]) l(p[2]) l(p[3])

l(x)是求p中，在x右侧，比x小的元素的个数

## 逆展开
已知一个序号x，求其排列p
元素数为n=4
x/((4-1)!) 为 a 说明 l(p[0])==a
用n个元素组成的集合，减去p[i]左边已经出现过的元素组成的集合，得到所有可能出现在p[i]右侧的元素集合
将此集合排序为列表，取第a个元素即可

令x等于x % ((4-1)!)，继续迭代

"""
from math import factorial


def calculate_cantor_num(p):
    """
    >>> calculate_cantor_num([1,2,3])
    0
    >>> calculate_cantor_num([1,3,2])
    1
    >>> calculate_cantor_num([2,1,3])
    2
    >>> calculate_cantor_num([3,2,1])
    5
    >>> calculate_cantor_num([2,1,0])
    5
    >>> calculate_cantor_num([])
    0
    >>> calculate_cantor_num([1])
    0
    
    :param p: list[int]
    :return: int
    """

    def find_less_in_right_side(p, i):
        count = 0
        j = i + 1
        while j < len(p):
            if p[j] < p[i]:
                count += 1
            j += 1
        return count

    len_p = len(p)
    f = [factorial(i) for i in range(len_p)]
    f.reverse()
    for i in range(len_p):
        f[i] *= find_less_in_right_side(p, i)
    return sum(f)


def get_permutation_from_cantor_num(n, x):
    """
    >>> get_permutation_from_cantor_num(3,1)
    [1, 3, 2]
    >>> get_permutation_from_cantor_num(3,0)
    [1, 2, 3]
    >>> get_permutation_from_cantor_num(3,2)
    [2, 1, 3]
    >>> get_permutation_from_cantor_num(3,5)
    [3, 2, 1]
    
    :param n: int 元素个数
    :param x: int 康托序数
    :return: list[int]
    """
    elements = set(range(1, n + 1))

    f = [factorial(i) for i in range(n)]
    f.reverse()
    for i in range(n):
        a = x // f[i]
        x %= f[i]
        f[i] = sorted(list(elements))[a]
        elements.remove(f[i])
    return f


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        f = get_permutation_from_cantor_num(n, k)
        return "".join([str(i) for i in f])


if __name__ == '__main__':
    import doctest

    doctest.testmod()
