"""
    Leetcode #209
"""


from typing import List

class Solution:
    # O(n) - Sliding window
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return

        l = 0   # left pointer of sliding window
        res = len(nums) + 1     # let len greater then len(nums)
        curr = 0    # to track current sum

        for r in range(len(nums)):
            curr += nums[r]

            while curr >= s:
                res = min(res, r - l + 1)
                curr -= nums[l]
                # move left of window towards right
                l += 1

        return res if res <= len(nums) else 0

    # O(nlogn) - followup
    # we can't sort and calc min length from right end
    # because since subarray needs to be contigous and after sorting we may loose original order
    def minSubArrayLen_NLOGN(self, s:int, nums: List[int]) -> int:
        if not nums:
            return 0

        sums = [0]
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            sums.append(curr)

        ans = []

        for i in range(len(nums)):
            left = i
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if sums[mid+1] - sums[i] >= s:
                    ans.append(mid-i)
                    right = mid-1
                else:
                    left = mid + 1

        return min(ans)+1 if len(ans) > 0 else 0



if __name__ == "__main__":

    assert Solution().minSubArrayLen(7, [2,3,1,2,4,3]) == 2
    assert Solution().minSubArrayLen_NLOGN(7, [2,3,1,2,4,3]) == 2

