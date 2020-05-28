"""
    Leetcode #1456
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if not s:
            return 0

        if len(s) < k:
            return 0

        vowels = {"a", "e", "i", "o", "u"}
        res = 0

        for i in range(k):
            res += (1 if s[i] in vowels else 0)

        curr = res
        for i in range(k, len(s)):
            curr += (1 if s[i] in vowels else 0) - (1 if s[i-k] in vowels else 0)
            res = max(curr, res)

        return res


if __name__ == "__main__":

    solution = Solution()

    assert solution.maxVowels("abciiidef", 3) == 3
    assert solution.maxVowels("leetcode", 3) == 2
