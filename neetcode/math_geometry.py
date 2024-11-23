# Math & Geometry Solutions

class Solution:
	# Solution Functions

	def rotate(self, matrix: List[List[int]]) -> None:
		'''Rotate Matrix

  		Space Complexity: O(n) -> Row reverse temporary list
    		Time Complexity: O(n ^ 2) -> Transpose

      		Args:
			matrix (list): Matrix
   		'''
        	for i in range(len(matrix)):
            		for j in range(i):
                		matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        	for i in range(len(matrix)):
            		matrix[i] = matrix[i][::-1]
        
