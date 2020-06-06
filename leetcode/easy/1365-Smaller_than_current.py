"""
    Leetcode #1365
"""


from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        res = [0] * len(nums)

        for i in range(len(nums)):
            tmp = nums[i]
            for j in range(len(nums)):
                if i != j and nums[j] < tmp:
                    res[i] += 1

        return res

    def smallerNumbersThanCurrent_OPTI(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        sorted_nums = sorted(nums) # nlogn

        N = len(nums)
        store = {}

        for i in range(N):
            if store.get(sorted_nums[i]) is None:
                store[sorted_nums[i]] = i

        res = [0] * N
        for i in range(N):
            res[i] = store.get(nums[i])


        return res



if __name__ == "__main__":

    solution = Solution()

    assert solution.smallerNumbersThanCurrent([8,1,2,2,3]) ==  [4,0,1,1,3]
    assert solution.smallerNumbersThanCurrent_OPTI([8,1,2,2,3]) ==  [4,0,1,1,3]

