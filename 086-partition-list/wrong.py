#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
理解成 [小于x，x，大于x] 的形式了。留存吧
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None  # type: ListNode


def build_list(l):
    # todo 此处不用guard有哪些实现？guard方便在哪？
    i = 0
    guard = a = ListNode(0)
    while True:
        if i >= len(l):
            break
        a.next = ListNode(l[i])
        i += 1
        a = a.next
    a.next = None
    return guard.next


def print_list(a):
    while a:
        print(a.val, end="")
        a = a.next
    print("\n", end="")


class Solution:
    """
    >>> s=Solution()
    >>> l=build_list([1,4,3,2,5,2])
    >>> a=s.partition(l,3)
    >>> print_list(a)
    122345
    >>> l=build_list([3])
    >>> a=s.partition(l,3)
    >>> print_list(a)
    3
    >>> l=build_list([])
    >>> a=s.partition(l,3)
    >>> print_list(a)
    <BLANKLINE>
    """

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        guard = pre_check = pre_x = ListNode("x")
        pre_check.next = pre_x.next = head
        node_x = head
        while node_x and node_x.val != x:
            node_x = node_x.next
        if not node_x:
            return guard.next
        check = head
        while check:
            if check.val == x:
                break
            if check.val > x:
                pre_check.next = check.next
                check.next = node_x.next
                node_x.next = check
                check = pre_check.next
            else:
                pre_x = check
                pre_check = check
                check = check.next
        pre_check = node_x
        check = pre_check.next
        while check:
            if check.val < x:
                pre_check.next = check.next
                check.next = pre_x.next
                pre_x.next = check
                check = pre_check.next
            else:
                pre_check = check
                check = check.next
        return guard.next


if __name__ == '__main__':
    import doctest

    doctest.testmod()
