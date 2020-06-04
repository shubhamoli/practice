"""
    Leetcode #1396
"""


from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.transit = defaultdict(list)
        self.dest = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.transit[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.transit[id]
        route = (startStation, stationName)
        self.dest[route].append(t - startTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return sum(self.dest[route])/len(self.dest[route])


if __name__ == "__main__":

    # Your UndergroundSystem object will be instantiated and called as such:
    obj = UndergroundSystem()

    obj.checkIn(5,"A",8)
    obj.checkIn(6,"A",8)
    obj.checkOut(5,"C",10)
    obj.checkOut(6,"D",11)

    assert  obj.getAverageTime("A","C") == 2
