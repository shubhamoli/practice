"""
    Leetcode #377
"""

from typing import List
from collections import defaultdict

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        res = 0
        memo = {}
        def helper(target):
            if memo.get(target) is not None:
                return memo[target]

            if target == 0:
                return 1

            if target < 0:
                return 0

            res = 0
            for i in range(len(nums)):
                res += helper(target-nums[i])

            memo[target] = res
            return res

        memo = defaultdict(int)
        return helper(target)


if __name__ == "__main__":

    assert Solution().combinationSum4([1, 2, 3], 4) == 7
    assert Solution().combinationSum4([1, 2], 10) == 89
