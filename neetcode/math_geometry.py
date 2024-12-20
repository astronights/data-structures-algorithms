# Math & Geometry Solutions
from collections import defaultdict

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

	def plusOne(self, digits: List[int]) -> List[int]:
		'''Add one to array of digits

  		Space Complexity: O(n) -> Digits
    		Time Complexity: O(n) -> Single Pass

      		Args:
			digits (list): Iterable of digits

     		Returns:
       			out (list): Incremented number
	  	'''
        	out = []
        	done = False
        
		for n in digits[::-1]:
            		if done:
                		out.append(n)
            		else:
                		if n < 9:
                    			out.append(n + 1)
                    			done = True
                		else:
                    			out.append(0)
        	if out[-1] == 0:
            		out.append(1)

        	return out[::-1]

	def myPow(self, x: float, n: int) -> float:
		'''Calculate power of a number

  		Space Complexity: O(log n) -> Binary Exponentiation
    		Time Complexity: O(log n) -> Binary Exponentiation

      		Args:
			x (float): Number
   			n (int): Exponent

      		Returns:
			out (float): Exponentiated number
   		'''
        	def helper(x: float, n: int) -> float:
			'''Helper function

   			Args:
				x (float): Number
   				n (int): Exponent

      			Returns:
				out (float): Exponentiated number
    			'''
            		if x == 0:
                		return 0
            		elif n == 0:
                		return 1
            		out = pow(x ** 2, n // 2)
            		return x * out if n % 2 else out

        	out = helper(x, abs(n))
        	return out if n >= 0 else 1 / out

	def multiply(self, num1: str, num2: str) -> str:
		'''Multiply two strings

  		Space Complexity: O(m + n) -> Product
    		Time Complexity: O(m * n) -> Multiplication

		Values: Digits in num1 (m), digits in num2 (n)

  		Args:
    			num1 (str): Number 1
       			num2 (str): Number 2

   		Returns:
     			prod (str): Product
		'''
        	if num1 == '0' or num2 == '0':
            		return '0'
        
		a, b = len(num1), len(num2)
        	out = [0] * (a + b + 2)
        	num1, num2 = num1[::-1], num2[::-1]

        	for i in range(a):
            		for j in range(b):
                		prod = int(num1[i]) * int(num2[j])
                		out[i + j] += prod
                		out[i + j + 1] += out[i + j] // 10
                		out[i + j] %= 10

        	return ''.join(str(x) for x in out).rstrip('0')[::-1]


class CountSquares:

	def __init__(self):
		'''Count number of squares

  		Space Complexity: O(n) -> Points
    		'''
        	self.counter = defaultdict(int)
        	self.points = []

	def add(self, point: List[int]) -> None:
		'''Add point

  		Time Complexity: O(1) -> Append

    		Args:
      			point (list): Co-ordinates
		'''
        	self.counter[tuple(point)] += 1
        	self.points.append(point)

    	def count(self, point: List[int]) -> int:
		'''Count number of squares with point

  		Time Complexity: O(n) -> Point Iteration

    		Args:
      			point (list): Co-ordinates

  		Returns:
    			out (int): Number of squares
       		'''
        	out = 0
        	px, py = point

		for x, y in self.points:
            		if abs(x - px) != abs(y - py) or x == px or y == py:
                		continue
            		out += self.counter[(x, py)] * self.counter[(px, y)]
        	return out
