from collections import Counter

class ArrayHashing:
	# Arrays and Hashing Solutions
  
	def hasDuplicate(self, nums: List[int]) -> bool:
		'''Check if list has any duplicate numbers
  
  		Space Complexity: O(n) -> Set of seen numbers
		Time Complexity: O(n) -> Iterating over numbers. Set IO is O(1)
	
		Args:
			nums (list): Iterable of numbers
	
		Returns:
			is_dup (bool): If the list has duplicates
		'''
		seen = set()
	
		for n in nums:
			if n in seen:
				return True
			seen.add(n)
		return False

	def isAnagram(self, s: str, t: str) -> bool:
		'''Check if two strings are anagrams of each other

  		Space Complexity: O(n) -> Frequency Counter
		Time Complexity: O(n) -> Creating Counter

		Args:
  			s (str): String 1
	 		t (str): String 2

 		Returns:
   			is_same (bool): If the two strings are anagrams
	  	'''
        	return Counter(s) == Counter(t)

	def twoSum(self, nums: List[int], target: int) -> List[int]:
		'''Get indices of elements that sum to target

  		Space Complexity: O(n) -> Value Position Dictionary
    		Time Complexity: O(n) -> Creating dictionary. Dict IO is O(1)

      		Args:
			nums (list): Iterable of numbers
   			target (int): Sum value

      		Returns:
			indices (list): Indices of the two elements
   		'''
	        pos = {}
		
	        for ix, num in enumerate(nums):
			rem = target - num
		        if rem in pos:
				return [pos[rem], ix]
			pos[num] = ix
		return [-1, -1]
