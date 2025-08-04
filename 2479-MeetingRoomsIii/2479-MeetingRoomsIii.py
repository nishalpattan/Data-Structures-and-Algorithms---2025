# Last updated: 8/3/2025, 9:01:51 PM
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        count_rooms = [0] * n
        free_rooms = list(range(n))  # min heap of room numbers
        heapq.heapify(free_rooms)
        max_occupancy = float("-inf")
        meetings.sort()


        busy_rooms = list()  # min heap of (end_time, room)

        for meeting in meetings:
            start = meeting[0]
            end = meeting[1]

            # make busy rooms free and add room to free_rooms list
            while busy_rooms and  busy_rooms[0][0] <=start:
                end_time, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)

            if free_rooms:
                # remove earliest free room from from free_rooms min heap and add to busy rooms
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room))
                count_rooms[room] += 1

            else:
                # add new end time for earliest room in busy_rooms
                earliest_end_time, room = heapq.heappop(busy_rooms)
                heapq.heappush(busy_rooms, (earliest_end_time + end - start, room))
                count_rooms[room] += 1
        
        max_occupancy = max(count_rooms)
        for room, occupancy in enumerate(count_rooms):
            if occupancy ==  max_occupancy:
                return room
