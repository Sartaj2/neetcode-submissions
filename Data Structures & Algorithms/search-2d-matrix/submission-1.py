class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row, cols = len(matrix), len(matrix[0])
        l, r = 0, row*cols - 1
        while l <= r:
            mid = l + (r - l) // 2
            mid_row = mid // cols
            mid_col = mid % cols
            mid_val = matrix[mid_row][mid_col]
            if mid_val == target:
                return True
            elif target < mid_val:
                r = mid - 1
            else:
                l = mid+ 1
        return False