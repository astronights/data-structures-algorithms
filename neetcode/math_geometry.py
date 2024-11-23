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

	def setZeroes(self, matrix: List[List[int]]) -> None:
		'''Set Matrix Zeroes

  		Space Complexity: O(1) -> Constant space
    		Time Complexity: O(m * n) -> Matrix dimensions

      		Values: Matrix dimensions (m x n)

      		Args:
			matrix (list): Matrix
   		'''
        	first = False
        	R, C = len(matrix), len(matrix[0])

        	for i in range(R):
            		for j in range(C):
                		if matrix[i][j] == 0:
                    			matrix[0][j] = 0
                    			if i > 0:
                        			matrix[i][0] = 0
                    			else:
                        			first = True
        
        	for i in range(1, R):
            		for j in range(1, C):
                		if matrix[i][0] == 0 or matrix[0][j] == 0:
                    			matrix[i][j] = 0

        	if matrix[0][0] == 0:
            		for i in range(R):
                		matrix[i][0] = 0

        	if first:
            		matrix[0] = [0] * C

	def isHappy(self, n: int) -> bool:
		'''Happy (Non-Cyclical) Number

  		Space Complexity: O(n) -> Hash Set
		Time Comeplexity: O(n) -> Iteration

  		Values: Numbers on the cyclical path (n)

    		Args:
      			n (int): Number

  		Returns:
    			is_happy (bool): If number is happy number
       		'''
        	seen = set()
        	
		while n not in seen:
            		seen.add(n)
            		n = sum(int(x)**2 for x in str(n))
            		if n == 1:
                		return True
        	return False
