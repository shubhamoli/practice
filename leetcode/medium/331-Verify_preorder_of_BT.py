"""
    Leetcode #331
"""


from collections import deque


# Note: we don't have to re-construct tree
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        pre = deque(preorder.split(","))

        def helper(nodes):
            if not nodes:
                return False

            val = nodes.popleft()
            if val == "#":
                return True

            left = helper(nodes)
            right = helper(nodes)

            return left and right

        return helper(pre) and len(pre) == 0


if __name__ == "__main__":

    solution = Solution()

    assert solution.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#") == True
    assert solution.isValidSerialization("1,#") == False
    assert solution.isValidSerialization("9,#,#,1") == False

