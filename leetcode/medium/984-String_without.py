"""
    Leetcode #984
"""


class Solution:
    def strWithout3a3b_ITER(self, A: int, B: int) -> str:
        res = []
        while A + B > 0:
            last_2 = res[-2:]

            if last_2 == ["a", "a"]:
                res.append("b")
                B -= 1
            elif last_2 == ["b", "b"]:
                res.append("a")
                A -= 1
            elif A > B:
                res.append("a")
                A -= 1
            else:
                res.append("b")
                B -= 1

        return "".join(res)

    def strWithout3a3b_RECUR(self, A: int, B: int) -> str:
        if A == 0:
            return B*"b"

        if B == 0:
            return A*"a"

        if A == B:
            return "ab" + self.strWithout3a3b_RECUR(A-1, B-1)

        if A > B:
            return "aab" + self.strWithout3a3b_RECUR(A-2, B-1)

        return "bba" + self.strWithout3a3b_RECUR(A-1, B-2)


if __name__ == "__main__":

    solution = Solution()

    assert solution.strWithout3a3b_ITER(1, 2) == "bba"
    assert solution.strWithout3a3b_ITER(4, 1) == "aabaa"

    assert solution.strWithout3a3b_RECUR(1, 2) == "bba"
    assert solution.strWithout3a3b_RECUR(4, 1) == "aabaa"
