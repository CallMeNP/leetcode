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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        li = head
        while l1 and l2:
            if l1.val <= l2.val:
                li.next = l1
                l1 = l1.next
            else:
                li.next = l2
                l2 = l2.next
            li = li.next
        if l1:
            li.next = l1
        elif l2:
            li.next = l2

        return head.next


if __name__ == "__main__":
    s = Solution()
    data = [
        [[1, 2], [2, 3], [1, 2, 2, 3]],
        [[1, 2], [3, 3], [1, 2, 3, 3]],
        [[1, 2], [3, 4], [1, 2, 3, 4]],
        [[1, 2], [3], [1, 2, 3]],
        [[1, 2], [], [1, 2]],
        [[], [], []],
        [[2, 3], [1, 2], [1, 2, 2, 3]],
        [[3, 3], [1, 2], [1, 2, 3, 3]],
        [[3, 4], [1, 2], [1, 2, 3, 4]],
        [[3], [1, 2], [1, 2, 3]],
        [[], [1, 2], [1, 2]],
    ]
    for d in data:
        nodes_a = list2nodes(d[0])
        nodes_b = list2nodes(d[1])
        answer = s.mergeTwoLists(nodes_a, nodes_b)
        list_answer = nodes2list(answer)
        if list_answer == d[2]:
            print(True)
        else:
            print(d, list_answer)
