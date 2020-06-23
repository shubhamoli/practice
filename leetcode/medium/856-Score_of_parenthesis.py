"""
    Leetcode #856
"""


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        if not S:
            return 0

        stk = []
        score = 0

        for s in S:
            if s == '(':
                stk.append(score)
                score = 0
            elif s == ')':
                score = stk.pop() + max(score * 2, 1)

        return score


if __name__ == "__main__":

    solution = Solution()

    assert solution.scoreOfParentheses("()") == 1
    assert solution.scoreOfParentheses("(())") == 2
    assert solution.scoreOfParentheses("()()") == 2
    assert solution.scoreOfParentheses("(()(()))") == 6


