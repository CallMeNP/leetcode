#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
bad solution: TLE
todo 尝试dp
"""


def char_match(s, p):
    return p == "?" or s == p


class Solution:
    def __init__(self):
        self.memo = {}

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.memo = {}
        return self.do_match(s, p)

    def do_match(self, s, p):
        if (s, p) in self.memo:
            return self.memo[(s, p)]
        if p == "":
            if s == "":
                self.memo[(s, p)] = True
                return True
            else:
                self.memo[(s, p)] = False
                return False
        if s == "":
            return set(p) == set("*")
        pp = p.replace("*", "")
        if len(pp) > len(s):
            self.memo[(s, p)] = False
            return False
        p_i = 0
        while p[p_i] == "*" and p_i + 1 < len(p) and p[p_i + 1] == "*":
            p_i += 1
        if p[p_i] == "*":
            for i in range(0, len(s) + 1):
                re = self.do_match(s[i:], p[p_i + 1:])
                if re:
                    self.memo[(s, p)] = True
                    return True
            self.memo[(s, p)] = False
            return False
        if char_match(s[0], p[0]):
            re = self.do_match(s[1:], p[1:])
            self.memo[(s, p)] = re
            return re

        self.memo[(s, p)] = False
        return False


if __name__ == "__main__":
    s = Solution()
    data = [
        [("a", "a"), True],
        [("a", "?"), True],
        [("a", "*a"), True],
        [("a", "*?"), True],
        [("a", "***a"), True],
        [("a", "***b"), False],
        [("aa", "***?*"), True],
        [("aa", "a"), False],
        [("aa", "*"), True],
        [("", "e"), False],
        [("", "*"), True],
        [("", ""), True],
        [("", "?*"), False],
        [("", "?***"), False],
        [("a", ""), False],
        [("aaabcaa", "a?*e"), False],
        [("aaabcaa", "a*?*e"), False],
        [("aaabcaa", "a*?*"), True],
        [("a", "a*?*"), False],
        [("ab", "a*?*"), True],
        [("abc", "a*?****"), True],
        [("abc", "?a*?****"), False],
        [("abbbbb", "a*?*"), True],
        [("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"), False],
        [("abbbbbbbaabbabaabaa", "*****a*ab"), False],
        [("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", "***bba**a*bbba**aab**b"), False],
        [("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb",
          "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"), False],
        [(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa*"),
            False],
        [(
            "aaabaaabbababaabbabaababbbbbbaabababbbaabaaaabbbbabbbbaaaaabaabbbbaaaabbabbaaabbabbbababbaaaabbabbabbbbabaabbabbbabbbbabbbbbaabbbababaaaababbbbababababababbabbbbaaaaababbaaababbabaababbbaaabbbbbababab",
            "aa*abab*a*a**a*b****ba*ba*aa*****b****b**bbbba*b*b*a**b**b*aab***b*bb***baa*b***a***baa*****a*a*a*ab**a"),
            False],
    ]
    for j in range(70):
        for i in data:
            r = s.isMatch(*i[0]) == i[1]
            if not r:
                print(i[0])
            else:
                print(True)
