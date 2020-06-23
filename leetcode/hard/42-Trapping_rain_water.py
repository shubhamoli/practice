"""
    Leetcode #42
"""


from typing import List


class Solution:
    def trap_BF(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0
        N = len(height)

        for i in range(N):
            l_max = 0
            r_max = 0
            for j in range(i, -1, -1):
                l_max = max(l_max, height[j])

            for j in range(i, N):
                r_max = max(r_max, height[j])

            res += min(l_max, r_max) - height[i]


        return res

    # basically, storing left_max and right_max
    # to avoid computing them for every i
    def trap_DP(self, height: List[int]) -> int:
        if not height:
            return 0

        N = len(height)

        l_max = [0] * N
        l_max[0] = height[0]
        for i in range(1, N):
            l_max[i] = max(height[i], l_max[i-1])

        r_max = [0] * N
        r_max[N-1] = height[N-1]
        for i in range(N-2, -1, -1):
            r_max[i] = max(height[i], r_max[i+1])


        res = 0
        for i in range(N):
            res += min(l_max[i], r_max[i]) - height[i]


        return res


    def trap_STK(self, height: List[int]) -> int:
        if not height:
            return 0

        N = len(height)

        res = 0
        i = 0

        stk = []
        for i in range(N):
            # keeping adding element till larger bar is not found
            while stk and height[stk[-1]] < height[i]:
                top = stk[-1]
                stk.pop()
                if not stk:
                    break

                dis = i - stk[-1] - 1
                bounded_height = min(height[i], height[stk[-1]]) - height[top]

                res += bounded_height * dis

            stk.append(i)

        return res

    def trap_2Pointer(self, height: List[int]) -> int:
        if not height:
            return 0

        N = len(height)

        lp = 0
        rp = N-1

        res = 0
        left_max = height[0]
        right_max = height[N-1]

        while lp < rp:
            if height[lp] < height[rp]:
                if height[lp] >= left_max:
                    left_max = height[lp]
                else:
                    res += left_max - height[lp]
                lp += 1
            else:
                if height[rp] >= right_max:
                    right_max = height[rp]
                else:
                    res += right_max - height[rp]
                rp -= 1

        return res






if __name__ == "__main__":

    solution = Solution()

    assert solution.trap_BF([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert solution.trap_DP([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert solution.trap_2Pointer([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert solution.trap_STK([0,1,0,2,1,0,1,3,2,1,2,1]) == 6

