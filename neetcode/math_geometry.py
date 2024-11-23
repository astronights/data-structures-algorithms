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
        
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		'''Spiral matrix numbers

  		Space Complexity: O(m * n) -> Output values
    		Time Complexity: O(m * n) -> Matrix traversal

      		Values: Matrix dimensions (m x n)

 		Args:
   			matrix (list): Matrix of values

      		Returns:
			out (list): List of spiral values
   		'''
        	out = []
        	dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        	R, C = len(matrix), len(matrix[0])
        	x, y, c = 0, -1, 0

        	while len(out) < R * C:
            		dx, dy = dirs[c]
            		x, y = x + dx, y + dy
            		
			out.append(matrix[x][y])
            		matrix[x][y] = None

            		nx, ny = x + dx, y + dy
            		if nx < 0 or nx >= R or ny < 0 or ny >= C or matrix[nx][ny] is None:
                		c = (c + 1) % 4
        	return out
