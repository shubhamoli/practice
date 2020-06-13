"""
    Leetcode #821
"""


from typing import List
import bisect

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        if not S:
            return []

        res = [0] * len(S)

        # traverse left to right
        prev = float("-inf")
        for i in range(len(S)):
            if S[i] == C:
                prev = i
            res[i] = i - prev

        # traverse right to left
        prev = float("inf")
        for i in range(len(S)-1, -1, -1):
            if S[i] == C:
                prev = i
            res[i] = min(res[i], prev - i)

        return res



if __name__ == "__main__":

    solution = Solution()

    assert solution.shortestToChar("loveleetcode", "e") == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
    assert solution.shortestToChar("baaa", "b") == [0, 1, 2, 3]

