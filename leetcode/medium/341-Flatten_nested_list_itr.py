"""
    Leetcode #341
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#       """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._peek = None
        def gen(nestedList):
            for x in nestedList:
                if x.isInteger():
                    yield x
                else:
                    for y in gen(x.getList()):
                        yield y

        self._list = gen(nestedList)

    def next(self) -> int:
        return self.value

    def hasNext(self) -> bool:
        try:
            self.value = next(self.gen)
            return True
        except StopIteration:
            return False

# Your NestedIterator object will be instantiated and called as such:
