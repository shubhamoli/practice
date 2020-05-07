"""
    Leetcode #116
"""


from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return None

        q = []
        q.append(root)

        while q:
            size = len(q)
            prev = None

            for i in range(size):
                curr = q.pop(0)
                curr.next = None

                # addition to level order traversal
                if prev:
                    prev.next = curr

                prev = curr

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return root

    # implicit stack of recursion is ignored
    # see folloup in problem statement
    def connect_constant_space(self, root: Node) -> Node:

        if not root:
            return None

        def helper(root):
            if not root:
                return

            if root.left:
                root.left.next = root.right

            if root.next and root.right:
                if root.next.left:
                    root.right.next = root.next.left
                elif root.next.right:
                    root.right.next = root.next.right

            helper(root.left)
            helper(root.right)

        helper(root)
        return root



if __name__ == "__main__":

    """
    Tree
            1
           / \
          /   \
         2     3
        / \   / \
       4   5 6   7
    """

    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(Solution().connect(root))
