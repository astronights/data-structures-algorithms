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
            		for i, num in enumerate(nums[ix:]):
                		if num > diff:
                    			break
                		dfs(cur + [num, ], diff - num, ix + i)
        	
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
