"""
    Leetcode #946
"""


from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []

        # just simulating the desired behaviour
        i = 0
        for ele in pushed:
            stk.append(ele)
            while stk and stk[-1] == popped[i]:
                stk.pop()
                i += 1

        return len(stk) == 0


if __name__ == "__main__":

    solution = Solution()

    assert solution.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]) == True
    assert solution.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]) == False
