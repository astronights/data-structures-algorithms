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
