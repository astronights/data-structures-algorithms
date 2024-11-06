# Linked List

class ListNode:
	def __init__(self, val = 0, next = None):
		'''Node of Linked List

  		Args:
    			val (int): Value
       			next (ListNode): Next Node
	  	'''
		self.val = val
        	self.next = next

class Solutions:
	# Solution Functions

	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		'''Reverse Linked List

  		Space Complexity: O(1) -> Pointers
    		Time Complexity: O(n) -> Single Pass

      		Args:
			head (ListNode): Linked List

   		Returns:
     			prev (ListNode): Reversed Linked List
		'''
        	cur, prev = head, None
        	
		while cur:
            		nxt = cur.next
            		cur.next = prev
            		prev = cur
            		cur = nxt
        	return prev
