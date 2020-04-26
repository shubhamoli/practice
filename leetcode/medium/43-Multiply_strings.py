"""
    Leetcode #43
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0]* (len(num1) + len(num2))

        for i, el in enumerate(reversed(num1)):
            for j, el2 in enumerate(reversed(num2)):
                res[i+j] +=  (ord(el) - ord('0')) * (ord(el2) - ord('0'))
                res[i+j+1] += res[i+j] // 10
                res[i+j] %= 10

        while len(res) > 1 and res[-1] == 0: res.pop()

        return "".join( map(str,res[::-1]) )


if __name__ == "__main__":

    solution = Solution()

    assert solution.multiply("2", "3") == "6"
    assert solution.multiply("123", "456") == "56088"

