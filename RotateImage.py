from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrixOrder = len(matrix)
        end = matrixOrder - 1
        for i in range(0 ,matrixOrder // 2):
            innerMatrixEnd = end - i
            for j in range(0, innerMatrixEnd - i):
                # A B
                # C D
                # temp is B
                temp = matrix[i + j][end - i]
                # change B with A
                matrix[i + j][end - i] = matrix[i][i + j]
                # change A with D
                matrix[i][i + j] = matrix[end - j - i][i]
                # change D with C
                matrix[end -j - i][i] = matrix[end - i][end - j - i]
                # change C with temp
                matrix[end - i][end - j - i] = temp
                
if __name__ == "__main__":
    solution = Solution()
    solution.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    solution.rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    solution.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])

