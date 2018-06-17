#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""
import re


class Solution:
    def check(self, substring):
        """
        :type substring: str
        :rtype: bool
        """
        sub_list = re.findall('.{%s}' % self.word_len, substring)
        sub_dict = self.gen_dict(sub_list)
        if sub_dict == self.word_dic:
            return True
        return False

    @staticmethod
    def gen_dict(word_list):
        """
        :type word_list: List[str
        :rtype: dict
        """
        # word_dic = dict()
        word_dic = dict.fromkeys(word_list, 0)
        # print(word_dic)
        for w in word_list:
            word_dic[w] += 1
        return word_dic

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        self.word_len = len(words[0])
        self.word_num = len(words)
        self.word_dic = self.gen_dict(words)
        res = []
        for i in range(len(s) - (self.word_len * self.word_num) + 1):
            if self.check(s[i:(self.word_len * self.word_num + i)]):
                res.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    data = [
        [("barfoothefoobarman", ["foo", "bar"]), [0, 9]],
        [("barthefoobarman", ["foo", "bar"]), [6]],
        [("barthefooman", ["foo", "bar"]), []],
        [("barthefooman", ["bar"]), [0]],
        [("barthefoomanbar", ["bar"]), [0, 12]],
        [("barthefoomanbar", []), []],
        [("", ["bar"]), []],
        [("barfoofoobarthefoobarman", ["bar", "foo", "the"]), [6, 9, 12]],
        [("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"]), [13]],
        [("lingmindraboofooowingdingbarrwingokokmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing", "okok"]),
         [13]]
    ]
    for d in data:
        answer = s.findSubstring(*d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
