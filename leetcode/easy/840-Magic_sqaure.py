"""
    Leetcode #840
"""


from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        M = len(grid)
        N = len(grid[0])

        if M < 3 or N < 3:
            return 0

        def helper(i, j):
            nums = set(grid[a][b] for b in range(j,j+3) for a in range(i,i+3) if grid[a][b]>=1 and grid[a][b]<=9)

            a = grid[i][j:j+3]
            b = grid[i+1][j:j+3]
            c = grid[i+2][j:j+3]
            d = [grid[x][j] for x in range(i, i+3)]
            e = [grid[x][j+1] for x in range(i, i+3)]
            f = [grid[x][j+2] for x in range(i, i+3)]
            g = [grid[x+i][y+j] for x in range(3) for y in range(3) if x == y]
            h = [grid[x+i][y+j] for x in range(2, -1, -1) for y in range(3) if x+y == 2]

            return sum(a) == sum(b) == sum(c) == sum(d) == sum(e) == sum(f) == sum(g) == sum(h) and len(nums)==9

        count = 0
        for i in range(M-2):
            for j in range(N-2):
                if helper(i, j):
                    count += 1

        return count



if __name__ == "__main__":

    solution = Solution()

    grid = [[4,3,8,4],
            [9,5,1,9],
            [2,7,6,2]]
    assert solution.numMagicSquaresInside(grid) == 1

