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
        
		def dfs(tree: Optional[TreeNode]) -> int:
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

	def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
		'''K-th smallest element in Binary Search Tree

  		Space Complexity: O(n) -> Tree Structure
    		Time Complexity: O(n) -> Node Iteration

  		Args:
    			root (TreeNode): Binary Search Tree
       			k (int): Index of sorted element

   		Returns:
     			node (int): K-th smallest value
		'''
        	stack = []
        	cur = root
        
		while cur or stack:
            		while cur:
                		stack.append(cur)
                		cur = cur.left
            
            		node = stack.pop()
            		k -= 1

            		if k == 0:
                		return node.val
            
            		cur = node.right

	def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
		'''Reconstruct Binary Tree from preorder and inorder traversal

  		Space Complexity: O(n) -> Index Counter
    		Time Complexity: O(n) -> Single Pass

  		Args:
    			preorder (list): Preorder Traversal
       			inorder (list): Inorder Traversal

   		Returns:
     			root (TreeNode): Binary Tree
		'''
        	pre_ix = 0
		indices = {val: ix for ix, val in enumerate(inorder)}

		def dfs(left: int, right: int) -> Optional[TreeNode]:
			'''DFS through Binary Tree

   			Args:
      				left (int): Left index
	  			right (int): Right index

      			Returns:
	 			root (TreeNode): Binary Tree Node
     			'''
			nonlocal pre_ix
			if left > right:
				return None

			mid_val = preorder[pre_ix]
			mid_ix = indices[mid_val]
			pre_ix += 1
			
			root = TreeNode(mid_val)
			root.left = dfs(left, mid_ix - 1)
			root.right = dfs(mid_ix + 1, right)
			return root

		return dfs(0, len(preorder) - 1)
			
	def maxPathSum(self, root: Optional[TreeNode]) -> int:
		'''Maximum path sum

    		Space Complexity: O(n) -> Tree Structure
      		Time Complexity: O(n) -> Node Iteration

 		Args:
   			root (TreeNode): Binary Tree

      		Returns:
			path_sum (int): Maximum path sum
   		'''
		path_sum = -1001
        
		def dfs(tree: Optional[TreeNode]) -> int:
			'''DFS Through Tree

      			Args:
	 			tree (TreeNode): Tree Node

			Returns:
   				tree_sum (int): Current tree sum
    			'''
            		nonlocal max_sum
            		if not tree:
                		return 0
            
            		left_sum = max(0, dfs(tree.left))
            		right_sum = max(0, dfs(tree.right))

            		path_sum = max(path_sum, tree.val + left_sum + right_sum)
            		return tree.val + max(left_sum, right_sum)

        	dfs(root)
        	return path_sum
