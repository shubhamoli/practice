"""
    Leetcode #33
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(l, r) :
            if r < l:
                return -1
            mid = l + (r-l) // 2
            if nums[mid] ==  target:
                return mid
            # Normal
            elif nums[l] <= target < nums[mid]:
                return helper(l, mid-1)
            elif nums[mid] < target <= nums[r]:
                return helper(mid+1, r)

            # Rotated
            elif nums[mid] > nums[r]:
                return helper(mid+1, r)
            else:
                return helper(l, mid-1)

        return helper(0, len(nums)-1)

if __name__ == "__main__":

    solution = Solution()

    assert solution.search([4, 5, 6, 7, 0, 1, 2], 1) == 5
