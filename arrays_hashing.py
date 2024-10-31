

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
