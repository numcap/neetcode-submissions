class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        problem: we need to find the mimimum bph (bannas/hour) that the monkey
        can eat under or equal to the time we have in hours (h), once the monkey
        starts eating a pile he takes the bph time to eat it even if its less
        bananas then the pile

        potential solution: we know that the minimum value of hours is the length
        of the piles array, meaning that the high end of possibilities for k is
        the max value of bananas at the biggest pile, so we can actually perform
        a binary search on an array that is between 1 and the largest pile
        to find the most optimal bph
        """

        piles.sort()

        l, r = 1, piles[-1]

        res = 0

        while l <= r:
            mid = (l + r) // 2  # this is the k value here

            curr_hours = 0
            for pile in piles:
                curr_hours += math.ceil(pile / mid)

            if curr_hours > h:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        
        return res

