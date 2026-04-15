class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        what we want to do is find 3 numbers that add up to 0

        potential solution: first we need to sort the array because what we will 
        do is choose a pivot and create a Left and Right pointer similar to 2 
        sum two where if the sum of the pivot and L and R is greater than the
        target (0) then we will move the R to the left and vice versa when 
        the sum is less than the target (0)
        """


        nums = sorted(nums)
        ans = []

        for index, pivot in enumerate(nums):
            if pivot > 0: break
            if index > 0 and nums[index-1] == pivot: continue

            L = index+1
            R = len(nums) -1

            while L < R:
                three_sum = pivot + nums[L] + nums[R]
                if three_sum < 0:
                    L += 1
                elif three_sum > 0:
                    R -= 1
                else:
                    ans.append([pivot, nums[L], nums[R]])
                    L+=1

                    while nums[L] == nums[L-1] and L < R:
                        L+=1
        
        return ans


