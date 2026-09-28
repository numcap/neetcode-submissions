class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [-val for val in counter.values()]
        heapq.heapify(heap)
        time = 0
        q = deque()

        while heap or q:
            time += 1
            if not heap:
                time = q[0][0]
            else:
                most_freq = heapq.heappop(heap)
                most_freq += 1
                if most_freq:
                    q.append((time + n, most_freq))

            if q and q[0][0] == time:
                heapq.heappush(heap, q[0][1])
                q.popleft()
        return time
