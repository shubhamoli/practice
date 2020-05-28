"""
    Leetcode #373
"""


from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        res = []

        # insert (i, 0), (i+1, 0), (i+n, 0) in heap
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(len(nums1))]

        while heap and k > 0:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))

            k -= 1

        return res



if __name__ == "__main__":

    solution = Solution()

    print(solution.kSmallestPairs([1,7,11], [2,4,6], 3))        # [[1,2],[1,4],[1,6]]
    print(solution.kSmallestPairs([1,1,2], [1,2,3], 2))     # [1,1],[1,1]
