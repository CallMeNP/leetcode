#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""


class RegexFSM:
    __EMPTY = ''

    def __init__(self, pattern):
        self.transition_table = dict()
        self.accept = 0
        self.__build_nfa(pattern)
        self.state = {0}
        self.__extend_state_by_empty(0)

    def __add_transition(self, state, char, new_state):
        i = (state, char)
        if i not in self.transition_table:
            self.transition_table[i] = set()
        self.transition_table[i].add(new_state)

    def __build_nfa(self, pattern):
        state = 0
        for i in range(len(pattern)):
            if pattern[i] != "*":
                if i < len(pattern) - 1 and pattern[i + 1] == '*':
                    state_a = state + 1
                    state_b = state + 2
                    state_c = state + 3
                    self.__add_transition(state, self.__EMPTY, state_a)
                    self.__add_transition(state, self.__EMPTY, state_c)
                    self.__add_transition(state_a, pattern[i], state_b)
                    self.__add_transition(state_b, self.__EMPTY, state_a)
                    self.__add_transition(state_b, self.__EMPTY, state_c)
                    state = state_c
                else:
                    self.__add_transition(state, pattern[i], state + 1)
                    state += 1
        self.accept = state

    def print_trans_table(self):
        """
        将状态转移表，输出为plantuml(graphviz)的格式
        :return: None
        """
        for i in self.transition_table:
            for s in self.transition_table[i]:
                state = i[0]
                if state == 0:
                    state = '[*]'
                char = i[1]
                new_state = s
                if new_state == self.accept:
                    new_state = '[*]'
                print("%s -r-> %s : '%s'" % (state, new_state, char))

    def __extend_state_by_empty(self, state):
        for new_state in self.transition_table.get((state, self.__EMPTY), set()):
            if new_state not in self.state:
                self.state.add(new_state)
                self.__extend_state_by_empty(new_state)

    def input(self, char):
        new_state_set = set()
        for state in self.state:
            for c in [char, '.']:
                for new_state in self.transition_table.get((state, c), set()):
                    new_state_set.add(new_state)
        self.state = new_state_set
        for s in list(self.state):
            self.__extend_state_by_empty(s)

    def is_accepted(self):
        return self.accept in self.state


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        fsm = RegexFSM(p)
        for c in s:
            fsm.input(c)
        return fsm.is_accepted()


if __name__ == "__main__":
    s = Solution()
    data = [
        [("baaa", "ba*a"), True],
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
        # print("----")
        # print(i[0][1], prepare_p(i[0][1]))
        r = s.isMatch(*i[0]) == i[1]
        if not r:
            print(i, r)
        else:
            print(True)
