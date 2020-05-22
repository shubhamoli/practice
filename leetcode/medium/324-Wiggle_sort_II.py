"""
    Leetcode #324
"""


from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]


if __name__ == "__main__":

    nums = [1, 5, 1, 1, 6, 4]
    Solution().wiggleSort(nums)
    print(nums)     # [1, 4, 1, 5, 1, 6] or [1, 6, 1, 5, 1, 4]

