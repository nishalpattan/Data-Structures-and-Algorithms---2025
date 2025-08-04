# Last updated: 8/3/2025, 9:01:59 PM
class UndergroundSystem:

    def __init__(self):
        self.check_in = dict()
        self.travel_time = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_stn, start_time = self.check_in[id]
        start_to_dest = start_stn + "_" + stationName
        time = t - start_time
        if start_to_dest in self.travel_time:
            self.travel_time[start_to_dest][0] += time
            self.travel_time[start_to_dest][1] += 1
            
        else:
            self.travel_time[start_to_dest] = [time, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        start_to_dest = startStation + "_" + endStation
        return self.travel_time[start_to_dest][0] / self.travel_time[start_to_dest][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)