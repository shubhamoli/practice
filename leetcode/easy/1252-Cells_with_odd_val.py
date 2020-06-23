"""
    Leetcode #1252
"""


from typing import List

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        if not indices:
            return 0

        rows = [0] * n
        cols = [0] * m

        for r, c in indices:
            rows[r] += 1
            cols[c] += 1

        # we'll just be simulating changes using count from rows and cols above
        count = 0
        for i in range(n):
            for j in range(m):
                if (rows[i] + cols[j]) % 2 != 0:
                    count += 1

        return count


if __name__ == "__main__":

    solution = Solution()

    assert solution.oddCells(2, 3, [[0,1],[1,1]]) == 6


