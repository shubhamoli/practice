"""
    Leetcode #50
"""



class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n

        res = 1
        for i in range(abs(n)):
            res = x * res

        return res

    def myPow_OPTI(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n

        res = 1
        while n > 0:
            if n % 2:
                res *= x
            x = x * x
            n = n // 2

        return res


if __name__ == "__main__":

    solution = Solution()

    print(solution.myPow(2.00000, 10))
    print(solution.myPow(2.10000, 3))
    print(solution.myPow(2.00000, -2))

    print(solution.myPow_OPTI(2.00000, 10))
    print(solution.myPow_OPTI(2.10000, 3))
    print(solution.myPow_OPTI(2.00000, -2))

