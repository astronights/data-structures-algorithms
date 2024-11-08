# Trees Solutions

class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		'''Binary Tree Node

    		Args:
      			val (int): Node Value
	 		left (TreeNode): Left Child
    			right (TreeNode): Right Child
       		'''
        	self.val = val
        	self.left = left
        	self.right = right

class Solutions:
	# Solution Functions
	
	def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		'''Invert Binary Tree

  		Space Complexity: O(n) -> Same structure as tree
    		Time Complexity: O(n) -> Iterate over all nodes once

		Args:
  			root (TreeNode): Binary Tree

     		Returns:
       			root (TreeNode): Inverted Binary Tree
	  	'''
        	if not root:
            		return None
        	
		root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        	return root

	def maxDepth(self, root: Optional[TreeNode]) -> int:
		'''Maximum depth of Binary Tree

  		Space Complexity: O(n) -> Tree structure
    		Time Complexity: O(n) -> Node iteration

      		Args:
			root (TreeNode): Binary Tree

   		Returns:
     			max_depth (int): Maximum depth
		'''
        	if not root:
            		return 0
        	return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

	def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
		'''Diameter of Binary Tree

  		Space Complexity: O(n) -> Tree Structure
    		Time Complexity: O(n) -> Node iteration

      		Args:
			root (TreeNode): Binary Tree

   		Returns:
     			max_D (int): Diameter
		'''
        	max_D = 0
        
		def dfs(tree: Optional[TreeNode]) -> int:
			'''DFS Through Tree

      			Args:
	 			tree (TreeNode): Tree Node
     			Returns:
				height (int): Height so far
    			'''
            		nonlocal max_D
            		
			if not tree:
                		return 0
            		left_D = dfs(tree.left)
            		right_D = dfs(tree.right)

            		max_D = max(max_D, left_D + right_D)
            		return 1 + max(left_D, right_D)

        	_ = dfs(root)
        	return max_D

	def isBalanced(self, root: Optional[TreeNode]) -> bool:
		'''Is Binary Tree balanced

   		Space Complexity: O(n) -> Tree Structure
     		Time Complexity: O(n) -> Node Iteration

       		Args:
	 		root (TreeNode): Binary Tree

    		Returns:
      			is_balance (bool): Is tree balanced
	 	'''
        	is_balance = True
        
		def dfs(tree: Optional[TreeNode]):
			'''DFS Through Tree

      			Args:
	 			tree (TreeNode): Tree Node
     			Returns:
				height (int): Height so far
    			'''
            		nonlocal is_balance
            		
			if not tree:
                		return 0

		        left_H = dfs(tree.left)
            		right_H = dfs(tree.right)

            		if abs(left_H - right_H) > 1:
                		is_balance = False
                		return 0

            		return 1 + max(left_H, right_H)

        	dfs(root)
        	return is_balance

	def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
		'''Check if two trees are the same

  		Space Complexity: O(n) -> Tree Structure
    		Time Complexity: O(n) -> Node Iteration

      		Args:
			p (TreeNode): Binary Tree 1
   			q (TreeNode): Binary Tree 2

      		Returns:
			is_same (bool): If two trees are the same
   		'''
        	if not p and not q:
            		return True
        	elif not p or not q:
            		return False
        	else:
            		return (p.val == q.val 
				and self.isSameTree(p.left, q.left) 
				and self.isSameTree(p.right, q.right))

	def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
		'''Check if tree is a subtree of another

  		Space Complexity: O(m + n) -> Two Trees
    		Time Complexity: O(m * n) -> Node Iteration

      		Values: Nodes in Tree (m), Nodes in Sub Tree (n)

 		Args:
   			root (TreeNode): Binary Tree
      			subRoot (TreeNode): Binary SubTree

  		Returns:
    			is_sub (bool): If Sub Tree
       		'''
        	if not subRoot:
            		return True
        	elif not root:
            		return False
        	else:
            		return (self.isSameTree(root, subRoot) 
				or self.isSubtree(root.left, subRoot) 
				or self.isSubtree(root.right, subRoot))

	def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
		'''Lowest Common Ancestor in a Binary Search Tree

    		Space Complexity: O(n) -> Tree Structure
      		Time Complexity: O(n) -> Node Iteration

 		Args:
   			root (TreeNode): Binary Search Tree
      			p (TreeNode): Node 1
	 		q (TreeNode): Node 2

    		Returns:
      			root (TreeNode): Lowest Common Ancestor
	 	'''
        	if p.val >= q.val:
            		p, q = q, p
        
		while not (p.val <= root.val and q.val >= root.val):
            		if p.val <= root.val:
                		root = root.left
            		else:
                		root = root.right
        	return root
