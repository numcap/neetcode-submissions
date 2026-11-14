"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        |-----|
                |------|
            |-----|
        """

        start_arr = sorted([i.start for i in intervals])
        end_arr = sorted([i.end for i in intervals])

        start = end = 0
        count = 0
        res = 0

        while start < len(start_arr):
            if start_arr[start] < end_arr[end]:
                count += 1
                start += 1
            else:
                count -= 1
                end += 1
            res = max(count, res)
        
        return res