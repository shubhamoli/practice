"""
    Leetcode #344
"""


from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for i in range(len(s)//2):
            s[i], s[len(s)-1 - i] = s[len(s)-1 - i], s[i]


if __name__ == "__main__":

    solution = Solution()

    s = []
    solution.reverseString(s)
    assert s == []

    s = ["o"]
    solution.reverseString(s)
    assert s == ["o"]

    s = ["i", "l", "O"]
    solution.reverseString(s)
    assert s == ["O", "l", "i"]

