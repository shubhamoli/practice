"""
    Leetcode #73
"""


from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        m = len(matrix)
        n = len(matrix[0])

        aux = [[0]*n for x in range(m)]
        # aux_rows = [0]*m
        # aux_cols = [0]*n

        # record position of 0 in aux matrix
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    aux[i][j] = -1

        # check for -1 in aux and if found make entire row and col 0
        # O(n^3)
        for i in range(m):
            for j in range(n):
                if aux[i][j] == -1:
                    for k in range(n):
                        matrix[i][k] = 0
                    for l in range(m):
                        matrix[l][j] = 0

        print(matrix)

    # O(n^2) solution
    def setZeroes_OPTI(self, matrix: List[List[int]]) -> None:

        if not matrix:
            return None

        m = len(matrix)
        n = len(matrix[0])

        aux_rows = [0]*m
        aux_cols = [0]*n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    aux_rows[i] = -1
                    aux_cols[j] = -1

        for i in range(len(aux_rows)):
            if aux_rows[i] == -1:
                for k in range(n):
                    matrix[i][k] = 0

        for j in range(len(aux_cols)):
            if aux_cols[j] == -1:
                for l in range(m):
                    matrix[l][j] = 0

        print(matrix)



if __name__ == "__main__":

    solution = Solution()

    m1 = [[0,1,2,0], [3,4,5,2], [1,3,1,5]]
    # need new copy as above one will be modifeed by func
    # also m1[:] doesn't work for 2-D
    m2 = [[m1[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
    m3 = [[1,1,1], [1,0,1], [1,1,1]]
    # same here
    m4 = [[m3[i][j] for j in range(len(m3[0]))] for i in range(len(m3))]

    solution.setZeroes(m1)
    solution.setZeroes_OPTI(m2)

    solution.setZeroes(m3)
    solution.setZeroes_OPTI(m4)

