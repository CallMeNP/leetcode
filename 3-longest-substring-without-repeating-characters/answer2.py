#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 np <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        i=0
        j=1
        char_set=set()
        char_set.add(s[0])
        while i<len(s) and j<len(s):
            if s[i]==s[j]:
                char_set.remove(s[j])
                i=j
                j+=1
            else:
                char_set.add(s[j])
                j+=1
        return len(char_set)

if __name__ == "__main__":
    s=Solution()
    print s.lengthOfLongestSubstring("abcabcbb")
    print s.lengthOfLongestSubstring("aaaa")
    print s.lengthOfLongestSubstring("pwwkew")
    print s.lengthOfLongestSubstring("p")
    print s.lengthOfLongestSubstring("jlygy")
