#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
note: sorted(str) 返回的是 list
note: 没有 str.sort() 方法
note: dict.values() 返回的不是 list。是 <class 'dict_value'>
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        word_dic = dict()
        for s in strs:
            ss = str(sorted(s))
            if ss not in word_dic:
                word_dic[ss] = []
            word_dic[ss].append(s)
        return [word_dic[i] for i in word_dic]
