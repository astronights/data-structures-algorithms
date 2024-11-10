# Arrays and Hashing Solutions
from collections import Counter, defaultdict

class Solutions:
	# Solution Functions
  
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

	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		'''Group anagrams from list of strings together

  		Space Complexity: O(n*m) -> String Mapping Dictionary
    		Time Complexity: O(n*m) -> List iteration + Frequency Tuple

      		Values: Number of strings (n), Max Length of String (m)

  		Args:
    			strs (list): List of strings

       		Returns:
	 		values (list): List of grouped strings
    		'''
	        groups = defaultdict(list)
		
	        for s in strs:
			# Building string representation as frequency tuple of characters
			counter = [0] * 26
	            	for c in s:
				ix = ord(c) - ord('a')
				counter[ix] += 1
			groups[tuple(counter)].append(s)
	
	        return groups.values()

	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		'''Get Top K Frequent Elements from list

  		Space Complexity: O(n) -> Frequency Buckets
    		Time Complexity: O(n) -> Bucket Sort

  		Args:
    			nums (list): Iterable of numbers
       			k (int): Threshold value

		Returns:
  			res (list): Top K Frequent Elements
     		'''
		count = {}
		freq = [[] for i in range(len(nums)+1)]

		# Bucket sort numbers
		for num in nums:
	        	count[num] = 1 + count.get(num, 0)
	        for num, cnt in count.items():
	        	freq[cnt].append(num)
	
	        res = []
	        for i in range(len(freq)-1, -1, -1):
	        	for num in freq[i]:
	        		res.append(num)

	                	if len(res) == k:
	                    		return res

	def productExceptSelf(self, nums: List[int]) -> List[int]:
		'''Calculate product of array except element

  		Space Complexity: O(n) -> Remainder products
    		Time Complexity: O(n) -> Array two pass

      		Args:
			nums (list): Iterable of numbers

     		Returns:
       			res (list): Product of other elements
	  	'''
        	N = len(nums)
        	left, right = [1] * N, [1] * N

        	for i in range(1, N):
            		left[i] = left[i-1] * nums[i-1]
            		right[N-1-i] = right[N-i] * nums[N-i]

        	return [left[i]*right[i] for i in range(N)]

	def isValidSudoku(self, board: List[List[str]]) -> bool:
		'''Check if a Sudoku is valid

  		Space Complexity: O(n*n) -> Sudoku size
    		Time Complexity: O(n*n) -> Element iteration

      		Values: Sudoku Dimension (n*n)

 		Args:
   			board (list): Sudoku board

      		Returns:
			is_valid (bool): Sudoku validity
		'''
        	rows = defaultdict(set)
        	cols = defaultdict(set)
        	squares = defaultdict(set)

	        for r in range(9):
        		for c in range(9):
                		cur = board[r][c]

		                if cur == '.':
			    		continue
                		if (cur in rows[r] or 
				    cur in cols[c] or 
				    cur in squares[(r // 3), (c // 3)]):
                    			return False

			        rows[r].add(cur)
				cols[c].add(cur)
				squares[(r // 3, c // 3)].add(cur)
        	return True

	def longestConsecutive(self, nums: List[int]) -> int:
		'''Longest Consecutive Subsequence

  		Space Complexity: O(n) -> Set of values
    		Time Complexity: O(n) -> Single pass over each element

      		Args:
			nums (list): Iterable of numbers

   		Returns:
     			res (int): Longest consecutive subsequence
		'''
        	res = 0
		seen = set(nums)

        	for n in nums:
            		if n - 1 not in seen:
                		cur = 1
                		while n + cur in seen:
	    				cur += 1
                		res = max(res, cur)
        	return res

class StringEncodeDecode:
	# String Encode Decode
	
	def encode(self, strs: List[str]) -> str:
		'''Encode string

  		Space Complexity: O(n*m) -> Encoded string
    		Time Complexity: O(n) -> List iteration

		Values: Number of strings (n), Max Length of String (m)
  
  		Args:
    			strs (list): Iterable of strings

       		Returns:
	 		s (str): Encoded string
    		'''
		return ''.join(f'{len(s)}#{s}' for s in strs)
		
	def decode(self, s: str) -> List[str]:
		'''Decode string

  		Space Complexity: O(n*m) -> Decoded list
    		Time Complexity: O(n) -> String iteration

		Values: Number of strings (n), Max Length of String (m)
  
  		Args:
    			s (str): Encoded string

       		Returns:
	 		res (list): Decoded strings
    		'''
		res = []
		cur = ''
		i = 0
		
	        while i < len(s):
	        	c = s[i]
	        	if c != '#':
	        		cur += c
	                	i += 1
	            	else:
	                	nxt = i + 1 + int(cur)
	                	res.append(s[i+1:nxt])
	                	i = nxt
				cur = ''
	        return res
	            
