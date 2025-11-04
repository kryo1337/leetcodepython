from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = 0
        while row < 9:
            d = dict()
            col = 0
            while col < 9:
                val = board[row][col]
                if val != '.':
                    if val in d:
                        return False
                    d[val] = True
                col += 1
            row += 1

        col = 0
        while col < 9:
            d = dict()
            row = 0
            while row < 9:
                val = board[row][col]
                if val != '.':
                    if val in d:
                        return False
                    d[val] = True
                row += 1
            col += 1

        boxrow = 0
        while boxrow < 9:
            boxcol = 0
            while boxcol < 9:
                d = dict()
                r = boxrow
                while r < boxrow + 3:
                    c = boxcol
                    while c < boxcol + 3:
                        val = board[r][c]
                        if val != '.':
                            if val in d:
                                return False
                            d[val] = True
                        c += 1
                    r += 1
                boxcol += 3
            boxrow += 3

        return True


def test_valid_board():
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert Solution().isValidSudoku(board) == True

def test_invalid_board():
    board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert Solution().isValidSudoku(board) == False

def test_duplicate_in_column():
    board = [
        [".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]
    ]
    assert Solution().isValidSudoku(board) == False

if __name__ == "__main__":
    test_valid_board()
    test_invalid_board()
    test_duplicate_in_column()
    print("All tests passed.")
