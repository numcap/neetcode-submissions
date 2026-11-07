class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()

        def is_overlapping(a,b):
            return a[0] < b[1] and b[0] < a[1]
        
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res +=1
                prevEnd = min(end, prevEnd)
        return res
