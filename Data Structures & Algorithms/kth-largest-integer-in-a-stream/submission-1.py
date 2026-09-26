class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-num for num in nums]
        heapq.heapify(self.heap)
        self.k  = k
        
        

    def add(self, val: int) -> int:
        arr = []
        heapq.heappush(self.heap, -val)
        for i in range(self.k):
            arr.append(heapq.heappop(self.heap))
        
        print(arr)
        
        ans = -arr[len(arr) - 1]

        for num in arr:
            heapq.heappush(self.heap, num)
        
        return ans

