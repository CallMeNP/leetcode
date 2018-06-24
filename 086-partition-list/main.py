#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
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
    122435
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
        last_of_smaller = guard = ListNode('x')
        last_of_smaller.next=head
        last_of_bigger = bigger_guard = ListNode('x')
        checker = head
        while checker:
            if checker.val >= x:
                last_of_smaller.next = checker.next
                last_of_bigger.next = checker
                checker.next = None
                last_of_bigger = last_of_bigger.next
                checker = last_of_smaller.next
            else:
                last_of_smaller = last_of_smaller.next
                checker = checker.next
        last_of_smaller.next=bigger_guard.next

        return guard.next


if __name__ == '__main__':
    import doctest

    doctest.testmod()
