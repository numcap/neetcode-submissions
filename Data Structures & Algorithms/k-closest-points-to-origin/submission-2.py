class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # build min heap with (distance, [x,y])
        heap = [((point[0] ** 2 + point[1] ** 2), point) for point in points]

        heapq.heapify(heap)

        # pop k from min heap to find closest
        return [heapq.heappop(heap)[1] for i in range(k)]
