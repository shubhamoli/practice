"""
    Leetcode #79
"""


from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False

        if not board[0]:
            return False

        m = len(board)
        n = len(board[0])

        # using separate visited array
        # but you can do that without using it
        # by just setting board[i][j] == "#" or any char when visiting a cell
        # then reset it back to original value
        visited = [[False]*n for x in range(m)]

        def helper(i, j, idx):
            if idx == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[idx] or visited[i][j]:
                return False

            # Mark visited
            visited[i][j] = True

            # Search in adjacent cells
            # left, right, top, bottom (4 recursive calls)
            if helper(i+1, j, idx+1) or helper(i-1, j, idx+1) or helper(i, j+1, idx+1) or helper(i, j-1, idx+1):
                return True

            # reset visited array for next further searches
            visited[i][j] = False

            return False



        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and helper(i, j, 0):
                    return True

        return False


if __name__ == "__main__":

    solution = Solution()

    matrix = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

    assert solution.exist(matrix, "ABCCED") == True
    assert solution.exist(matrix, "SEE") == True
    assert solution.exist(matrix, "ABCB") == False


