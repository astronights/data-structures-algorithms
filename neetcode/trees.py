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
