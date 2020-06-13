"""
    Leetcode #575
"""


from typing import List

class Solution:
    def distributeCandies_OPTI(self, candies: List[int]) -> int:
        unique = set(candies)

        # max number of candies sister can get will be atmost len(candies) / 2
        if len(unique) >= len(candies) // 2:
            return len(candies) // 2
        else:
            return len(unique)

    def distributeCandies(self, candies: List[int]) -> int:

        count = 0
        N = len(candies)

        for i in range(N//2):
            # max number of candies sister can get will be atmost len(candies) / 2
            if count >= N // 2:
                break

            if candies[i] != float("-inf"):
                count += 1
                for j in range(i+1, N):
                    if candies[i] == candies[j]:
                        candies[j] == float("-inf")

        return count


if __name__ == "__main__":

    solution = Solution()

    assert solution.distributeCandies([1,1,2,2,3,3]) == 3
    assert solution.distributeCandies([1,1,2,3]) == 2

    assert solution.distributeCandies_OPTI([1,1,2,2,3,3]) == 3
    assert solution.distributeCandies_OPTI([1,1,2,3]) == 2

