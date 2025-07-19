from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(row, col):
            return not (cols[col] or pos_diag[row + col] or neg_diag[row - col])

        def place_queen(row):
            if row == n:
                board = ["".join(r) for r in chessboard]
                result.append(board)
                return

            for col in range(n):
                if is_safe(row, col):
                    chessboard[row][col] = 'Q'
                    cols[col] = pos_diag[row + col] = neg_diag[row - col] = True

                    place_queen(row + 1)

                    # backtrack
                    chessboard[row][col] = '.'
                    cols[col] = pos_diag[row + col] = neg_diag[row - col] = False

        result = []
        chessboard = [['.' for _ in range(n)] for _ in range(n)]
        cols = [False] * n
        pos_diag = [False] * (2 * n - 1)
        neg_diag = [False] * (2 * n - 1)

        place_queen(0)
        return result
