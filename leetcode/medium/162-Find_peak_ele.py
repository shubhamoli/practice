"""
    Leetcode #162
"""


from typing import List

class Solution:

    # O(n) - simple and intuitive
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return

        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i

        return -1

    # O(logn) - complexity
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return

        if len(nums) < 2:
            return 0

        # left most
        if nums[0] > nums[1]:
            return 0

        # right most
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid

            elif nums[mid] < nums[mid-1]:
                r = mid-1

            elif nums[mid] < nums[mid+1]:
                l = mid + 1

        return -1


if __name__ == "__main__":

    assert Solution().findPeakElement([1,2,3,1]) == 2    # index 2
    assert Solution().findPeakElement([1,2,1,3,5,6,4]) == 5     # index 5

