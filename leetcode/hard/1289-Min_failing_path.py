"""
    Leetcode #1289
"""


from typing import List
import heapq

class Solution:
    # DFS + memoization will cause TLE
    # due to internal function overhead
    def minFallingPathSum(self, arr: List[List[int]]) -> int:

        if not arr or not arr[0]:
            return 0

        M = len(arr)
        N = len(arr[0])

        memo = [[float("inf") for j in range(N+1)] for _ in range(M+1)]

        def helper(idx, jdx):
            if idx > M - 1 or jdx > N - 1:
                return 0

            if memo[idx][jdx] != float("inf"):
                return memo[idx][jdx]

            mins = float("inf")
            for j in range(N):
                if j == jdx:
                    continue

                mins = min(mins, arr[idx][j] + helper(idx+1, j))

            memo[idx][jdx] = mins
            return memo[idx][jdx]

        minimum = float("inf")
        for j in range(N):
            minimum = min(minimum, helper(0, j))

        return minimum


    def minFallingPathSum_DP(self, arr: List[List[int]]) -> int:
        M = len(arr)
        N = len(arr[0])

        # to avoid manipulating original array
        tmp = [[arr[i][j] for j in range(N)] for i in range(M)]

        for i in range(1, M):
            # find 2 smallest in previous row
            # as if one may belong to same column, we can skip it and pick another
            r = heapq.nsmallest(2, tmp[i - 1])
            for j in range(N):
                tmp[i][j] += r[1] if tmp[i - 1][j] == r[0] else r[0]

        return min(tmp[-1])


if __name__ == "__main__":

    solution = Solution()

    arr = [ [1,2,3],
            [4,5,6],
            [7,8,9]]

    assert solution.minFallingPathSum(arr) == 13
    assert solution.minFallingPathSum_DP(arr) == 13

