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
