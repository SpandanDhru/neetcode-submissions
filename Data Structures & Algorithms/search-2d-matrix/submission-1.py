class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = []

        for row in matrix:
            if target < row[0] or target > row[len(row) - 1]:
                continue
            elif target == row[0] or target == row[len(row) - 1]:
                return True
            else:
                target_row = row
        
        l = 0
        r = len(target_row) - 1
        
        while l <= r:
            m = l + ((r - l) // 2)

            if target_row[m] > target:
                r = m - 1
            elif target_row[m] < target:
                l = m + 1
            else:
                return True
        
        return False
        