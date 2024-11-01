# More interesting puzzles

class Solution:
	'''Solution Functions'''
	
	def longestValidParentheses(self, s: str) -> int:
		'''Longest Valid Parentheses

		Space Complexity: O(n) -> DP Array
  		Time Complexity: O(n) -> Single Pass

    		Args:
      			s (str): Parenthesis string

  		Returns:
    			n (int): Longest parentheses length
       		'''
      
        	dp = [0] * (len(s) + 1)

		for i, c in enumerate(s):
        		if c ==')':
                		if (i > 0):
                    			if (s[i - 1] == '('):
                        			dp[i + 1] = 2 + dp[i - 1]
                    			else:
                        			start_pos = i - 1 - dp[i]
                        			if start_pos >= 0 and s[start_pos] == '(':
                            				dp[i + 1] = dp[i] + 2 + dp[start_pos]
		return max(dp)
