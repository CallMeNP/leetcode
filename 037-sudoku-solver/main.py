#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 np <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

from mod.dfs import DFSTree


class Grid:
    def __init__(self, prob):
        """
        :param prob: set
        """
        self.prob = prob
        self.chosen_by_same_row = set()
        self.chosen_by_same_col = set()
        self.chosen_by_same_9grids = set()
        self.tested = set()
        self.chosen = None

    def new_chosen(self):
        if self.chosen:
            self.tested.add(self.chosen)
        if self.has_more_prob():
            self.chosen = self.prob.pop()
            return self.chosen
        raise Exception("no more choice")

    def clear_tested(self):
        if self.chosen:
            self.prob.add(self.chosen)
            self.chosen = None
        self.prob |= self.tested
        self.tested.clear()

    def has_more_prob(self):
        return len(self.prob) > 0

    def prob_count(self):
        if not self.chosen:
            return len(self.prob)
        return len(self.prob) + 1

    def __str__(self):
        return "(%d,%d),%s,%s" % (self.x, self.y, self.chosen, str(self.prob))

    def __cmp__(self, other):
        return self.prob_count() - other.prob_count()

    def __lt__(self, other):
        return self.prob_count() < other.prob_count()

    def __gt__(self, other):
        return self.prob_count() > other.prob_count()


class Solution(DFSTree):
    def __init__(self):
        DFSTree.__init__(self)
        self.PROB_SET = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.board = []
        # 通过坐标将不确定的格子索引起来
        self.multi_prob_grids_dict = dict()  # type:{tuple:Grid}
        # 将不确定的格子放在 list 里，方便排序
        self.multi_prob_grids = []
        # 做出选择的格子组成的栈，用于回溯选择
        self.action_history = []

    def is_target(self):
        if self.multi_prob_grids:
            self.multi_prob_grids.sort()
            if self.multi_prob_grids[0].prob_count() != 1:
                return False
            if self.multi_prob_grids[-1].prob_count() != 1:
                return False
        # todo 通过已填入的数验证
        return True

    def found(self):
        for g in self.action_history:
            self.board[g.y][g.x] = g.chosen
        for g in self.multi_prob_grids:
            self.board[g.y][g.x] = g.prob.pop()
            # print(self.board)

    def go_on(self):
        return False

    def has_children(self):
        # 已经找到解，无子状态
        if self.is_target():
            return False
        # 没有更多待选格子，无子状态
        if not self.multi_prob_grids:
            return False
        # 存在待选格子没有可选项，说明发生了矛盾，无子状态
        self.multi_prob_grids.sort()
        if self.multi_prob_grids[0].prob_count() == 0:
            return False
        return True

    def visit_first_child(self):
        self.multi_prob_grids.sort()
        g = self.multi_prob_grids.pop(0)
        g.new_chosen()
        self.action_history.append(g)
        self.process_same_row_col_9grids(g)

    def has_next_sibling(self):
        # 没有已作出选择的格子了，回溯到尽头了
        if not self.action_history:
            return False
        # 最后一个已做选择的格子，还有其他选项
        g = self.action_history[-1]  # type: Grid
        return g.has_more_prob()

    def visit_next_sibling(self):
        g = self.action_history[-1]
        self.revert_same_row_col_9grids(g)
        g.new_chosen()
        self.process_same_row_col_9grids(g)

    def has_parent(self):
        return bool(self.action_history)

    def back_to_parent(self):
        g = self.action_history.pop()  # type: Grid
        self.revert_same_row_col_9grids(g)
        g.clear_tested()
        self.multi_prob_grids.append(g)

    def clear_prob_set_by_board(self):
        for g in self.multi_prob_grids:
            g.prob -= set([row[g.x] for row in self.board])
            g.prob -= set(self.board[g.y])
            x = g.x // 3 * 3
            y = g.y // 3 * 3
            g.prob -= set([self.board[y + dy][x + dx] for dx in range(3) for dy in range(3)])

    def process_same_row_col_9grids(self, grid):
        x = grid.x
        y = grid.y
        choice = grid.chosen
        # same row
        for i in range(9):
            if i == x:
                continue
            if (i, y) not in self.multi_prob_grids_dict:
                continue
            g = self.multi_prob_grids_dict[(i, y)]  # type:Grid
            if choice in g.prob:
                g.prob.remove(choice)
                g.chosen_by_same_row.add(choice)
        # same col
        for i in range(9):
            if i == y:
                continue
            if (x, i) not in self.multi_prob_grids_dict:
                continue
            g = self.multi_prob_grids_dict[(x, i)]  # type:Grid
            if choice in g.prob:
                g.prob.remove(choice)
                g.chosen_by_same_col.add(choice)
        # same 9 grids
        if not 0 <= y < 9:
            raise Exception("bad y")
        if not 0 <= x < 9:
            raise Exception("bad x")
        x_ = x // 3 * 3
        y_ = y // 3 * 3
        for i in [(x_ + dx, y_ + dy) for dx in range(3) for dy in range(3)]:
            if i == (x, y):
                continue
            if i not in self.multi_prob_grids_dict:
                continue
            g = self.multi_prob_grids_dict[i]  # type:Grid
            if choice in g.prob:
                g.prob.remove(choice)
                g.chosen_by_same_9grids.add(choice)

    def revert_same_row_col_9grids(self, grid):
        x = grid.x
        y = grid.y
        choice = grid.chosen
        # same row; x 变，y不变
        for i in range(9):
            if i == x:
                continue
            if (i, y) not in self.multi_prob_grids_dict:
                continue
            g = self.multi_prob_grids_dict[(i, y)]  # type:Grid
            if choice in g.chosen_by_same_row:
                g.chosen_by_same_row.remove(choice)
                g.prob.add(choice)
        # same col; x 不变; y 变
        for i in range(9):
            if i == y:
                continue
            if (x, i) not in self.multi_prob_grids_dict:
                continue
            g = self.multi_prob_grids_dict[(x, i)]  # type:Grid
            if choice in g.chosen_by_same_col:
                g.chosen_by_same_col.remove(choice)
                g.prob.add(choice)
        # same 9 grids
        if not 0 <= y < 9:
            raise Exception("bad y")
        if not 0 <= x < 9:
            raise Exception("bad x")
        x_ = x // 3 * 3
        y_ = y // 3 * 3
        for i in [(x_ + dx, y_ + dy) for dx in range(3) for dy in range(3)]:
            if i == (x, y):
                continue
            if i not in self.multi_prob_grids_dict:
                continue
            g = self.multi_prob_grids_dict[i]  # type:Grid
            if choice in g.chosen_by_same_9grids:
                g.chosen_by_same_9grids.remove(choice)
                g.prob.add(choice)

    def simple_elimination(self):
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

    def solveSudoku(self, board):
        """
        :type board: list[list[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 清理
        self.__init__()
        self.board = board
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

        # print(len(self.multi_prob_grids))
        self.simple_elimination()
        # print(len(self.multi_prob_grids))
        if len(self.multi_prob_grids) == 0:
            # print(self.board)
            return
        self.visit_first_child()
        self.depth_first_search()


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
    import re

    pe_data_file = open('./p096_sudoku.txt', "r")
    pe_data_lines = pe_data_file.readlines()
    sudokus = []
    for i in range(50):
        sudokus.append([])
        for j in range(1, 10):
            sudokus[-1].append(re.findall(".", pe_data_lines[i * 10 + j].replace("0", ".")))
    sum = 0
    for sudoku in sudokus:
        s.solveSudoku(sudoku)
        sum += int("".join(s.board[0][0:3]))
    print(sum)
