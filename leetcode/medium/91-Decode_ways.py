"""
    Leetcode #91
"""


from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:

        if not s: return 0

        @lru_cache(maxsize=None)
        def helper(s):
            if not s: return 1
            tmp = 0

            # Skip zeroes and take next
            if 0 < int(s[0]) <= 9:
                tmp += helper(s[1:])

            # or take next 2s
            if 10 <= int(s[:2]) <= 26:
                tmp += helper(s[2:])

            return tmp

        return helper(s)

if __name__ == "__main__":


    solution = Solution()

    assert solution.numDecodings("12") == 2
    assert solution.numDecodings("226") == 3

