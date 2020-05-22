"""
    Leetcode #318
"""

from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if not words:
            return 0

        L = len(words)
        vals = [0] * len(words)

        for i in range(L):
            for c in words[i]:
                vals[i] |= 1 << (ord(c) - ord('a'))

        _max = float("-inf")
        for i in range(L):
            for j in range(i+1, L):
                if vals[i] & vals[j] == 0:
                    _max = max(_max, len(words[i]) * len(words[j]))

        return _max if _max != float("-inf") else 0


if __name__ == "__main__":

    solution = Solution()

    assert solution.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]) == 16
    assert solution.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]) == 4
    assert solution.maxProduct(["a","aa","aaa","aaaa"]) == 0

