"""
    Leetcode #224
"""


class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        sign = 1
        number = 0
        stk = []

        for ch in s:
            if ch.isdigit():
                number = (10 * number) + (ord(ch)-ord('0'))

            elif ch == '+':
                res += sign * number
                number = 0
                sign = 1
            elif ch == '-':
                res += sign * number
                number = 0
                sign = -1
            elif ch == '(':
                stk.append(res)
                stk.append(sign)
                sign = 1
                res = 0
            elif ch == ')':
                res += sign * number
                number = 0
                res *= stk.pop() # sign
                res += stk.pop() # result calculated before "("

        if number != 0:
            res += sign * number

        return res




if __name__ == "__main__":

    solution = Solution()

    assert solution.calculate(" 2-1 + 2 ") == 3
    assert solution.calculate("(1+(4+5+2)-3)+(6+8)") == 23

