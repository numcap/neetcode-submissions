"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        def overllaping(a: Interval,b: Interval):
            return a.start < b.end and b.start < a.end

        intervals = sorted(intervals, key=lambda interval: interval.start)
        n = len(intervals)
        res = True

        for i in range(n):
            if i + 1 < n and overllaping(intervals[i], intervals[i + 1]):
                res = False
                break
        
        return res