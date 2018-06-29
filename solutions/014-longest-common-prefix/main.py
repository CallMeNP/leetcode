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
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        i = 0
        is_common = True
        while is_common:
            for str in strs:
                if i >= len(str):
                    is_common = False
                    break
                if str[i] != strs[0][i]:
                    is_common = False
                    break
            if not is_common:
                break
            i += 1
        return str[:i]


if __name__ == "__main__":
    s = Solution()
    data = [
        [["abc", "a", "ab"], "a"],
        [["abc", "abc", "abc"], "abc"],
        [["abc", "a", "ab", ""], ""],
        [["dog", "racecar", "car"], ""],
        [[], ""],
        [["", "", ""], ""],
    ]
    for d in data:
        answer = s.longestCommonPrefix(d[0])
        if answer != d[1]:
            print(d, answer)
        else:
            print(True)
