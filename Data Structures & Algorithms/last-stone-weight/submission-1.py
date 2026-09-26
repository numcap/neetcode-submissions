class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]  # for max heap
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            diff = 0
            if x > y:
                diff = x - y
            elif y > x:
                diff = y - x

            if diff != 0:
                heapq.heappush(stones, -diff)
        
        return -stones[0] if len(stones) > 0 else 0

