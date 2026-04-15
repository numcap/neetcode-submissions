class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        problem: we need to return the max area that is possible by picking 2 
        heights and returning min(height1, height2) * distance between 
        height1 and height 2 indicies

        potential solution: so we can do a brute force method which would involve
        interating over the array twice causing O(n), we might be able to do a
        2 pointer approach with L and R pointers on each side, 
        """

        # maxArea = -1

        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         area = min(heights[i], heights[j]) * (j - i)
        #         maxArea = max(area, maxArea)
        
        # return maxArea

        maxArea = -1

        L = 0
        R = len(heights)-1

        while L < R:
            area = min(heights[L], heights[R]) * (R - L)
            maxArea = max(area, maxArea)
            if heights[L] > heights[R]:
                R -=1
            else:
                L +=1
        return maxArea
            
