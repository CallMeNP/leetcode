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
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        guard = ListNode("x")
        guard.next = head
        pre = guard
        a = pre.next
        while a:
            if a.next and a.next.val == a.val:
                while a.next and a.next.val == a.val:
                    a = a.next
                sub = a.next
                pre.next = sub
                a = sub
            else:
                pre = pre.next
                a = a.next
        return guard.next
