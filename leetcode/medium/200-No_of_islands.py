"""
    Leetcode #200
"""


from typing import List


class Solution:
    count = 0
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        M = len(grid)
        N = len(grid[0])

        def helper(i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
                return

            grid[i][j] = '#'

            helper(i+1, j)
            helper(i-1, j)
            helper(i, j+1)
            helper(i, j-1)

        count = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    helper(i, j)
                    count +=1

        print(count)
        return count



if __name__ == "__main__":

    solution = Solution()

    matrix = [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]

    assert solution.numIslands(matrix) == 1

    matrix = [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]

    assert solution.numIslands(matrix) == 3
