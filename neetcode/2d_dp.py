# 2-D DP Solutions

class Solution:
	# Solution Functions

	def uniquePaths(self, m: int, n: int) -> int:
		'''Number of unique paths in grid

    		Space Complexity: O(m * n) -> DP Array
      		Time Complexity: O(m * n) -> Single Pass

 		Values: Grid Dimensions (m x n)

   		Args:
     			m (int): Grid length
			n (int): Grid width

   		Returns:
     			n_paths (int): Number of paths
		'''
        	dp = [[0] * (n) for _ in range(m)]

        	for i in range(m):
            		dp[i][0] = 1
        	for i in range(n):
            		dp[0][i] = 1

        	for i in range(1, m):
            		for j in range(1, n):
                		dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        	return dp[-1][-1]

	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		'''Longest Common Subsequence between 2 words

  		Space Complexity: O(m * n) -> DP Array
    		Time Complexity: O(m * n) -> Single Pass

      		Values: Length of word 1 (m), length of word 2 (n)

      		Args:
			text1 (str): Word 1
   			text2 (str): Word 2

      		Returns:
			longest (int): Length of longest common subsequence
   		'''
        	m, n = len(text1), len(text2)
        	dp = [[0] * (n + 1) for _ in range(m + 1)]

        	for i in range(1, m + 1):
            		for j in range(1, n + 1):
                		if text1[i - 1] == text2[j - 1]:
                    			dp[i][j] = 1 + dp[i - 1][j - 1]
                		else:
                    			dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        	return dp[-1][-1]

	def maxProfit(self, prices: List[int]) -> int:
		'''Maximum profit with cooldown

    		Space Complexity: O(n) -> DP Array
      		Time Complexity: O(n) -> Single Pass

 		Args:
   			prices (list): Iterable of prices

		Returns:
  			max_profit (int): Maximum profit
     		'''
        	n = len(prices)
        	dp = {}

        	def dfs(i: int, buy: bool) -> int:
			'''DFS through days

   			Args:
      				i (int): Day index
	  			buy (bool): Buy / Sell

      			Returns:
	 			max_profit (int): Maximum profit
     			'''
            		if i >= n:
                		return 0
            		if (i, buy) in dp:
                		return dp[(i, buy)]

            		cooldown = dfs(i + 1, buy)

            		if buy:
                		profit = dfs(i + 1, False) - prices[i]
                		dp[(i, buy)] = max(profit, cooldown)
            		else:
                		profit = dfs(i + 2, True) + prices[i]
                		dp[(i, buy)] = max(profit, cooldown)

            		return dp[(i, buy)]
			
        	return dfs(0, True)

	def change(self, amount: int, coins: List[int]) -> int:
		'''Distinct ways to change coins

  		Space Complexity: O(n) -> DP Array
    		Time Complexity: O(n * k) -> Coin Iteration

      		Values: Amount (n), number of coins (k)

 		Args:
   			amount (int): Money available
      			coins (list): Iterable of coins

  		Returns:
    			n_ways (int): Number of ways
       		'''
        	dp = [0] * (amount + 1)
        	dp[0] = 1

        	for c in coins:
            		for i in range(c, amount + 1):
                		dp[i] += dp[i - c]
        	return dp[-1]

	def findTargetSumWays(self, nums: List[int], target: int) -> int:
		'''Find Ways to Target Sum

    		Space Complexity: O(n) -> DP Array
      		Time Complexity: O(n * k) -> Iteration

 		Values: Numbers (n), Sum of all numbers (k)

   		Args:
     			nums (list): Iterable of numbers
			target (int): Target number

   		Returns:
     			n_ways (int): Number of ways to sum
		'''
        	dp = {}
        
		def dfs(i: int, total: int) -> int:
			'''DFS through number sums

   			Args:
      				i (int): Index
	  			total (int): Running sum

      			Returns:
	 			n_ways (int): Number of ways
     			'''
            		if i == len(nums):
                		return 1 if total == target else 0
            		if (i, total) in dp:
                		return dp[(i, total)]

            		dp[(i, total)] = dfs(i + 1, total + nums[i]) + dfs(i + 1,total - nums[i])
            		return dp[(i, total)]

        	return dfs(0, 0)

	def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
		'''If string can be formed by interleaving others

  		Space Complexity: O(m * n) -> DP Array
    		Time Complexity: O(m * n) -> Single Pass

      		Values: Lengths of smaller strings (m, n)

 		Args:
   			s1 (str): Iterable of characters 1
      			s2 (str): Iterable of characters 2
	 		s3 (str): Iterable to check interleaving on

    		Returns:
      			is_interleave (bool): If strings can interleave to form target
	 	'''
        	m, n = len(s1), len(s2)

        	dp = [[False] * (n + 1) for _ in range(m + 1)]
        	dp[0][0] = True

        	for i in range(1, m + 1):
            		dp[i][0] = (s1[i - 1] == s3[i - 1]) and dp[i - 1][0]
        	for i in range(1, n + 1):
            		dp[0][i] = (s2[i - 1] == s3[i - 1]) and dp[0][i - 1]

        	for i in range(1, m + 1):
            		for j in range(1, n + 1):
                		check_1 = (s1[i - 1] == s3[i + j - 1]) and dp[i - 1][j]
                		check_2 = (s2[j - 1] == s3[i + j - 1]) and dp[i][j - 1]
                		dp[i][j] = check_1 or check_2
        	return dp[-1][-1]
