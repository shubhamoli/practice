"""
    Leetcode #96
"""


# Similar to find nth catalan number
class Solution:
    def numTrees(self, n: int) -> int:

        memo = {}
        self.count = 0

        def uniqueTrees(n):
            if n < 1:
                return 1

            if n in memo:
                return memo[n]

            self.count +=  sum([uniqueTrees(i - 1) * uniqueTrees(n - i) for i in range(1 , n + 1)])

            memo[n] = self.count

            return self.count

        return uniqueTrees(n)


if __name__ == "__main__":

    solution = Solution()

    assert solution.numTrees(1) == 1
    assert solution.numTrees(2) == 2
    assert solution.numTrees(3) == 5
