#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""


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
        return self.do_match(s, prepare_p(p))

    def do_match(self, s, p):
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
                    return self.isMatch(s, p[p_i + 2:])
                return False

        if p_i < len_p - 1:
            if p[p_i + 1] == '*':
                re_result = False
                s_ii = s_i
                while s_ii <= len_s:
                    re_result |= self.do_match(s[s_ii:], p[p_i + 2:])
                    if re_result:
                        break
                    if s_ii < len_s and not char_match(s[s_ii], p[p_i]):
                        break
                    s_ii += 1
                    # return self.do_match(s, p[p_i] + p) or )
                return re_result
        return char_match(s[s_i], p[p_i]) and self.do_match(s[s_i + 1:], p[p_i + 1:])


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
