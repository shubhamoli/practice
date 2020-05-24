"""
    Leetcode #334
"""


from typing import List
import bisect

# Your algorithm should run in O(n) time complexity
# and O(1) space complexity.
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums:
            return False

        # hardcoding k = 3 in general solution
        k = 3
        inc = [float('inf')] * (k - 1)

        for x in nums:
            # find position/index for x in "inc" array
            i = bisect.bisect_left(inc, x)

            # if i >= k-1 (in our case index 2)
            # means we have inserted 3 increasing numbers
            # so we're done
            if i >= k - 1:
                return True

            inc[i] = x

        # return True if k == 0
        # else return False (always)
        return k == 0




if __name__ == "__main__":

    solution = Solution()

    assert solution.increasingTriplet([1,2,3,4,5]) == True
    assert solution.increasingTriplet([5,4,3,2,1]) == False
