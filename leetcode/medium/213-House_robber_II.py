"""
    Leetcode #213
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        if len(nums) == 3:
            return max(nums[0], nums[1], nums[2])

        dp1 = [0] * (len(nums) -1)
        dp2 = [0] * (len(nums) -1)

        dp1[0] = nums[0] # start with first house and leave last house (as they are adjacent)
        dp1[1] = max(nums[0], nums[1])

        dp2[0] = nums[1] # skip first house and free to include last house
        dp2[1] = max(nums[1], nums[2])

        for i in range(2,len(nums)-1):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i+1])

        return max(dp1[-1], dp2[-1])


if __name__ == "__main__":

    solution = Solution()

    assert solution.rob([2,3,2]) == 3
    assert solution.rob([1,2,3,1]) == 4
    assert solution.rob([1,2,1,1]) == 3
