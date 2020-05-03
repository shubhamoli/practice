"""
    Leetcode #81
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        l, r = 0, len(nums) - 1

        while l<=r:
            mid= l+(r-l)//2

            if nums[mid]==target:
                return True

            while l < mid and nums[l] == nums[mid]:
                l += 1

            # Notmal case
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1

            # Rotation case
            else:
                if nums[mid] < target<= nums[r]:
                    l = mid+1
                else:
                    r = mid-1

        return False



if __name__ == "__main__":

    solution = Solution()

    assert solution.search([2,5,6,0,0,1,2], 0) == True
    assert solution.search([2,5,6,0,0,1,2], 3) == False

