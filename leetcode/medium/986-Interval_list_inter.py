"""
    Leetcode #986
"""

from typing import List

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []

        m, n = len(A), len(B)
        i = j = 0
        res = []

        while i < m and j < n:
            if A[i][1] >= B[j][0] and A[i][0] <= B[j][1]:
                # see diagram for this
                res.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res


if __name__ == "__main__":

    solution = Solution()

    A = [[0,2],[5,10],[13,23],[24,25]]
    B = [[1,5],[8,12],[15,24],[25,26]]

    print(solution.intervalIntersection(A, B))  # [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

