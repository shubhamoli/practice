"""
    Leetcode #63
"""


from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0

        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        matrix = [[0]*n for x in range(m)]

        # set element in first column to 1
        # as there is only 1 way to reach them
        for i in range(n):
            matrix[0][i] = 1

        # set element in first row to 1
        # as there is only 1 way to reach them
        for i in range(m):
            matrix[i][0] = 1

        # expand like we're increasing m and n
        for i in range(1, m):
            for j in range(1, n):
                # if it is one, then skip this
                if obstacleGrid[i][j] == 1:
                    continue
                # only way to reach current cell is from either up or left
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        return matrix[-1][-1]



if __name__ == "__main__":

    solution = Solution()

    assert solution.uniquePathsWithObstacles([[0,0,0], [0,1,0], [0,0,0]]) == 2
