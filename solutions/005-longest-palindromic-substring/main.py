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
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_j=0
        i_when_max_j=0
        max_k=-1
        i_when_max_k=0
        for i in range(len(s)):
            j=0
            while i-j>=0 and i+j<len(s):
                if s[i-j]==s[i+j]:
                    j+=1
                    continue
                break
            j-=1
            if j>max_j:
                max_j=j
                i_when_max_j=i
            k=0
            while i-k>=0 and i+k+1<len(s):
                if s[i-k]==s[i+k+1]:
                    k+=1
                    continue
                break
            k-=1
            if k>max_k:
                max_k=k
                i_when_max_k=i
        if max_j>max_k:
            return s[(i_when_max_j-max_j):(i_when_max_j+max_j+1)]
        else:
            return s[(i_when_max_k-max_k):(i_when_max_k+max_k+2)]
