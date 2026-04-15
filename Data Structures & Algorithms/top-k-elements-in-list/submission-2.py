class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        so given k we want to find the k most frequent numbers
        we can start by counting all the occurances and put that into a hashmap,
        then we can use max on the values that are in a list
        """

        count = {}
        maximum = 0
        for num in nums:
            count[num] = count.get(num, 0) + 1
            maximum = max(maximum, count[num])
        
        vals = list(count.values())
        
        buckets = [[] for _ in range(maximum)]

        for val, cnt in count.items():
            buckets[cnt-1].append(val)
        
        res = []
        
        for i in range(len(buckets)-1, -1, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res


            # if len(buckets[-1]) >= k:
            #     return buckets[-1][-1:k-1:-1]
            # res.append(buckets[-i-1][0])

        return res
            
