# Two Pointers Solutions
from collections import Counter, defaultdict

class Solutions:
	# Solution Functions
	
	def isPalindrome(self, s: str) -> bool:
		'''Check if a string is a palindrome

  		Space Complexity: O(n) -> Cleaned string
    		Time Complexity: O(n) -> Iteration to half the string

      		Args:
			s (str): String

   		Returns:
     			is_pal (bool): Palindrome check
		'''
	        s = [c.lower() for c in s if c.isalnum()]
        	l, r = 0, len(s) - 1
		
        	while l < r:
            		if s[l] == s[r]:
		                l += 1
		                r -= 1
		        else:
		        	return False
       		
		return True
