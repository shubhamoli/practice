"""
    Leetcode #133
"""


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    visited = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        if node in self.visited:
            return self.visited[node]

        newNode = Node(node.val)
        self.visited[node] = newNode

        for connection in node.neighbors:
            if connection in self.visited:
                newNode.neighbors.append(self.visited[connection])
            else:
                newNode.neighbors.append(self.cloneGraph(connection))

        return newNode



if __name__ == "__main__":

    Solution().cloneGraph([[2,4],[1,3],[2,4],[1,3]])
    Solution().cloneGraph([[]])
    Solution().cloneGraph([])
    Solution().cloneGraph([2],[1])


