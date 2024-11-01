# Stack Solutions
from collections import Counter, defaultdict

class Solutions:
	# Solution Functions
	
	def isValid(self, s: str) -> bool:
		'''Check valid parentheses

  		Space Complexity: O(n) -> Parentheses Stack
    		Time Complexity: O(n) -> String Iteration

      		Args:
			s (str): String

   		Returns:
     			is_valid (bool): If valid parentheses
		'''
		stack = []
        	pairs = {')': '(', '}': '{', ']': '['}
        
		for c in s:
            		if c in pairs:
                		if stack and stack[-1] == pairs[c]:
                    			stack.pop()
                		else:
                    			return False
            		else:
                		stack.append(c)
		return len(stack) == 0

	def evalRPN(self, tokens: List[str]) -> int:
		'''Evaluate Reverse Polish Notation

  		Space Complexity: O(n) -> Stack
    		Time Complexity: O(n) -> Iteration

      		Args:
			tokens (list): Mathematical symbols

   		Returns:
     			val (int): Result
		'''
	        stack = []
        	for c in tokens:
            		if c not in '+-*/':
                		stack.append(int(c))
            		else:
				# Pop happens Left to Right
                		a, b = stack.pop(), stack.pop()
                		if c == '+':
                    			stack.append(a+b)
                		elif c == '-':
                    			stack.append(b-a)
                		elif c == '*':
                    			stack.append(a*b)
                		else:
                    			stack.append(int(float(b)/a))
        	return stack[-1]

	def generateParenthesis(self, n: int) -> List[str]:
		'''Generate Parentheses

  		Space Complexity: O(n) -> Stack space
  		Time Complexity: O(4^n / √n) -> Catalan number DFS

    		Args:
      			n (int): Number of parentheses to use

  		Returns:
    			res (list): List of valid parentheses strings
       		'''
        	res = []
        	stack = []
		
		def dfs(l: int, r: int) -> None:
			'''DFS to build parenthesis string

   			Args:
      				l (int): Number of left parenthesis used
	  			r (int): Number of right parenthesis used
      			'''
            		if l + r == 2*n:
                		res.append(''.join(stack))
            		if l < n:
                		stack.append('(')
                		dfs(l + 1, r)
                		stack.pop()
            		if r < l:
                		stack.append(')')
                		dfs(l, r + 1)
                		stack.pop()
		dfs(0, 0)
        	return res
            


class MinStack:

	def __init__(self):
		'''Minimum Stack

		Space Complexity: O(n) -> Stack Elements
     		'''
	    	self.stack = []
	    	self.min_stack = []

   	 def push(self, val: int) -> None:
		'''Add element to stack

      		Time Complexity: O(1) -> List Append

 		Args:
   			val (int): Value to append
      		'''
		min_val = val if not self.min_stack else min(self.min_stack[-1], val)
     		
        	self.stack.append(val) 
	        self.min_stack.append(min_val)

	def pop(self) -> None:
		'''Pop top element from stack

    		Time Complexity: O(1) -> List Pop
      		'''
	        self.stack.pop()
        	self.min_stack.pop()

    	def top(self) -> int:
		'''Get top element from stack

  		Time Complexity: O(1) -> List Access

    		Returns:
      			val (int): Top Element
	 	'''
        	return self.stack[-1]

    	def getMin(self) -> int:
		'''Get minimum element from stack

  		Time Complexity: O(1) -> List Access

    		Returns:
      			val (int): Minimum Element
	 	'''
        	return self.min_stack[-1]
