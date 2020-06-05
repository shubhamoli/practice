"""
    Leetcode #9
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x >= 0 and x < 10:
            return True

        tmp = x
        y = 0
        while tmp > 0:
            t = tmp % 10
            y = 10*y + t
            tmp = tmp // 10

        return x == y

if __name__ == "__main__":

    solution = Solution()

    assert solution.isPalindrome(121) == True
    assert solution.isPalindrome(-121) == False
    assert solution.isPalindrome(10) == False

