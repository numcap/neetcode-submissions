class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # build the max heap
        heap = []
        heapq.heapify(heap)
        for point in points:
            x, y = point[0], point[1]
            distance = (x**2 + y**2) ** 0.5
            heapq.heappush(heap, (distance, point))

        return [heapq.heappop(heap)[1] for i in range(k)]
