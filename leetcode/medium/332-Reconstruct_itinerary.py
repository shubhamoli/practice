"""
    Leetcode #332
"""


from typing import List
from collections import defaultdict, deque


# https://en.wikipedia.org/wiki/Eulerian_path
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        routes = defaultdict(list)

        for u, v in tickets:
            routes[u].append(v)

        # for lexical order
        for route in routes:
            routes[route] = deque(sorted(routes[route]))

        itinerary = []

        def helper(node):
            while routes[node]:
                to = routes[node].popleft()
                helper(to)
            itinerary.append(node)

        helper("JFK")

        return itinerary[::-1]




if __name__ == "__main__":

    solution = Solution()

    # ["JFK", "MUC", "LHR", "SFO", "SJC"]
    print(solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))

    # ["JFK","ATL","JFK","SFO","ATL","SFO"]
    print(solution.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
