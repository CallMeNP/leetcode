#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Hailong Gao <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""
"""


class DFSTree:
    def is_target(self):
        return False

    def found(self):
        pass

    def not_found(self):
        pass

    def has_children(self):
        return False

    def has_parent(self):
        return False

    def has_next_sibling(self):
        return False

    def visit_first_child(self):
        pass

    def visit_next_sibling(self):
        pass

    def back_to_parent(self):
        pass

    def depth_first_search(self):
        while True:
            if self.is_target():
                self.found()
                return True
            if self.has_children():
                self.visit_first_child()
            elif self.has_next_sibling():
                self.visit_next_sibling()
            else:
                while not self.has_next_sibling():
                    if not self.has_parent():
                        self.not_found()
                        return False
                    self.back_to_parent()
                self.visit_next_sibling()
