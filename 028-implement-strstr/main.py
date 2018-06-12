#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""


def compute_prefix(s):
    """
    :type s: str
    :rtype: list
    """
    if not s:
        return []
    # 第一个字符的最长前缀直接写为-1
    next_arr = [-1]
    # prefix_i为已经匹配为前缀的字符
    # 省的检测到不匹配的情况再退回
    prefix_i = -1
    # 一次遍历模式串
    for suffix_i in range(1, len(s)):
        # prefix_i=-1的情况，如果不匹配，就表示与第一个字符不匹配，直接进行下一个suffix_i
        # 已经发生匹配，不匹配则检验已匹配部分的可能前缀
        while prefix_i > -1 and s[suffix_i] != s[prefix_i + 1]:
            prefix_i = next_arr[prefix_i]
        if s[suffix_i] == s[prefix_i + 1]:
            prefix_i += 1
        next_arr.append(prefix_i)
    return next_arr


def kmp(s, p):
    """
    :type s: str
    :type p: str
    :rtype: int
    """
    if not p:
        return 0
    next_arr = compute_prefix(p)
    # 模式字符串指针
    # 保持指向已经匹配成功的最后一个字符
    # 省的检测到不匹配的情况再退回
    p_i = -1
    len_p = len(p)
    # 一次遍历字符串
    for s_i in range(len(s)):
        # 如果模式字符串中，已经匹配的字符的下一个字符，不匹配：就找一个模式字符串的可能前缀
        # 此处限定p_i>-1，即模式字符串已经开始有匹配字符。如果没有匹配字符的情况，就继续下一个s_i
        while s[s_i] != p[p_i + 1] and p_i > -1:
            p_i = next_arr[p_i]
        if s[s_i] == p[p_i + 1]:
            p_i += 1
        if p_i == len_p - 1:
            break
        # 如果找到第一个匹配后，继续寻找，则：p_i=next_arr[p_i]
    if p_i < len_p - 1:
        return -1
    return s_i - p_i


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return kmp(haystack, needle)


if __name__ == '__main__':
    s = Solution()
    data = [
        ["abc", "-"],
        ["abc", "a"],
        ["abc", "b"],
        ["abc", "c"],
        ["abc", "abc"],
        ["abc", "ab"],
        ["abc", "bc"],
        ["bacbababadababacambabacaddababacasdsd", "ababaca"],
        ["mississippi", "issip"],
        ["aaaabaaaabaaaabaaaab", "aaaaa"],
        ["aabaaabaaac", "aabaaac"],
    ]
    for d in data:
        answer = s.strStr(d[0], d[1])
        if answer == d[0].find(d[1]):
            print(True)
        else:
            print(d, d[0].find(d[1]), answer, cal_next(d[1]))
