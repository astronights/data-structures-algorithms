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
