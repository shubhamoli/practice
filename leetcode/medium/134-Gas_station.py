"""
    Leetcode #134
"""


from typing import List


class Solution:
    def canCompleteCircuit_BF(self, gas, cost) -> int:
        if sum(gas) < sum(cost):
            return -1

        N = len(gas)

        station = -1
        totalGas = 0

        # O(N^2)
        for i in range(N):
            totalGas = gas[i]
            success = False
            j = i

            # for each i check whether trip can be completed
            while j < len(gas):
                if totalGas >= cost[j]:
                    totalGas -= cost[j]
                else:
                    break

                # for circular movement
                if j+1 == len(gas):
                    j = 0
                else:
                    j += 1

                # refill
                totalGas += gas[j]

                # Trip complete
                if i == j:
                    success = True
                    break

            if success:
                return i

        return -1


    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas or not cost:
            return -1

        if len(gas) != len(cost):
            return -1

        N = len(gas)

        curr = 0
        station = 0
        total = 0

        for i in range(N):
            curr += (gas[i] - cost[i])
            total += (gas[i] - cost[i])

            if curr < 0:
                station = i + 1
                curr = 0

        return station if total >=0 else -1


if __name__ == "__main__":

    solution = Solution()

    gas  = [1,2,3,4,5]
    cost = [3,4,5,1,2]

    assert solution.canCompleteCircuit_BF(gas, cost) == 3

    gas  = [2,3,4]
    cost = [3,4,3]

    assert solution.canCompleteCircuit(gas, cost) == -1
