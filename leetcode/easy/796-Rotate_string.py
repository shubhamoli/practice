"""
    Leetcode #796
"""


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        if not A:
            return True

        def helper(rotation):
            for i in range(len(A)):
                if A[i] != B[(i+rotation) % len(A)]:
                    return False

            return True

        # try all rotation and if helper return True in any rotation i
        # return True
        for i in range(len(A)):
            if helper(i):
                return True

        return False


    def rotateString_OPTI(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A+A


if __name__ == "__main__":

    solution = Solution()

    assert solution.rotateString("abcde", "cdeab") == True
    assert solution.rotateString("abcde", "abced") == False

    assert solution.rotateString_OPTI("abcde", "cdeab") == True
    assert solution.rotateString_OPTI("abcde", "abced") == False

