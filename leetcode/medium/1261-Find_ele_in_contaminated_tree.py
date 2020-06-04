"""
    Leetcode #1261
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

        def __init__(self, root: TreeNode):
            self._set = set()
            self._root = self._recover(root, 0)

        def find(self, target: int) -> bool:
            q = [self._root]

            # this time let's go BFS
            while q:
                N = len(q)
                for i in range(N):
                    tmp = q.pop(0)
                    if tmp.val == target:
                        return True

                    if tmp.left:
                        q.append(tmp.left)

                    if tmp.right:
                        q.append(tmp.right)

            return False

        # using extra memory
        def find_OPTI(self, target: int) -> bool:
            return target in self._set

        def _recover(self, root, v):
            if not root:
                return

            self._set.add(v)    # for finding in O(1)
            root.val = v

            self._recover(root.left, 2 * v + 1)
            self._recover(root.right, 2 * v + 2)


if __name__ == "__main__":

