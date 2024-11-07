# Linked List
import heapq

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


	def hasCycle(self, head: Optional[ListNode]) -> bool:
		'''Linked List Cycle Detection

  		Space Complexity: O(1) -> Two Pointers
    		Time Complexity: O(n) -> Pass over Linked List nodes

      		Args:
			head (ListNode): Linked List

   		Returns:
     			has_cycle (bool): If Linked List contains cycle
   		'''
        	slow, fast = head, head.next
        
		while fast and fast.next:
            		slow = slow.next
            		fast = fast.next.next

            		if slow == fast:
                		return True
        	return False

	def findDuplicate(self, nums: List[int]) -> int:
		'''Find duplicate in list

    		Space Complexity: O(1) -> Pointers
      		Time Complexity: O(n) -> Two passes over list

 		Args:
   			nums (list): Iterable of numbers

      		Returns:
			ix (int): Index of duplicate
   		'''
		slow, fast = 0, 0

		# Find cycle
        	while True:
            		slow = nums[slow]
            		fast = nums[nums[fast]]

            		if slow == fast:
                		break

        	slow_start = 0

		# Begin again to find cyclic node
        	while slow_start != slow:
            		slow = nums[slow]
            		slow_start = nums[slow_start]

        	return slow

	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
		'''Merge K Linked Lists

  		Space Complexity: O(k) -> Min Heap 
    		Time Complexity: O(n*k) -> Pass over all elements

		Values: Linked Lists (k), Maximum elements (n)

  		Args:
    			lists (list): List of Linked Lists

       		Returns:
	 		out (ListNode): Linked List
    		'''
		c = 0
        	min_heap = []
        
		for cur_list in lists:
            		heapq.heappush(min_heap, (cur_list.val, c, cur_list.next))
            		c += 1
        
        	out = ListNode()
        	res = out
        
		while min_heap:
            		cur = heapq.heappop(min_heap)
            		res.next = ListNode(cur[0])
            		res = res.next

            		cur = cur[2]
            		if cur:
                		heapq.heappush(mh, (cur.val, c, cur.next))
                		c += 1
            
        	return out.next


class LRUNode:
	def __init__(self, key = 0, val = 0, prev = None, nxt = None):
		'''Linked List Node for LRU Cache

  		Args:
    			key (int): Key
       			value (int): Value
	  		prev (LRUNode): Pointer to previous node
     			nxt (LRUNode): Pointer to next node
		'''
		self.key = key
		self.val = val
		self.prev = prev
		self.nxt = nxt

class LRUCache
	def __init__(self, capacity: int):
		'''LRU Cache implementation with Doubly Linked List

  		Space Complexity: O(n) -> Dictionary for keys

      		Args:
			capacity (int): Maximum capacity
		'''
		self.capacity = capacity
		self.cache = {}

		self.left = LRUNode()
		self.right = LRUNode()

		self.left.nxt = self.right
		self.right.prev = self.left

	def remove(self, node: LRUNode):
		'''Helper function to remove node from Linked List

  		Time Complexity: O(1) -> Repoint pointers

    		Args:
      			node (LRUNode): Node to remove
	 	'''
		node.prev.nxt = node.nxt
		node.nxt.prev = node.prev

	def insert(self, node: LRUNode):
		'''Helper function to insert node to Linked List

  		Time Complexity: O(1) -> Repoint pointers

    		Args:
      			node (LRUNode): Node to add
	 	'''
		prev, bound = self.right.prev, self.right

		prev.nxt = node
		node.prev = prev

		node.nxt = bound
		bound.prev = node
		
	def get(self, key: int) -> int:
		'''Access value of key

  		Time Complexity: O(1) -> Dict IO and node move

    		Args:
      			key (int): Key

  		Returns:
    			val (int): Value
	 	'''
		if key in self.cache:
			cur = self.cache[key]
			self.remove(cur)
			self.insert(cur)
			return cur.val
		return -1

	def put(self, key: int, value: int) -> None:
		'''Add key to cache

  		Time Complexity: O(1) -> Dict IO and pointer move

    		Args:
      			key (int): Key
	 		value (int): Value
		'''
		if key in self.cache:
			self.remove(self.cache[key])
		self.cache[key] = LRUNode(key, value)
		self.insert(self.cache[key])

		if len(self.cache) > self.capacity:
			del self.cache[self.left.nxt.key]
			self.remove(self.left.nxt)
			
