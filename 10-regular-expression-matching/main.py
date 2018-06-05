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


def find_next_non_star_pattern_char_index(p, p_i):
    while p_i < len(p) and p[p_i] == '*':
        p_i += 1
    return p_i


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p_i = 0
        # 找到第一个非*模式字符
        p_i = find_next_non_star_pattern_char_index(p, p_i)

        s_i = 0
        result = True
        if len(p) == 0:
            return len(s) == 0
        if len(s) == 0:
            return p_i == len(p)
        while p_i < len(p) or s_i < len(s):
            if p_i>=len(p):
                return False
            if p[p_i] == '*':
                recursion_result = False
                next_non_start_index = find_next_non_star_pattern_char_index(p, p_i)
                # print("next_non_start_index:", next_non_start_index)
                while s_i <= len(s):
                    recursion_result |= self.isMatch(s[s_i:], p[next_non_start_index:])
                    if recursion_result:
                        # print("break at recursion_result; s_i:", s_i)
                        break
                    if s_i < len(s) and not char_match(s[s_i], p[p_i - 1]):
                        # print("break at not match *; s_i:", s_i)
                        break
                    s_i += 1
                return recursion_result
            # print(s, p, s_i, p_i)
            if s_i >= len(s):
                return False
            if result and char_match(s[s_i], p[p_i]):
                s_i += 1
                p_i += 1
                continue
            else:
                return False
        return result


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
        [("a", ""), False],
        [("aaabcaa", "a.*e"), False],
        [("aaabcaa", "a*.*e"), False],
        [("aaabcaa", "a*.*"), True],
        [("a", "a*.*"), False],
        [("ab", "a*.*"), True],
        [("abc", "a*.****"), True],
        [("abc", ".a*.****"), False],
        [("abbbbb", "a*.*"), True],
    ]
    for i in data:
        r=s.isMatch(*i[0]) == i[1]
        if not r:
            print(i[0])
