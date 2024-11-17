# Backtracking Solutions

def Solution:
	# Solution Functions

	def subsets(self, nums: List[int]) -> List[List[int]]:
		'''Possible subsets of list

  		Space Complexity: O(n * 2 ^ n) -> Power Set
    		Time Complexity: O(n * 2 ^ n) -> Power Set

      		Args:
			nums (list): Iterable of numbers

   		Returns:
     			subs (list): All Possible Subsets
   		'''
        	subs = []
        	
		def dfs(cur: list, ix: int):
			'''DFS through values

   			Args:
      				cur (list): Current subset
	  			ix (int): Remaining index on list
			'''
			subs.append(cur)

            		for i in range(ix, len(nums)):
                		dfs(cur + [nums[i], ], i + 1)

        	dfs([], 0)
        	return subs

	def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
		'''Possible combinations that sum to target

  		Space Complexity: O(n * 2 ^ n) -> Power Set
    		Time Complexity: O(n * 2 ^ n) -> Power Set

      		Args:
			nums (list): Iterable of numbers
   			target (int): Sum target

   		Returns:
     			subs (list): All Possible Subsets
   		'''
        	nums.sort()
        	subs = []
        
		def dfs(cur: list, diff: int, ix: int):
			'''DFS through values

   			Args:
      				cur (list): Current subset
	  			diff (int): Remaining difference
	  			ix (int): Remaining index on list
			'''
            		if diff == 0:
                		subs.append(cur)
                		return
            		for i in range(ix, len(nums):
                		if nums[i] > diff:
                    			break
                		dfs(cur + [nums[i], ], diff - nums[i], i)
        	
		dfs([], target, 0)
        	return subs

	def permute(self, nums: List[int]) -> List[List[int]]:
		'''Generate all permutations

  		Space Complexity: O(n * n!) -> Permutations
    		Time Complexity: O(n * n!) -> Permutations

		Args:
  			nums (list): Iterable of numbers

       		Returns:
	 		perms (int): Permutations
    		'''
        	perms = []
        
		def dfs(cur: list, vals: list):
			'''DFS through values

   			Args:
      				cur (list): Current subset
	  			vals (list): Remaining values
			'''
            		if len(cur) == len(nums):
                		perms.append(cur)
            
            		for i, v in enumerate(vals):
                		dfs(cur + [v, ], vals[:i] + vals[i+1:])

        	dfs([], nums)
        	return perms

	def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
		'''Possible subsets of list with duplicates

  		Space Complexity: O(n * 2 ^ n) -> Power Set
    		Time Complexity: O(n * 2 ^ n) -> Power Set

      		Args:
			nums (list): Iterable of numbers

   		Returns:
     			subs (list): All Possible Subsets
   		'''
        	subs = []
        	nums.sort()

        	def dfs(cur: list, ix: int):
			'''DFS through values

   			Args:
      				cur (list): Current subset
	  			ix (int): Remaining index on list
			'''
            		subs.append(cur)
            		prev = -21 # Below minimum permissable number
            
			for i in range(ix, len(nums)):
                		if nums[i] != prev:
                    			dfs(cur + [nums[i], ], i + 1)
                		prev = nums[i]

        	dfs([], 0)
        	return subs

	def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
		'''Possible combinations that sum to target with duplicates

  		Space Complexity: O(n * 2 ^ n) -> Power Set
    		Time Complexity: O(n * 2 ^ n) -> Power Set

      		Args:
			candidates (list): Iterable of numbers
   			target (int): Sum target

   		Returns:
     			subs (list): All Possible Subsets
   		'''
        	candidates.sort()
        	subs = []

        	def dfs(cur: list, diff: int, ix: int):
			'''DFS through values

   			Args:
      				cur (list): Current subset
	  			diff (int): Remaining difference
	  			ix (int): Remaining index on list
			'''
            		if diff == 0:
                		subs.append(cur)

            		prev = 0 # Below permissable value
            		
			for i in range(ix, len(candidates)):
                		if candidates[i] > diff:
                    			break
                		elif candidates[i] != prev:
                    			dfs(cur + [candidates[i], ], diff - candidates[i], i + 1)
                		prev = nums[i]

        	dfs([], target, 0)
        	return subs

	def exist(self, board: List[List[str]], word: str) -> bool:
		'''Check if word exists on grid

  		Space Complexity: O(m * n) -> Grid size
    		Time Complexity: O(m * n * 4 ^ w) -> Grid exploration by character

      		Args:
			board (list): Grid
   			word (str): Iterable of characters

      		Returns:
			is_exists (bool): If word exists in grid
   		'''
		seen = set()
       		R, C = len(board), len(board[0])
        	dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
		def dfs(x: int, y: int, i: int):
			'''DFS through grid

   			Args:
      				x (int): Row
	  			y (int): Column
      				i (int): Character index of word

     			Returns:
				is_word (bool): If word exists
    			'''
            		if i == len(word):
                		return True
            		if (x < 0 or x >= R or y < 0 or y >= C 
			    or board[x][y] != word[i] or (x, y) in seen):
                		return False
            
            		seen.add((x, y))
            		res = any((dfs(x + dx, y + dy, i+1) for dx, dy in dirs))
            		seen.remove((x, y))
            		return res

        	for i in range(R):
            		for j in range(C):
                		if board[i][j] == word[0]:
                    			if dfs(i, j, 0):
                        			return True
        	return False

	def partition(self, s: str) -> List[List[str]]:
		'''Partition palindromes

  		Space Complexity: O(n * 2 ^ n) -> Possible partitions
    		Time Complexity: O (n * 2 ^ n) -> Possible partitions

      		Args:
			s (str) -> Iterable of characters

   		Returns:
     			parts (list): Possible Partitioned Strings
		'''
        	parts = []
        
		def dfs(cur: list, rest: str):
			'''DFS through string

   			Args:
      				cur (list): Current partitioned subset
	  			rest (str): Remaining characters
    			'''
            		if not rest:
                		parts.append(cur)
            		
			for i in range(1, len(rest) + 1):
                		sub = rest[:i]
                		
				if sub == sub[::-1]:
                    			dfs(cur + [sub,], rest[i:])
        	dfs([], s)
        	return parts 

	def letterCombinations(self, digits: str) -> List[str]:
		'''Letter combinations of phone number

  		Space Complexity: O(n * 4 ^ n) -> Letter Exponentiation
    		Time Complexity: O(n * 4 ^ n) -> Letter Exponentiation

      		Args:
			digits (str) -> Iterable of numbers

   		Returns:
     			letters (list) -> Possible combinations
		'''
        	keys = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        	letters = []
        
		def dfs(cur: str, nums: str):
			'''DFS through digits

      			Args:
	 			cur (str): Current letter combination
     				nums (str): Remaining numbers
	 		'''
            		if not nums:
                		if cur:
                    			letters.append(cur)
            		else:
                		d = int(nums[0])
                		for c in keys[d]:
                    			dfs(cur + c, nums[1:])
        	
		dfs('', digits)
        	return letters
