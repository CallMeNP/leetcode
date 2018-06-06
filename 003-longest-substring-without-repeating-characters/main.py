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
        count=[]
        for i in range(len(s)):
            count.append(1)
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    break
                count[i]+=1
        for i in range(len(count)-2,-1,-1):
            #print count[i],count[i+1]
            if count[i]>count[i+1]+1:
                count[i]=count[i+1]+1
        return max(count)

if __name__ == "__main__":
    s=Solution()
    print s.lengthOfLongestSubstring("abcabcbb")
    print s.lengthOfLongestSubstring("aaaa")
    print s.lengthOfLongestSubstring("pwwkew")
    print s.lengthOfLongestSubstring("p")
    print s.lengthOfLongestSubstring("jlygy")
