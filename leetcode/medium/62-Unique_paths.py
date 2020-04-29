"""
    Leetcode #62
"""


class Solution:
    count = 0
    def uniquePaths(self, m: int, n: int) -> int:

        if not m:
            return n

        if not n:
            return m

        matrix = [[1 for x in range(n)] for x in range(m)]
        self.count = 0      # reset counter

        def helper(a, b):
            if a == m or b == n:
                self.count = self.count + 1
                return

            for path in ["right", "down"]:
                if path == "right":
                    helper(a+1, b)
                if path == "down":
                    helper(a, b+1)


        helper(1, 1)
        return self.count

    def uniquePaths_DP(self, m: int, n: int) -> int:

        if not m:
            return n

        if not n:
            return m

        matrix = [[0 for x in range(n)] for x in range(m)]

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
                # only way to reach current cell is from either up or left
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        return matrix[-1][-1]



if __name__ == "__main__":

    solution = Solution()

    assert solution.uniquePaths(3, 2) == 3
    assert solution.uniquePaths(7, 3) == 28
    assert solution.uniquePaths_DP(3, 2) == 3
    assert solution.uniquePaths_DP(7, 3) == 28


