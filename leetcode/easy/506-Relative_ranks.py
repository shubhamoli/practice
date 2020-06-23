"""
    Leetcode #506
"""


from typing import List

class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        sorted_nums = sorted(nums, reverse=True)
        store = {}
        N = len(nums)

        for i in range(N):
            if i == 0:
                store[sorted_nums[i]] = "Gold Medal"
            elif i == 1:
                store[sorted_nums[i]] = "Silver Medal"
            elif i == 2:
                store[sorted_nums[i]] = "Bronze Medal"
            else:
                store[sorted_nums[i]] = str(i+1)

        return [store[i] for i in nums]


if __name__ == "__main__":

    solution = Solution()

    print(solution.findRelativeRanks([5, 4, 3, 2, 1]))  #["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
