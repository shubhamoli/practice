"""
    Leetcode #390
"""


class Solution:
    def lastRemaining(self, n: int) -> int:

        left = True
        step = 1
        head = 1
        remaining = n
        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step

            step *= 2
            left = not left
            remaining = remaining // 2

        return head



if __name__ == "__main__":

    solution = Solution()

    assert solution.lastRemaining(9) == 6
