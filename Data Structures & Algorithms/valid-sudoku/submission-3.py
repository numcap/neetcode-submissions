class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        """
        we need to check every column, row and 3x3 grid for duplicates, and return true if there aren't
        duplicates and false if there are

        potential solution: brute force could mean we check every single row, column, and 3x3 grid with 
        for loops, but there may be a better option im not thinking of
        """

        # for rows
        for row in board: # O(1) constant time because set length of 9
            seen = set()
            for item in row:
                if item != "." and item in seen:
                    return False
                else:
                    seen.add(item)
            
        # for columns
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] != "." and board[j][i] in seen:
                    return False
                else:
                    seen.add(board[j][i])

        # for 3x3 grids
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                seen_in_3x3 = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        # print(board[i][j])
                        if board[i][j] != "." and board[i][j] in seen_in_3x3:
                            return False
                        else:
                            seen_in_3x3.add(board[i][j])

        return True
