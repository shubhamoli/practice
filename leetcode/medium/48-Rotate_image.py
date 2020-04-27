"""
    Leetcode #48
"""


class Solution:
    def rotate(self, matrix: List{List[int]}) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        N = len(matrix)
        for i in range(N//2):
            first = i
            last = N - 1 - i
            for j in range(first, last):
                offset = j - first

                top = matrix[first][j]
                matrix[first][j] = matrix[last-offset][first]
                matrix[last-offset][first] = matrix[last][last-offset]
                matrix[last][last-offset] = matrix[j][last]
                matrix[j][last] = top

    def rotate_OPTIM(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(N):
            for j in range(i, N):

                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        for i in range(N):
            for j in range(N//2):

                matrix[i][j], matrix[i][N-j-1] = matrix[i][N-j-1], matrix[i][j]



if __name__ == "__main__":

    print(Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
