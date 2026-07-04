class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        left, right = 0, m

        found_row = False
        row_index = 0

        while left <= right and not found_row:
            mid = left + ((right - left) // 2)

            if matrix[mid][0] <= target <= matrix[mid][n]:
                row_index = mid
                found_row = True
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1

        return (target in matrix[row_index])
