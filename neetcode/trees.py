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
