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
