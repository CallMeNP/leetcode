#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""
from random import randint


def quick_sort(arr, low, high):
    """
    >>> a=[3,1,4,1,5,9,2,6]
    >>> quick_sort(a,0,len(a)-1)
    >>> print(a)
    [1, 1, 2, 3, 4, 5, 6, 9]
    >>> a=[3,1,4,1,5,9,2]
    >>> quick_sort(a,0,len(a)-1)
    >>> print(a)
    [1, 1, 2, 3, 4, 5, 9]

    :type arr: list[int]
    :type low: int [
    :type high: int ]
    :rtype: list
    """
    if low < high:
        i = randomized_partition(arr, low, high)
        quick_sort(arr, low, i - 1)
        quick_sort(arr, i + 1, high)
    # return arr


def randomized_partition(arr, low, high):
    """
    randomized_partition()
    概念：
    判别元素，指针元素
    边界情况：
    - 为什么用最后一个位置做判别元素
    - 如果没发生交换，指针所在元素会不会不对
    - 指针移动到最后一个元素的情况
    :type arr: list[int]
    :type low: int [
    :type high: int ]
    :rtype: int
    """
    # 随机取一下标
    i = randint(low, high)
    # 交换此下标元素到最后；以最后一个元素为判别元素
    arr[i], arr[high] = arr[high], arr[i]
    # 指针指向第一个元素；将保持指针左侧都小于判别元素，指针和指针右侧都大于判别元素。
    i = low
    # 遍历第一到倒数第二个元素
    for j in range(low, high):
        # 如果当前元素小于判别元素
        if arr[j] < arr[high]:
            # 交换当前元素和指针
            arr[i], arr[j] = arr[j], arr[i]
            # 指针移动
            i += 1
    # 交换指针和判别元素
    arr[i], arr[high] = arr[high], arr[i]
    # 指针所在位置即判别元素
    return i


if __name__ == '__main__':
    # import doctest
    import itertools

    # doctest.testmod()

    for l in range(9):
        arr = [i for i in range(l)]
        for a in itertools.permutations(arr):
            a = list(a)
            b = sorted(a)
            quick_sort(a, 0, len(a) - 1)
            assert b == a
