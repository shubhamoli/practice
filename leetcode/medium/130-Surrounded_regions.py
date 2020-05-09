"""
    Leetcode #134
"""


from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m = len(board)
        n = len(board[0])

        def markBorder(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] in ('X', '#'):
                return

            board[i][j] = '#'
            markBorder(i-1, j)
            markBorder(i+1, j)
            markBorder(i, j-1)
            markBorder(i, j+1)

        # mark 'O's which are connected to borders
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    if board[i][j] == 'O':
                        markBorder(i, j)


        # since border 'O' are marked we can change reamining Os
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                # restore border Os
                if board[i][j] == '#':
                    board[i][j] = 'O'


if __name__ == "__main__":

    board = [
                ['X', 'X', 'X', 'X'],
                ['X', 'O', 'O', 'X'],
                ['X', 'X', 'O', 'X'],
                ['X', 'O', 'X', 'X'],
            ]

    Solution().solve(board)
    print(board)
