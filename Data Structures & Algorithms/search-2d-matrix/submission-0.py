class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        problem: so we need to search a 2D matrix to see if our target is in this
        matrix

        potential solution: obviously we can do a brute force with a nested for loop
        we can also do a binary search since the arrays are already sorted.
        what i am thinking is since the numbers are sorted and carry on we can 
        perform a binary search on the first elements of the array, this will tell
        us what target the array will be in, then we can perform a binary search 
        through that array 
        
        notes: we can always perform a binary search on a sorted array
        """

        l, r = 0, len(matrix) - 1

        arrayNum = -1

        while l <= r:
            mid = (l + r) //2

            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                arrayNum = mid
                break


        if arrayNum == -1: return False

        l, r = 0, len(matrix[arrayNum]) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if matrix[arrayNum][mid] > target:
                r = mid -1
            elif matrix[arrayNum][mid] < target:
                l = mid +1
            else:
                return True
        return False



