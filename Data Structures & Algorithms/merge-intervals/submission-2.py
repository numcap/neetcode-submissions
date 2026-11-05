class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        res = []
        i, n = 0, len(intervals)
        intervals.sort()

        """
        intervals=[[1,4],[0,2],[3,5]]
        intervals=[[0,2],[1,4],[3,5]]
        res = [0,4],[1,5]

        """

        def merge_together(a, b):
            return [min(a[0], b[0]), max(a[1], b[1])]

        def overlap(a, b):
            return a[0] <= b[1] and b[0] <= a[1]

        while i < n:
            # print(i, res)
            # if i + 1 < n :print(intervals[i], intervals[i + 1])
            if i - 1 >= 0 and overlap(intervals[i], res[- 1]):
                res[-1] = merge_together(intervals[i], res[- 1])
            else:
                res.append(intervals[i])
            i += 1

        return res
