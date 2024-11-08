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


	def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		'''Level Order Traversal of Binary Tree

  		Space Complexity: O(n) -> Leaf Nodes of Tree
    		Time Complexity: O(n) -> Node Iteration

      		Args:
			root (TreeNode): Binary Tree

     		Returns:
       			out (list): Node Values
	  	'''
        	if not root:
            		return []
			
        	queue = [root]
        	out = []
        
		while queue:
            		nodes = []
            		out.append([n.val for n in queue])
            		for n in queue:
                		nodes.extend([n.left, n.right])
            		queue = [n for n in nodes if n]
        	return out

	def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
		'''Right Side View of Binary Tree

    		Space Complexity: O(n) -> Tree Structure
      		Time Complexity: O(n) -> Node Iteration

  		Args:
    			root (TreeNode): Binary Tree

       		Returns:
	 		view (list): Right Side View
    		'''
        	if not root:
            		return []
        	
		queue = [root]
        	view = []
        	
		while queue:
            		nodes = []
            		view.append(queue[-1].val)
            		for n in queue:
                		nodes.extend([n.left, n.right])
            		queue = [n for n in nodes if n]
        	return view

	def goodNodes(self, root: TreeNode) -> int:
		'''Count good nodes in binary tree

  		Space Complexity: O(n) -> Tree Structure
    		Time Complexity: O(n) -> Node Iteration

      		Args:
			root (TreeNode): Binary Tree

   		Returns:
     			c (int): Number of good nodes
		'''
        	c = 0
        	
		def dfs(tree: Optional[TreeNode], val: int):
			'''DFS Through Tree

      			Args:
	 			tree (TreeNode): Tree Node
     				val (int): Maximum value so far
    			'''
            		nonlocal c
            		if not tree:
                		return
            		if tree.val >= val:
                		c += 1
            
			max_val = max(tree.val, val)
            		dfs(tree.left, max_val)
            		dfs(tree.right, max_val)

        	dfs(root, -101) # Minimum value as per problem
        	return c

	def isValidBST(self, root: Optional[TreeNode]) -> bool:
		'''Check if valid Binary Search Tree

  		Space Complexity: O(n) -> Tree Structure
    		Time Complexity: O(n) -> Node Iteration

      		Args:
			root (TreeNode): Binary Tree

   		Returns:
     			is_valid (bool): If Valid Binary Search Tree
		'''
        	def dfs(tree: Optional[TreeNode], min_val: int, max_val: int):
			'''DFS Through Tree

      			Args:
	 			tree (TreeNode): Tree Node
     				min_val (int): Minimum permissable value
	 			max_val (int): Maximum permissable value

     			Returns:
				is_valid (bool): If subtree is valid
    			'''
            		if not tree:
                		return True
            		if tree.val < max_val and tree.val > min_val:
                		return (dfs(tree.left, min_val, tree.val) 
					and dfs(tree.right, tree.val, max_val))
            		else:
                		return False

        	return dfs(root, -1001, 1001)
