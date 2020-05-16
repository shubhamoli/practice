"""
    Leetcode #201
"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0

        while m  != n:
             m >>= 1
             n >>= 1
             i += 1

        return n << i


if __name__ == "__main__":

    assert Solution().rangeBitwiseAnd(5, 7) == 4
