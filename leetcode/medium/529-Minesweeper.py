"""
    Leetcode #529
"""


from leetcode.utils import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or not board[0]:
            return


        M = len(board)
        N = len(board[0])

        r, c = click

        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        def helper(r, c):
            if board[r][c] != 'E':
                return

            mines = 0
            dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

            for d in dirs:
                i, j = r + d[0], c + d[1]
                if 0 <= i < M and 0 <= j < N and board[i][j] == 'M':
                    mines += 1

            if mines == 0:
                board[r][c] = 'B'
            else:
                board[r][c] = str(mines)
                return

            for d in dirs:
                i, j = r + d[0], c + d[1]
                if 0 <= i < M and 0 <= j < N:
                    helper(i, j)


        helper(r, c)
        return board



if __name__ == "__main__":

    solution = Solution()

    board = [['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E']]

    output = [['B', '1', 'E', '1', 'B'],
             ['B', '1', 'M', '1', 'B'],
             ['B', '1', '1', '1', 'B'],
             ['B', 'B', 'B', 'B', 'B']]

    assert solution.updateBoard(board, [3, 0]) == output

    board = [['B', '1', 'E', '1', 'B'],
            ['B', '1', 'M', '1', 'B'],
            ['B', '1', '1', '1', 'B'],
            ['B', 'B', 'B', 'B', 'B']]

    output = [['B', '1', 'E', '1', 'B'],
             ['B', '1', 'X', '1', 'B'],
             ['B', '1', '1', '1', 'B'],
             ['B', 'B', 'B', 'B', 'B']]

    assert solution.updateBoard(board, [1, 2]) == output

