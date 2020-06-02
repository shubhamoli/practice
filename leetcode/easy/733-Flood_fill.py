"""
    Leetcode #733
"""


from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return []

        if not image[0]:
            return []

        M = len(image)
        N = len(image[0])

        originalColor = image[sr][sc]

        def helper(r, c):
            if r < 0 or r >= M or c < 0 or c >=N:
                return

            if image[r][c] == newColor or originalColor != image[r][c]:
                return

            image[r][c] = newColor

            helper(r-1, c)
            helper(r+1, c)
            helper(r, c-1)
            helper(r, c+1)


        helper(sr, sc)
        return image


if __name__ == "__main__":

    image = [ [1,1,1],
              [1,1,0],
              [1,0,1]]

    # print(Solution().floodFill(image, 1, 1, 2))

    image = [[0,0,0],
             [0,1,1]]

    print(Solution().floodFill(image, 1, 1, 1))

