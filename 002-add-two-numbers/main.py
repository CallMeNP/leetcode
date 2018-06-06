#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
        print a.val,
        a = a.next
    print "\n",


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = lr = ListNode(0)
        while True:
            lr.val += l1.val + l2.val
            tmp = lr.val / 10
            lr.val = lr.val % 10
            if l1.next is None or l2.next is None:
                break
            lr.next = ListNode(tmp)
            l1 = l1.next
            l2 = l2.next
            lr = lr.next
        l = l1 if l1.next else l2
        while True:
            if l.next is None:
                break
            lr.next = ListNode(tmp)
            l = l.next
            lr = lr.next
            lr.val += l.val
            tmp = lr.val / 10
            lr.val = lr.val % 10
        if tmp:
            lr.next = ListNode(1)
        return start


if __name__ == '__main__':
    s = Solution()
    la = build_list([1, 1, 1])
    lb = build_list([2, 2, 9, 3])
    result = s.addTwoNumbers(la, lb)
    print_list(la)
    print_list(lb)
    print_list(result)
