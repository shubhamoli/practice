"""
    Leetcode #289
"""

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isSafe(i, j, board):
            if i>=0 and i <len(board) and j>=0 and j <len(board[0]):
                return True
            return False

        def count_live_neighbours(i, j, board):
            row_nbr = [-1,-1,-1,0,0,1,1,1]
            col_nbr = [-1,0,1,-1,1,-1,0,1]
            c = 0
            for k in range(8):
                # 2 (>1) is also accpetable as it is live in this iteration (games' iteration)
                if isSafe(i + row_nbr[k], j + col_nbr[k], board) and board[i + row_nbr[k]][j + col_nbr[k]] >= 1:
                    c += 1
            return c

        #First loop mark cell which will die as 2, and will become alive as -1;
        for i in range(len(board)):
            for j in range(len(board[0])):
                live_neighbours = count_live_neighbours(i,j,board=board)
                # rule 4
                if board[i][j] == 0 and live_neighbours == 3:
                    board[i][j] = -1
                # rule 3
                elif board[i][j] == 1 and live_neighbours > 3:
                    board[i][j] = 2
                # rule 2
                elif board[i][j] == 1 and live_neighbours in [2,3]:
                    board[i][j] = 1
                # rule 1
                elif board[i][j] == 1 and live_neighbours <2 :
                    board[i][j] = 2


        # Update board
        for i in range(len(board)):
            for j in range(len(board[0])):
                # those are supposed to alive
                # mark them 1
                if board[i][j]==-1:
                    board[i][j] = 1
                # those who are supposed to be dead
                # mark them 0
                elif board[i][j]==2:
                    board[i][j] = 0

if __name__ == "__main__":

    board = [
          [0,1,0],
          [0,0,1],
          [1,1,1],
          [0,0,0]
    ]

    Solution().gameOfLife(board)

    """
    Expecting
    [
      [0,0,0],
      [1,0,1],
      [0,1,1],
      [0,1,0]
    ]
    """
    print(board)
