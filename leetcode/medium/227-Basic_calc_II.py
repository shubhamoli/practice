"""
    Leetcode #227
"""

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        stk = []
        num = 0
        sign = "+"

        for i in range(len(s)):
            if s[i].isdigit():
                # build number until no sign is found
                num = num*10 + (ord(s[i]) - ord('0'))

            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:

                if sign == "-":
                    stk.append(-num)
                if sign == "+":
                    stk.append(num)
                if sign == "*":
                    stk.append(stk.pop() * num)
                if sign == "/":
                    tmp = stk.pop()
                    if tmp // num < 0 and tmp % num != 0:
                        stk.append(tmp // num+1)
                    else:
                        stk.append(tmp // num)

                sign = s[i]
                # reset num
                num = 0

        return sum(stk)



if __name__ == "__main__":

    solution = Solution()

    assert solution.calculate("3+2*2") == 7
    assert solution.calculate(" 3/2 ") == 1
    assert solution.calculate(" 3+5 / 2 ") == 5
