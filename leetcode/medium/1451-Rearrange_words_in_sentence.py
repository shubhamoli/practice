"""
    Leetcode #1451
"""

from collections import defaultdict


class Solution:
    def arrangeWords(self, text: str) -> str:
        if not text:
            return ""

        arr = text.split()

        # sorting in python is stable
        # so relative index of same level keys are maintained
        # keep will always come before calm and code in "Keep calm and code on"
        arr = sorted(arr, key=len)

        return " ".join(arr).capitalize()




if __name__ == "__main__":

    solution = Solution()

    assert solution.arrangeWords("Leetcode is cool") == "Is cool leetcode"
    assert solution.arrangeWords("Keep calm and code on") == "On and keep calm code"
    assert solution.arrangeWords("To be or not to be") == "To be or to be not"


