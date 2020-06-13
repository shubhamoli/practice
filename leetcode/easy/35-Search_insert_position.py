"""
    Leetcode #35
"""


from typing import List

class Solution:
    def searchInsert_OPTI(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0

        if target == nums[-1]:
            return len(nums)-1

        if target > nums[-1]:
            return len(nums)

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            if target < nums[m]:
                r = m - 1
            if target > nums[m]:
                l = m + 1

        return l

    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        if target <= nums[0]:
            return 0

        if target == nums[-1]:
            return len(nums)-1

        if target > nums[-1]:
            return len(nums)

        i = 0
        while i < len(nums):
            if nums[i] >= target:
                return i
            else:
                i += 1

        return i


if __name__ == "__main__":

    solution = Solution()

    assert solution.searchInsert([1,3,5,6], 5) == 2
    assert solution.searchInsert([1,3,5,6], 2) == 1
    assert solution.searchInsert([1,3,5,6], 7) == 4
    assert solution.searchInsert([1,3,5,6], 0) == 0

    assert solution.searchInsert_OPTI([1,3,5,6], 5) == 2
    assert solution.searchInsert_OPTI([1,3,5,6], 2) == 1
    assert solution.searchInsert_OPTI([1,3,5,6], 7) == 4
    assert solution.searchInsert_OPTI([1,3,5,6], 0) == 0
