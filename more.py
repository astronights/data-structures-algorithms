# More interesting puzzles

class TreeNode:
	def __init__(self, x):
		'''Binary Tree Node

  		Args:
    			x (int): Value
       		'''
        	self.val = x
        	self.left = None
        	self.right = None

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

	def maxProfit(self, k: int, prices: List[int]) -> int:
		'''Maximum profit with k transactions

  		Space Complexity: O(n) -> Storing prices and profits
		Time Complexity: O(k * n) -> Iterating over ticks and transactions

  		Values: Transactions (k), Ticks (n)

    		Args:
      			k (int): Number of transactions
	 		prices (list): Tick data of prices

    		Returns:
      			max_profit (int): Maximum profit
		'''
        	buys = [float('inf')] * (k+1)
        	profits = [0] * (k+1)

        	for p in prices:
            		for i in range(1, k+1):
                		buys[i] = min(buys[i], p - profits[i - 1])
                		profits[i] = max(profits[i], p - buys[i])

        	return profits[k]


	def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
		'''Lowest Common Ancestor of Binary Tree

  		Space Complexity: O(n) -> Tree Structure
    		Time Complexity: O(n) -> Node Iteration

      		Args:
			root (TreeNode): Binary Tree
   			p (TreeNode): Node 1
      			q  (TreeNode): Node 2

  		Returns:
    			node (TreeNode): Lowest Common Ancestor
       		'''
    		if not root or root == p or root == q:
      			return root

    		l = self.lowestCommonAncestor(root.left, p, q)
    		r = self.lowestCommonAncestor(root.right, p, q)

    		if l and r:
      			return root
    		return l or r

	def calculate(self, s: str) -> int:
		'''Basic addition and subtraction calculator

  		Space Complexity: O(n) -> Stack
    		Time Complexity: O(n) -> Single Pass

      		Args:
			s (str): String to evaluate

   		Returns:
     			res (int): Evaluated result
		'''
        	num = 0
        	sign = 1
        	stack = [1,]

		res = 0
        	
		for c in s:
            		if '0' <= c <= '9':
                		num = 10 * num + int(c)
            		elif c in '-+':
                		res += sign * num
                		sign = (-1 if c == '-' else 1) * stack[-1]
                		num = 0
            		elif c == '(':
                		stack.append(sign)
            		elif c == ')':
                		stack.pop()  
        	
		return res + num * sign
