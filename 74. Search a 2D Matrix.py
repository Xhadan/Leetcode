class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m = len(matrix)     # Number of rows
        n = len(matrix[0])  # Number of columns
        
        # Binary search on a "virtual" 1D array from 0 to (m*n - 1)
        l, r = 0, (m * n) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            # Map the 1D mid index to 2D (row, col) coordinates
            row = mid // n
            col = mid % n
            
            if matrix[row][col] == target:
                return True
            
            if target < matrix[row][col]:
                r = mid - 1
            else:
                l = mid + 1
                
        return False