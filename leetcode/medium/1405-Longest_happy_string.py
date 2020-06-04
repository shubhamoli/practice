"""
    Leetcode #1405
"""


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        A = 0
        B = 0
        C = 0
        res = []

        length = a+b+c
        for i in range(length):
            if (a >=b and a >= c and A < 2) or (B == 2 and a > 0) or (C == 2 and a > 0):
                res.append("a")
                a -= 1
                A += 1
                B = 0
                C = 0

            elif (b >= a and b >= c and B < 2) or (A == 2 and b > 0) or (C == 2 and b > 0):
                res.append("b")
                b -= 1
                B += 1
                A = 0
                C = 0
            elif (c >=b and c >= a and C < 2) or (A == 2 and c > 0) or (B == 2 and c > 0):
                res.append("c")
                c -= 1
                C += 1
                A = 0
                B = 0

        return "".join(res)


if __name__ == "__main__":

    solution = Solution()

    assert solution.longestDiverseString(1, 1, 7) == "ccaccbcc"
    assert solution.longestDiverseString(2, 2, 1) == "aabbc"

