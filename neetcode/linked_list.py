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

	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		'''Merge two sorted linked lists

  		Space Complexity: O(1) -> Linked List Pointers
    		Time Complexity: O(m+n) -> Single pass over both lists

      		Values: List sizes (m, n)

 		Args:
   			list1 (ListNode): Linked List 1
      			list2 (ListNode): Linked List 2

  		Returns:
    			res (ListNode): Merged Linked List
       		'''
        	res = ListNode()
        	dummy = res
        
		while list1 and list2:
            		if list1.val < list2.val:
                		dummy.next = list1
                		list1 = list1.next
            		else:
                		dummy.next = list2
                		list2 = list2.next
            		dummy = dummy.next
        
		if list1:
            		dummy.next = list1
        	if list2:
            		dummy.next = list2
        	
		return res.next

        
