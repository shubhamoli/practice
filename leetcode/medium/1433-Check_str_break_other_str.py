"""
    Leetcode #1433
"""


from collections import Counter


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:

        def check(d1, d2):
            diff = 0
            for c in "abcdefghijklmnopqrstuvwxyz":
                diff += d1[c] - d2[c]
                if diff < 0:    # if anytime diff < 0, return false
                    return False

            return True

        d1 = Counter(s1)
        d2 = Counter(s2)

        return check(d1, d2) or check(d2, d1)

    def checkIfCanBreak_Sort(self, s1: str, s2: str) -> bool:

        a = sorted(s1)
        b = sorted(s2)

        i = 0
        while i < len(a) and a[i] >= b[i]:
            i += 1

        if i == len(a): return True

        i = 0
        while i < len(b) and b[i] >= a[i]:
            i += 1

        if i == len(b): return True

        return False


if __name__ == "__main__":

    solution = Solution()

    assert solution.checkIfCanBreak("abc", "xya") == True
    assert solution.checkIfCanBreak("abe", "acd") == False
    assert solution.checkIfCanBreak("leetcodee", "interview") == True

    assert solution.checkIfCanBreak_Sort("abc", "xya") == True
    assert solution.checkIfCanBreak_Sort("abe", "acd") == False
    assert solution.checkIfCanBreak_Sort("leetcodee", "interview") == True

