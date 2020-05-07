"""
    Leetcode #117
"""



# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # Skipping queue based level-order traversal
    # as it is not in constant space
    #
    # and implicit stack of recursion is ignored
    # see folloup in problem statement
    def connect_constant_space(self, root: Node) -> Node:

        if not root:
            return None

        def helper(root):
            if not root:
                return

            if root.left:
                root.left.next = root.right

            tmp = root.right or root.left

            # this is done to handle
            # empty nodes
            if tmp:
                next = root.next

                while next:
                    if next.left:
                        tmp.next = next.left
                        tmp = tmp.next
                    if next.right:
                        tmp.next = next.right
                        tmp = tmp.next

                    next = next.next

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
