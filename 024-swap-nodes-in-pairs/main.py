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
    def reverse_k(self, head, k):
        """
        :param head: ListNode
        :param k: int
        :return: ListNode
        """
        pass

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pass


if __name__ == "__main__":
    s = Solution()
    data = [
        [[1, 2, 3, 4, 5], [2, 1, 4, 3, 5]],
        [[1, 2, 3, 4], [2, 1, 4, 3]],
        [[1, 2, 4], [2, 1, 4]],
        [[1, 2], [2, 1]],
        [[1], [1]],
        [[], []],
    ]
    for d in data:
        nodes = list2nodes(d[0])
        answer = s.swapPairs(nodes)
        list_answer = nodes2list(answer)
        if list_answer == d[1]:
            print(True)
        else:
            print(d, list_answer)
