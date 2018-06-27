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
    def lengthOfLongestSubstring(self, s):
        """
        >>> s=Solution()
        >>> s.lengthOfLongestSubstring("tmmzuxt")
        5
        >>> s.lengthOfLongestSubstring("abba")
        2
        >>> s.lengthOfLongestSubstring("")
        0
        >>> s.lengthOfLongestSubstring("a")
        1
        >>> s.lengthOfLongestSubstring("aba")
        2
        >>> s.lengthOfLongestSubstring("jlygy")
        4
        
        :type s: str
        :rtype: int
        """
        dic = dict()
        j = i = 0
        res = 0
        while j < len(s):
            if s[j] in dic:
                # 需要max，为了规避 "tmmzuxt" 中t的情况
                i = max(dic[s[j]] + 1, i)
            res = max(j - i + 1, res)
            dic[s[j]] = j
            j += 1
        return res


if __name__ == '__main__':
    import doctest

    doctest.testmod()
