"""
    Leetcode #153
"""


from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid+1

        return nums[right]


if __name__ == "__main__":

    assert Solution().findMin([3,4,5,1,2] ) == 1
    assert Solution().findMin([3,4,5,6,1,2] ) == 1
    assert Solution().findMin([4,5,6,7,0,1,2]) == 0
