"""
    Leetcode #223
"""


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        # compute invidiual area
        # and then subtract overlapping area
        Area_A = (C-A) * (D-B)
        Area_B = (G-E) * (H-F)

        l = max(A, E)
        r = min(C, G)

        b = max(B, F)
        t = min(D, H)

        overlap = 0
        if l < r and t > b:
            overlap = (r - l) * (t - b)

        return Area_A + Area_B - overlap


if __name__ == "__main__":

    assert Solution().computeArea(A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2) == 45
