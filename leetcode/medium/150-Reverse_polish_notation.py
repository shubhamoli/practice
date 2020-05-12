"""
    Leetcode #150
"""


from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stk = []
        oprs = {
            "+": lambda a,b: a + b,
            "-": lambda a,b: a - b,
            "*": lambda a,b: a * b,
            "/": lambda a,b: a / b
        }
        for i in tokens:
            if not i in "+-*/":
                stk.append(i)
            else:
                second = int(stk.pop())
                first = int(stk.pop())
                res = oprs[i](first, second)
                stk.append(res)

        return int(stk[-1])



if __name__ == "__main__":

    solution = Solution()

    assert solution.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert solution.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22

