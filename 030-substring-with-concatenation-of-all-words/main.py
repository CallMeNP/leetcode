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
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        word_len = len(words[0])
        finded = []
        res = []
        for w_i in range(len(words)):
            finded.append([])
            i = -1
            while True:
                i = s.find(words[w_i], i + 1)
                if i == -1:
                    break
                finded[w_i].append(i)
        # 存在部分单词没找到
        if len(finded) < len(words):
            return []

        while True:
            finded.sort()
            this_round = True
            # 单词1位置列表为空
            if len(finded[0]) == 0:
                return res
            f_i = 1
            while f_i < len(finded):
                # 某单词的位置列表为空
                if len(finded[f_i]) == 0:
                    return res
                if finded[f_i][0] == finded[f_i - 1][0] + word_len:
                    f_i += 1
                    continue
                this_round = False
                for f_j in range(0, f_i):
                    del finded[f_j][0]
                break
            if this_round:
                res.append(finded[0][0])
                del finded[0][0]


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
        [("lingmindraboofooowingdingbarrwingokokmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing","okok"]), [13]]
    ]
    for d in data:
        answer = s.findSubstring(*d[0])
        if answer == d[1]:
            print(True)
        else:
            print(d, answer)
