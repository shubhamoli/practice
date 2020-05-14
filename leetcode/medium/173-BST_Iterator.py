"""
    Leetcode #173
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator():

    def __init__(self, root: TreeNode):
        if node is None:
            return iter([])

        yield from self._generator(node.left)
        yield node.val
        yield from self._generator(node.right)
        self.node = root
        self._node_itr = self._generator(root)
        self._next = next(self._node_itr, None)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        _next = self._next
        self._next = next(self._node_itr, None)
        return _next

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self._next is not None

    def _generator(self, node):
        if node is None:
            return iter([])

        yield from self._generator(node.left)
        yield node.val
        yield from self._generator(node.right)


if __name__ == "__main__":

    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    itr = BSTIterator(root)

    assert itr.next() == 3
    assert itr.next() == 7
    assert itr.hasNext() == True
    assert itr.next() == 9
    assert itr.hasNext() == True
    assert itr.next() == 15
    assert itr.hasNext() == True
    assert itr.next() == 20
    assert itr.hasNext() == False

