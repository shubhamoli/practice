"""
    Leetcode #754
"""


class Solution:
    # 1+2+3=6 ( So, 4 is Over ) Now , just think that we can surely make this equation
    # to form 4 by flipping 1 to (-1) , So then summation will be 6-(1+1)==4.
    # So, assumption is when we flip a number(here 1) then we have to subtract that number
    # from the summation (here 6) twice( Here 6-(1+1)==4 ) . So , from here what we
    # can observe that as for flipping we have to subtract twice of some number from summation.
    # So, obviously we are subtracting even number ( Here we are flipping 1 , So we have to
    # subtract (1+1) which is even from summation 6 ) and finally we can reach goal target 4.
    def reachNumber(self, target: int) -> int:
        step = 0
        _sum = 0
        target = abs(target)
        while True:
            step += 1
            _sum += step
            if _sum == target:
                return step

            if _sum > target and (_sum-target) % 2 == 0:
                return step



if __name__ == "__main__":

    solution = Solution()

    assert solution.reachNumber(3) == 2 # 0 (1) -> 1 (2) -> 3
    assert solution.reachNumber(2) == 3 # 0 (1) -> 1 (-2) -> -1 (3) -> 2
