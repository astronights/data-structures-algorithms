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
