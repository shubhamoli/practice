"""
    Leetcode #300
"""


from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = [[-1 for i in range(len(nums)+1)] for j in range(len(nums))]

        def helper(idx, prevIdx):
            if idx == len(nums):
                return 0

            if memo[prevIdx+1][idx] >= 0:
                return memo[prevIdx+1][idx]

            taken = 0
            # taking current item
            if prevIdx < 0 or nums[idx] > nums[prevIdx]:
                taken = 1 + helper(idx+1, idx)

            # skipping current item
            not_taken = helper(idx+1, prevIdx)

            memo[prevIdx+1][idx] = max(taken, not_taken)

            return memo[prevIdx+1][idx]

        return helper(0, -1)


if __name__ == "__main__":

    assert Solution().lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
