#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""

import mod.dfs as dfs


class Solution(dfs.DFSTree):
    def __init__(self):
        super().__init__()

    def not_found(self):
        print("not found")


if __name__ == '__main__':
    s = Solution()
    s.depth_first_search()
