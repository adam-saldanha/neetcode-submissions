"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappop, heappush  # Use a min-heap for room end times.
from typing import List  # Provide the type annotation.

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval:interval.start)
        room_ends = []

        for interval in intervals:
            if room_ends and room_ends[0] <= interval.start:
                heappop(room_ends)
            heappush(room_ends, interval.end)

        return len(room_ends)
        