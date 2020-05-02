"""
    Leetcode #75
"""


from typing import List


class Solution:
    # two pass
    def sortColors_COUNTING_SORT(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counter = [0, 0, 0]     # one for each 0, 1, and 2

        for i in nums:
            counter[i] += 1

        i = 0
        for k in range(len(counter)):
            while counter[k] > 0:
                nums[i] = k
                i += 1
                counter[k] -= 1


    # Single pass
    # great solution
    # Dutch National Flag Problen
    # https://en.wikipedia.org/wiki/Dutch_national_flag_problem
    # see pseudocode section in this wiki page
    def sortColors(self, nums: List[int]) -> None:
        if len(nums) < 2: return nums

        low, high, i = 0, len(nums)-1, 0

        while i <= high:

            if nums[i] == 2:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1

            elif nums[i] == 1:
                i += 1

            else:
                nums[i], nums[low] = nums[low], nums[i]
                i, low = i + 1, low + 1

        return nums



if __name__ == "__main__":

    nums = [2,0,2,1,1,0]
    Solution().sortColors_COUNTING_SORT(nums)
    print(nums)     # [0,0,1,1,2,2]

    nums = [2,0,2,1,1,0]
    Solution().sortColors(nums)
    print(nums)     # [0,0,1,1,2,2]
