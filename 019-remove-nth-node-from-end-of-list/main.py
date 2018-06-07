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


def nodes2list(head):
    """
    :type head: ListNode
    :rtype: list
    """
    l = []
    while head:
        l.append(head.val)
        head = head.next
    return l


def list2nodes(l):
    """
    :type l: list
    :rtype: ListNode
    """
    head = n = None
    for i in reversed(l):
        head = ListNode(i)
        head.next = n
        n = head
    return head


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head
        node = head
        nth_from_end = head
        n += 1
        while node:
            node = node.next
            if n == 0:
                nth_from_end = nth_from_end.next
            else:
                n -= 1
        # print(n)
        if n == 1:
            return head.next
        if n == 0:
            nth_from_end.next = nth_from_end.next.next
            return head
        if n > 1:
            return head


if __name__ == "__main__":
    s = Solution()
    data = [
        [[1, 2, 3, 4, 5], 2, [1, 2, 3, 5]],
        [[1, 2, 3, 4, 5], 1, [1, 2, 3, 4]],
        [[1, 2, 3, 4, 5], 5, [2, 3, 4, 5]],
        [[1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]],
        [[1], 1, []],
        [[], 0, []],
        [[], 10, []],
    ]
    for d in data:
        nodes = list2nodes(d[0])
        answer = s.removeNthFromEnd(nodes, d[1])
        list_answer = nodes2list(answer)
        if list_answer == d[2]:
            print(True)
        else:
            print(d, list_answer)
