#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 np <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""


class Grid:
    def __init__(self, prob):
        """
        :param prob: set[int]
        """
        self.prob = prob  # type:set
        self.chosen_by_same_row = set()
        self.chosen_by_same_col = set()
        self.chosen_by_same_9grids = set()
        self.tested = set()
        self.chosen = "."

    def new_chosen(self):
        self.tested.add(self.chosen)
        if self.prob:
            self.chosen = self.prob.pop()
        else:
            self.chosen = "."
            print("Grid(%d,%d) has no more choice" % (self.x, self.y))
        return self.chosen

    def prob_count(self):
        if self.chosen == '.':
            return len(self.prob)
        return len(self.prob) + 1

    def __str__(self):
        return "(%d,%d),%s" % (self.x, self.y, str(self.prob))

    def __cmp__(self, other):
        """
        :param other: Grid
        :return:
        """
        return self.prob_count() - other.prob_count()

    def __lt__(self, other):
        return self.prob_count() < other.prob_count()

    def __gt__(self, other):
        return self.prob_count() > other.prob_count()


class Solution:
    def __init__(self):
        self.PROB_SET = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.board = []
        self.multi_prob_grids_dict = dict()  # type:{tuple:Grid}
        self.multi_prob_grids = []
        self.action_history = []

    def clear_prob_set_by_board(self):
        for g in self.multi_prob_grids_dict:
            s = self.multi_prob_grids_dict[g].prob  # type:set
            s -= self.get_9grid_set(*g)
            s -= self.get_col_set(g[0])
            s -= self.get_row_set(g[1])

    def get_row_set(self, y):
        if not 0 <= y < 9:
            raise Exception("bad y")
        s = set(self.board[y])
        if "." in s:
            s.remove(".")
        return s

    def get_col_set(self, x):
        if not 0 <= x < 9:
            raise Exception("bad x")
        s = set([self.board[i][x] for i in range(9)])
        if "." in s:
            s.remove(".")
        return s

    def get_9grid_set(self, x, y):
        if not 0 <= y < 9:
            raise Exception("bad y")
        if not 0 <= x < 9:
            raise Exception("bad x")
        x = x // 3 * 3
        y = y // 3 * 3
        s = set([self.board[y + dy][x + dx] for dx in range(3) for dy in range(3)])
        if "." in s:
            s.remove(".")
        return s

    def process_same_row(self, x, y, choice):
        for i in range(9):
            if i == x:
                continue
            g = self.multi_prob_grids_dict[(i, y)]  # type:Grid
            if choice in g.prob:
                g.prob.remove(choice)
                g.chosen_by_same_row.add(choice)

    def process_same_col(self, x, y, choice):
        for i in range(9):
            if i == y:
                continue
            g = self.multi_prob_grids_dict[(x, i)]  # type:Grid
            if choice in g.prob:
                g.prob.remove(choice)
                g.chosen_by_same_col.add(choice)

    def process_same_9grids(self, x, y, choice):
        if not 0 <= y < 9:
            raise Exception("bad y")
        if not 0 <= x < 9:
            raise Exception("bad x")
        x_ = x // 3 * 3
        y_ = y // 3 * 3
        for i in [(x_ + dx, y_ + dy) for dx in range(3) for dy in range(3)]:
            if i == (x, y):
                continue
            g = self.multi_prob_grids_dict[i]  # type:Grid
            if choice in g.prob:
                g.prob.remove(choice)
                g.chosen_by_same_9grids.add(choice)

    def revert_same_row(self, x, y, choice):
        for i in range(9):
            if i == x:
                continue
            g = self.multi_prob_grids_dict[(i, y)]  # type:Grid
            if choice in g.chosen_by_same_row:
                g.chosen_by_same_row.remove(choice)
                g.prob.add(choice)

    def revert_same_col(self, x, y, choice):
        for i in range(9):
            if i == y:
                continue
            g = self.multi_prob_grids_dict[(y, i)]  # type:Grid
            if choice in g.chosen_by_same_col:
                g.chosen_by_same_col.remove(choice)
                g.prob.add(choice)

    def revert_same_9grids(self, x, y, choice):
        if not 0 <= y < 9:
            raise Exception("bad y")
        if not 0 <= x < 9:
            raise Exception("bad x")
        x_ = x // 3 * 3
        y_ = y // 3 * 3
        for i in [(x_ + dx, y_ + dy) for dx in range(3) for dy in range(3)]:
            if i == (x, y):
                continue
            g = self.multi_prob_grids_dict[i]  # type:Grid
            if choice in g.chosen_by_same_9grids:
                g.chosen_by_same_9grids.remove(choice)
                g.prob.add(choice)

    def simple_elimination(self):
        """
        简单排除法
        :return:
        """
        grids = self.multi_prob_grids
        grids.sort()
        while grids and len(grids[0].prob) == 1:
            for i in grids:
                if len(i.prob) > 1:
                    break
                if len(i.prob) == 1:
                    self.board[i.y][i.x] = i.prob.pop()
            self.clear_prob_set_by_board()
            grids.sort()
            while grids and len(grids[0].prob) == 0:
                g = grids[0]
                del self.multi_prob_grids_dict[(g.x, g.y)]
                grids.pop(0)

    def try_it(self):
        grids = self.multi_prob_grids
        grids.sort()
        if grids and grids[0].prob_count() == grids[-1].prob_count() == 1:
            return True
        for g in grids:  # type:Grid
            if g.prob_count() == 0:
                if not self.action_history:
                    return False
                last_g = self.action_history.pop()
                self.revert_same_row(last_g.x, last_g.y, last_g.chosen)
                self.revert_same_col(last_g.x, last_g.y, last_g.chosen)
                self.revert_same_9grids(last_g.x, last_g.y, last_g.chosen)
            if g.prob_count() == 1:
                continue
            choice = g.new_chosen()
            if choice == ".":
                raise Exception("bad")
            self.process_same_row(g.x, g.y, choice)
            self.process_same_col(g.x, g.y, choice)
            self.process_same_9grids(g.x, g.y, choice)
            self.action_history.append(g, choice)
            break

    def solveSudoku(self, board):
        """
        :type board: list[list[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 清理
        self.board = board
        self.multi_prob_grids_dict = dict()  # type:{tuple:Grid}
        self.multi_prob_grids = []
        # 整理空grid的可能性
        # 建立list和坐标索引
        for x in range(9):
            for y in range(9):
                if board[y][x] == ".":
                    g = Grid(set(self.PROB_SET))
                    g.x = x
                    g.y = y
                    self.multi_prob_grids_dict[(x, y)] = g
                    self.multi_prob_grids.append(g)
        self.clear_prob_set_by_board()

        print(len(self.multi_prob_grids))
        self.simple_elimination()
        print(len(self.multi_prob_grids))
        print(len(self.multi_prob_grids_dict))
        if len(self.multi_prob_grids) == 0:
            return
        print(self.board)


if __name__ == '__main__':
    s = Solution()
    data = [
        [
            [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]], 0],
        [
            [['3', '.', '.', '2', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '1', '.', '7', '.', '.', '.'],
             ['7', '.', '6', '.', '3', '.', '5', '.', '.'],
             ['.', '7', '.', '.', '.', '9', '.', '8', '.'],
             ['9', '.', '.', '.', '2', '.', '.', '.', '4'],
             ['.', '1', '.', '8', '.', '.', '.', '5', '.'],
             ['.', '.', '9', '.', '4', '.', '3', '.', '1'],
             ['.', '.', '.', '7', '.', '2', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '8', '.', '.', '6']], 0],
    ]
    for d in data:
        answer = s.solveSudoku(d[0])
        if answer == d[1]:
            print(True)
        else:
            pass
            # print(d, answer)
