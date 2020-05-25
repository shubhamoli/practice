"""
    Leetcode #357
"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """
        for n = 1, you have 9 choices
        for n = 2, you have 9*9 choices
        for n = 3, you have 9*9*8 choices for unique digits
        ...
        ...
        for n = 10, you have 9*9*8*7....1 choices for unique digits
        for n > 10, there can't be any number with unique digits
        """

        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1

        for i in range(n if n <= 10 else 10):
            product *= choices[i]
            ans += product

        return ans


if __name__ == "__main__":


    assert Solution().countNumbersWithUniqueDigits(2) == 91

