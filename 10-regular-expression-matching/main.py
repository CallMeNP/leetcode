#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""

# todo dp有待尝试
def char_match(c, pc):
    if pc == ".":
        return True
    if c == pc:
        return True
    return False


def prepare_p(p):
    i = 0
    while i < len(p) - 1:
        if p[i] == p[i + 1] == "*":
            p = p[:i] + p[i + 1:]
            continue
        i += 1
    if len(p) > 0 and p[0] == "*":
        p = p[1:]
    return p


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.memo = {}
        return self.do_match(s, prepare_p(p))

    def do_match(self, s, p):
        if (s, p) in self.memo.keys():
            return self.memo[(s, p)]
        # print(s, p)
        p_i = 0

        s_i = 0
        len_p = len(p)
        len_s = len(s)
        # 模式串已空，看字符串空不
        if len_p == p_i:
            return len_s == 0
        # 字符串已空，看模式串空不
        if len_s == 0:
            if len_p - p_i == 1:
                return False
            if len_p - p_i == 0:
                return True
            if len_p - p_i >= 2:
                if p[p_i + 1] == '*':
                    return self.do_match(s, p[p_i + 2:])
                return False

        if p_i < len_p - 1:
            if p[p_i + 1] == '*':
                re = self.do_match(s, p[p_i] + p) or self.do_match(s, p[p_i + 2:])
                self.memo[(s, p)] = re
                return re
        re = char_match(s[s_i], p[p_i]) and self.do_match(s[s_i + 1:], p[p_i + 1:])
        self.memo[(s, p)] = re
        return re


if __name__ == "__main__":
    s = Solution()
    data = [
        [("a", "a"), True],
        [("a", "."), True],
        [("a", "*a"), True],
        [("a", "*."), True],
        [("a", "***a"), True],
        [("a", "***b"), False],
        [("aa", "***.*"), True],
        [("aa", "a"), False],
        [("", "e"), False],
        [("", "*"), True],
        [("", ""), True],
        [("", ".*"), True],
        [("", ".***"), True],
        [("a", ""), False],
        [("aaabcaa", "a.*e"), False],
        [("aaabcaa", "a*.*e"), False],
        [("aaabcaa", "a*.*"), True],
        [("a", "a*.*"), True],
        [("ab", "a*.*"), True],
        [("abc", "a*.****"), True],
        [("abc", ".a*.****"), True],
        [("abbbbb", "a*.*"), True],
        [("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"), False],
    ]
    for i in data:
        print("----")
        print(i[0][1], prepare_p(i[0][1]))
        r = s.isMatch(*i[0]) == i[1]
        if not r:
            print(i[0])
