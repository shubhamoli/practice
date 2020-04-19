"""
    1.7 - Rotate an image matrix of size NXN by 90 degree
          Do rotation in-place
"""


from typing import List


# in-place rotation
# assuming clockwise 90 degree rotation
def rotate(image: List[List[int]]) -> List[List[int]]:

    N = len(matrix)
    C = len(matrix[0])

    if N != C:
        raise Exception("Not a square martix")

    for i in range(N):
        for j in range(i, N):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp


    for i in range(N):
        for j in range(N//2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][N-j-1]
            matrix[i][N-j-1] = temp

    return matrix


if __name__ == "__main__":

    # 2X2
    matrix = [[1, 2],
              [3, 4]]
    output = [[3, 1],
              [4, 2]]

    assert rotate(matrix) == output

    # 3X3
    matrix = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    output = [[7, 4, 1],
              [8, 5, 2],
              [9, 6, 3]]

    assert rotate(matrix) == output

    # 4 X4
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    output = [[13, 9, 5, 1],
              [14, 10, 6 ,2],
              [15, 11, 7, 3],
              [16, 12, 8, 4]]

    assert rotate(matrix) == output
