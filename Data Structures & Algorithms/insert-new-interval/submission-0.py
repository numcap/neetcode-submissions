class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i, n = 0, len(intervals)
        def merge(a,b):
            return [min(a[0], b[0]), max([a[1], b[1]])]
        
        def is_overlapping(a,b):
            return a[0] <= b[1] and b[0] <= a[1]

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1
        
        while i < n and is_overlapping(intervals[i], newInterval):
            newInterval = merge(intervals[i], newInterval)
            i += 1
        res.append(newInterval)
        
        while i < n:
            res.append(intervals[i])
            i+=1
        
        return res
