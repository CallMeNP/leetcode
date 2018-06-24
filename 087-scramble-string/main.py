#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""


class Solution:
    def isScramble(self, s1, s2):
        """
        >>> s=Solution()
        >>> s.isScramble("great","rgeat")
        True
        >>> s.isScramble("great","rgtae")
        True
        >>> s.isScramble("abcde","caebd")
        False
        >>> s.isScramble("abcdefghijklmnopq","efghijklmnopqcadb")
        False
        >>> s.isScramble("aaabbeeee","bbbaaeeee")
        False

        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l = len(s1)
        if s1 == s2:
            return True
        if l <= 1 and s1 != s2:
            return False
        # 集合比较可以放到头部，对 s1,s2 做 sorted() 之后的比较
        # leetcode-cn上有提交用sorted()这么实现。更快一些
        for i in range(l - 1):
            s1_left = s1[:i + 1]
            s1_right = s1[i + 1:]
            s1_left_set = set(s1_left)
            s1_right_set = set(s1_right)
            s2_left = s2[:i + 1]
            s2_right = s2[i + 1:]
            s2_left_set = set(s2_left)
            s2_right_set = set(s2_right)
            # print(s1_left_set, s1_right_set, s2_left_set, s2_right_set)
            if s1_left_set == s2_left_set and s1_right_set == s2_right_set:
                if self.isScramble(s1_left, s2_left) and self.isScramble(s1_right, s2_right):
                    return True
            s2_left = s2[:l - 2 - i + 1]
            s2_right = s2[l - 2 - i + 1:]
            s2_left_set = set(s2_left)
            s2_right_set = set(s2_right)
            if s1_left_set == s2_right_set and s1_right_set == s2_left_set:
                if self.isScramble(s1_left, s2_right) and self.isScramble(s1_right, s2_left):
                    return True
        return False


if __name__ == '__main__':
    import doctest

    doctest.testmod()
