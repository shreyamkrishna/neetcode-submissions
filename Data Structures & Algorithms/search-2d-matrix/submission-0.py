class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        l,r= 0, rows*columns-1

        while l<=r:
            mid = (l + r)//2
            row = mid //columns
            column = mid % columns
            if matrix[row][column]>target:
                r = mid -1
            elif matrix[row][column]<target:
                l = mid +1
            else:
                return True
        return False

