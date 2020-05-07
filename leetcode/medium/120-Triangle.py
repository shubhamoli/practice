"""
    Leetcode #120
"""


from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def dp(row,col):
            if row == len(triangle)-1:
                return triangle[row][col]

            if (row,col) not in memo:
                memo[(row,col)] = triangle[row][col] + min(dp(row+1,col),dp(row+1,col+1))

            return memo[(row,col)]

        memo = {}
        return dp(0,0)


if __name__ == "__main__":

    triangle = [
                 [2],
                [3,4],
               [6,5,7],
              [4,1,8,3]
            ]

    triangle2 = [
                    [-1],
                   [2, 3],
                  [1,-1,-3]
            ]

    # assert Solution().minimumTotal(triangle) == 11
    assert Solution().minimumTotal(triangle2) == -1
