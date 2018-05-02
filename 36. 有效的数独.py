INDEX = {
    0: {0: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 3, 7: 3, 8: 3},
    1: {0: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 3, 7: 3, 8: 3},
    2: {0: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 3, 7: 3, 8: 3},
    3: {0: 4, 1: 4, 2: 4, 3: 5, 4: 5, 5: 5, 6: 6, 7: 6, 8: 6},
    4: {0: 4, 1: 4, 2: 4, 3: 5, 4: 5, 5: 5, 6: 6, 7: 6, 8: 6},
    5: {0: 4, 1: 4, 2: 4, 3: 5, 4: 5, 5: 5, 6: 6, 7: 6, 8: 6},
    6: {0: 7, 1: 7, 2: 7, 3: 8, 4: 8, 5: 8, 6: 9, 7: 9, 8: 9},
    7: {0: 7, 1: 7, 2: 7, 3: 8, 4: 8, 5: 8, 6: 9, 7: 9, 8: 9},
    8: {0: 7, 1: 7, 2: 7, 3: 8, 4: 8, 5: 8, 6: 9, 7: 9, 8: 9},
}


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        left = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set()}
        left_row = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
        left_line = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}

        for _row_num, row in enumerate(board):
            for _line_num, _num in enumerate(row):
                if _num != '.':
                    if _num in left_row[_row_num] or _num in left_line[_line_num] or _num in left[
                        INDEX[_row_num][_line_num]]:
                        return False
                    else:
                        left_row[_row_num].add(_num)
                        left_line[_line_num].add(_num)
                        left[INDEX[_row_num][_line_num]].add(_num)
        return True
