"""
    Leetcode #80
"""


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = 0
        i = 0
        while i < len(nums):
            # if count >= 2
            # remove element
            if count >= 2:
                # next is different reset counter
                if len(nums) - i > 1 and nums[i] != nums[i+1]:
                    count = 0

                # remove element as this position
                print(i)
                nums.pop(i)
            else:
                # if next is same increase counter
                # else reset it
                if len(nums) - i > 1 and nums[i] == nums[i+1]:
                    count += 1
                else:
                    count = 0
                i += 1

        return len(nums)



if __name__ == "__main__":

    assert Solution().removeDuplicates([1,1,1,2,2,3]) == 5
    assert Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]) == 7
