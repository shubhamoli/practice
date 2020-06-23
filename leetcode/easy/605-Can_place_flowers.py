"""
    Leetcode #605
"""


from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not flowerbed:
            return False

        # the idea here is check for 0 and if left and right of 0 are also 0 
        # then plant
        N = len(flowerbed)
        i = 0
        count = 0
        while i < N:
            if (flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == N - 1 or flowerbed[i+1] == 0)):
                flowerbed[i] = 1
                count += 1

            if count >= n:
                return True

            i += 1

        return False



if __name__ == "__main__":

    solution = Solution()

    assert solution.canPlaceFlowers([1,0,0,0,1], 1) == True
    assert solution.canPlaceFlowers([1,0,0,0,1], 2) == False

