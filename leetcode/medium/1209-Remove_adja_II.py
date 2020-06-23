"""
    Leetcode #1209
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s:
            return s

        stk = []

        for c in s:
            if stk and stk[-1][0] == c:
                stk[-1][1] += 1
                # if count matches k, pop it
                if stk[-1][1] == k:
                    stk.pop()
            else:
                stk.append([c, 1])

        return "".join([c*k for c, k in stk])


if __name__ == "__main__":

    solution = Solution()

    assert solution.removeDuplicates("deeedbbcccbdaa", 3) == "aa"
