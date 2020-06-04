"""
    Leetcode #403
"""


from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:

        memo = set()
        target = stones[-1]
        stones = set(stones)

        def helper(pos, jump):
            if (pos, jump) in memo:
                return False

            if pos == target:
                return True

            if jump <= 0 or pos not in stones:
                return False

            for j in (jump-1, jump, jump+1):
                if pos+j in stones and helper(pos+j, j):
                    return True

            memo.add((pos, jump))   # record bad position and jump
            return False

        return helper(1, 1)


if __name__ == "__main__":

    solution = Solution()

    assert solution.canCross([0,1,3,5,6,8,12,17]) == True
    assert solution.canCross([0,1,2,3,4,8,9,11]) == False
