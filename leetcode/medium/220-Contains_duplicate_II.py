"""
    Leetcode #220
"""


from typing import List


class Solution:
    def containsNearbyAlmostDuplicate_BF(self, nums: List[int], k: int, t: int) -> bool:
        if not nums:
            return False

        # if target is 0 and array contains no duplicates
        # this is not possible, as (dup1 - dup2 == 0)
        if t == 0 and len(set(nums)) == len(nums):
            return False

        N = len(nums)
        for i in range(N):
            for j in range(i, N):
                if i != j and abs(nums[i] - nums[j]) <= t and abs(i - j) <= k:
                    return True

        return False


if __name__ == "__main__":

    solution = Solution()

    assert solution.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0) == True
    assert solution.containsNearbyAlmostDuplicate([1,0,1,1], 1, 2) == True
    assert solution.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3) == False

