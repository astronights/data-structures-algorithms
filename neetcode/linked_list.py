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

class Node:
	def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
		'''Node of Linked List with Random Pointer

  		Args:
    			x (int): value
       			next (Node): Next Node
	  		random (Node): Random Node
     		'''
        	self.val = int(x)
        	self.next = next
        	self.random = random

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

	def reorderList(self, head: Optional[ListNode]) -> None:
		'''Reorder Linked List

  		Space Complexity: O(1) -> Linked List Pointers
    		Time Complexity: O(n) -> Three Passes over Linked List

      		Args:
			head (ListNode): Linked List
   		'''

		# Identify mid point
		slow, fast = head, head.next
        	while fast and fast.next:
            		slow = slow.next
            		fast = fast.next.next

        	cur, prev = slow.next, None
        	slow.next = None

		# Reverse second half of linked list
        	while cur:
            		temp = cur.next
            		cur.next = prev
            		prev = cur
            		cur = temp

        	cur = head

		# Insert reversed half in between nodes
        	while prev:
            		temp = cur.next
            		cur.next = prev
            		prev = prev.next
            		cur.next.next = temp
            		cur = cur.next.next

	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		'''Remove n-th node from end

  		Space Complexity: O(1) -> Linked List Pointers
    		Time Complexity: O(n) -> Single Pass

      		Args:
			head (ListNode): Linked List
   			n (int): Node index from end

      		Returns:
			cur (ListNode): Linked List without nth node
   		'''
        	# Traverse to n-th node from start
        	counter = head
        	for i in range(n-1):
            		counter = counter.next

        	cur = ListNode(next=head)
        	dummy = cur

		# Traverse another pointer till first pointer reaches end
        	while counter.next:
            		dummy = dummy.next
            		counter = counter.next

        	dummy.next = dummy.next.next
        	return cur.next


	def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
		'''Deep Copy Linked List with random pointers

  		Space Complexity: O(n) -> Copy Dictionary
    		Time Complexity: O(n) -> Two Pass over all nodes

      		Args:
			head (Node): Linked List

   		Returns:
     			copy_head (Node): Deep copied Linked List
		'''
        	if not head:
            		return None
        
		copies = {}
        	cur = head
        	
		while cur:
            		copies[cur] = Node(cur.val)
            		cur = cur.next

        	for node in copies.keys():
            		if node.next:
                		copies[node].next = copies[node.next]
            		if node.random:
                		copies[node].random = copies[node.random]

        	return copies[head]

	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		'''Add two numbers

  		Space Complexity: O(1) -> Linked List Pointers
    		Time Complexity: O(n) -> Pass over all digits

      		Values: Number of digits in sum (n) i.e. length of longer number + 1

		Args:
  			l1 (ListNode): Number 1 Linked List
     			l2 (ListNode): Number 2 Linked List

 		Returns:
   			res (ListNode): Sum Linked List
      		'''
        	res = ListNode()
        	cur = res
        	carry = 0

        	while l1 or l2:
            		val1 = l1.val if l1 else 0
            		val2 = l2.val if l2 else 0

            		total = (val1 + val2 + carry)
            		add = total % 10
            		carry = total // 10

            		cur.next = ListNode(add)
            		cur = cur.next

            		l1 = l1.next if l1 else None
            		l2 = l2.next if l2 else None

        	if carry > 0:
            		cur.next = ListNode(carry)

        	return res.next
