"""
    1.8 - Write an algorithm such that if in an element in MxN matrix is 0
          All elements in that row become should become 0
"""


from typing import List


# assuming all element in matrix are >= 0
def algo(matrix: List[List[int]]) -> List[List[int]]:
    M = len(matrix)
    N = len(matrix[0])

    # mark location as -1 when element at this location is 0
    # O(MN)
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                matrix[i][j] = -1

    # now whenever -1 is found, replace all entire elements
    # in that row and col to 0
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == -1:
                # Zero entire col
                for k in range(N):
                    matrix[i][k] = 0

                # Zero entire row
                for l in range(M):
                    matrix[l][j] = 0

    return matrix


# It works for all integers
def algoOptimized(matrix: List[List[int]]) -> List[List[int]]:

    def nullifyRow(matrix, rowNum):
        for i in range(len(matrix[rowNum])):
            matrix[rowNum][i] = 0
        return matrix

    def nullifyCol(matrix, colNum):
        for i in range(len(matrix)):
            matrix[i][colNum] = 0
        return matrix

    M = len(matrix)
    N = len(matrix[0])

    rows = M*[0]
    cols = N*[0]

    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                rows[i] = 1
                cols[j] = 1

    for i in range(len(rows)):
        if rows[i]: nullifyRow(matrix, i)

    for j in range(len(cols)):
        if cols[j]: nullifyCol(matrix, j)

    return matrix


if __name__ == "__main__":

    matrix1 = [[1, 2, 3],
               [0, 5, 6],
               [7, 8, 0]]
    output = [[0, 2, 0],
              [0, 0, 0],
              [0, 0, 0]]

    assert algo(matrix1) == output


    matrix2 = [[1, 2, 3],
               [0, 5, 6],
               [7, 8, 0]]
    output = [[0, 2, 0],
              [0, 0, 0],
              [0, 0, 0]]
    assert algoOptimized(matrix2) == output

