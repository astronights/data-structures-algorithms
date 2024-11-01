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

	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		'''Get indices of two sum in sorted array

  		Space Complexity: O(1) -> Pointers
    		Time Complexity: O(n) -> Iteration over elements

      		Args:
			numbers (list): Iterable of numbers
   			target (int): Target sum

      		Returns:
			indices (list): Indices of elements
   		'''
        	l, r = 0, len(numbers) - 1
        
		while l < r:
			cur_sum = numbers[l] + numbers[r]
            		if cur_sum == target:
                		return [l+1, r+1]
            		elif cur_sum < target:
                		l += 1
            		else:
                		r -= 1
		return [-1, -1]
