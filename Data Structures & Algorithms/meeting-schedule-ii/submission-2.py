"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        minRooms = 0
        occupiedRooms = []

        intervals.sort(key=lambda x:x.start)

        for interval in intervals:
            while occupiedRooms and occupiedRooms[0] <= interval.start:
                heapq.heappop(occupiedRooms)

            heapq.heappush(occupiedRooms, interval.end)

            minRooms = max(minRooms, len(occupiedRooms))

        return minRooms



