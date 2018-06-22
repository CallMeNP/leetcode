#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
note: 看清是右转还是左转 囧
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        # k==0 也直接返回
        if not head or not k:
            return head

        count = 1
        point = head
        while point.next:
            count += 1
            point = point.next
        point.next = head
        k %= count
        k = count - k
        while k:
            point = point.next
            k -= 1
        res = point.next
        point.next = None
        return res

        return head
