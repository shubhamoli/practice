"""
    Leetcode #55
"""


from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False

        def helper(idx):
            if idx == len(nums) - 1:
                return True

            jump = min(len(nums)-1, idx+nums[idx])
            for i in range(idx+1, jump+1):
                if helper(i):
                    return True

            return False

        return helper(0)

    def canJump_OPTI(self, nums: List[int]) -> bool:
        farest = 0;
        for i in range(len(nums)):
            if farest < i:
                return False
            farest = max(i + nums[i], farest)

        return True


if __name__ == "__main__":

    solution = Solution()

    assert solution.canJump([2,3,1,1,4]) == True
    assert solution.canJump([3,2,1,0,4]) == False

    assert solution.canJump_OPTI([2,3,1,1,4]) == True
    assert solution.canJump_OPTI([3,2,1,0,4]) == False
