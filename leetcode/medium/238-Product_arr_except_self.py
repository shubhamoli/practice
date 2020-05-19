"""
    Leetcode #238
"""


from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        res = [1 for i in nums]

        left = 1
        right = 1

        for i in range(len(nums)):
            res[i] *= left
            res[-1-i] *= right
            left *= nums[i]
            right *= nums[-1-i]

        return res



if __name__ == "__main__":

    assert Solution().productExceptSelf([1,2,3,4]) == [24,12,8,6]
