"""
    Leetcode #241
"""

from typing import List

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        ops = {
            "+": lambda a, b: a+b,
            "-": lambda a, b: a-b,
            "*": lambda a, b: a*b,
        }

        if input.isdigit():
            return [int(input)]

        res = []
        for i in range(len(input)):
            if input[i] in "+-*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                res.extend([ops[input[i]](l, r) for l in left for r in right])

        return res


if __name__ == "__main__":

    solution = Solution()

    print(solution.diffWaysToCompute("2-1-1"))      # [0, 2]`
    print(solution.diffWaysToCompute("2*3-4*5"))    # [-34, -14, -10, -10, 10]

