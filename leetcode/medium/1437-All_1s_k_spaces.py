"""
    Leetcode #1437
"""


from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        N, last = len(nums), -1
        for i in range(len(nums)):
            if nums[i] == 1 and last == -1:
                last = i
                continue

            if nums[i] == 1 and last != -1:
                if i - last <= k:
                    return False
                last = i

        return True


if __name__ == "__main__":

    solution = Solution()

    assert solution.kLengthApart([1,0,0,0,1,0,0,1], 2) == True
    assert solution.kLengthApart([1,0,0,1,0,1], 2) == False
