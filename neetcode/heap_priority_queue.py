# Heap / Priority Queue Solutions
import math
import heapq
from collections import defaultdict

class KthLargest:

	def __init__(self, k: int, nums: List[int]):
		'''K-th Largest element in stream

  		Space Complexity: O(k) -> Min Heap
    		Time Complexity: O(n) -> Heapify

      		Args:
			k (int): Index of largest element
   			nums (list): Stream of numbers
      		'''
		self.k = k
        	self.heap = nums[:]
        	
		heapq.heapify(self.heap)
        	while len(self.heap) > k:
            		heapq.heappop(self.heap)

	def add(self, val: int) -> int:
		'''Add Value to heap and return K-th largest

  		Time Complexity: O(log k) -> Heap IO

  		Args:
    			val (int): Value to add

       		Returns:
	 		kth (int): K-th largest number
    		'''
        	heapq.heappush(self.heap, val)
        	if len(self.heap) > self.k:
            		heapq.heappop(self.heap)
        	return self.heap[0]

class Solution:
	# Solution Functions
	
	def lastStoneWeight(self, stones: List[int]) -> int:
		'''Last Stone Weight after smashing

  		Space Complexity: O(n) -> Stone Weight Heap
    		Time Complexity: O(n log n) -> Heap IO

      		Args:
			stones (list): Iterable of weights

   		Returns:
     			out (int): Remaining stone
		'''
        	stones = [-x for x in stones]
        	heapq.heapify(stones)

        	while len(stones) > 1:
            		a = heapq.heappop(stones)
			b = heapq.heappop(stones)

            		diff = abs(a - b)
			if diff:
                		heapq.heappush(stones, -diff)

        	return -stones[0] if stones else 0


	def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
		'''K Closest Points to Origin

  		Space Complexity: O(k) -> Point Heap
    		Time Complexity: O(n log k) -> Heap IO

      		Args:
			points (list): Iterable of co-ordinates
   			k (int): Index of closest points

      		Returns:
			c_points (list): K Closest Points
   		'''
        	min_heap = []
        
		for p in points:
            		x, y = p[0], p[1]
            		d = math.sqrt(x**2 + y**2)
            		heapq.heappush(min_heap, (-d, x, y))

            		if len(min_heap) > k:
                		heapq.heappop(min_heap)

        	return [[p[1], p[2]] for p in min_heap]

	def findKthLargest(self, nums: List[int], k: int) -> int:
		'''Find K-th largest element in array

  		Space Complexity: O(k) -> Element Heap
    		Time Complexity: O(n log k) -> Heap IO

      		Args:
			nums (list): Iterable of elements
   			k (int): Index of largest element

      		Returns:
			elem (int): K-th largest element
   		'''
        	min_heap = []
        
		for n in nums:
            		heapq.heappush(min_heap, n)

            		if len(min_heap) > k:
                		heapq.heappop(min_heap)

        	return min_heap[0]


	def leastInterval(self, tasks: List[str], n: int) -> int:
		'''Task Scheduling Least Interval

  		Space Complexity: O(1) -> List of 26
    		Time Complexity: O(n) -> Task iteration

  		Args:
    			tasks (list): Iterable of tasks A-Z
       			n (int): Waiting interval

   		Returns:
     			total_time (int): Total Time taken
		'''
        	count = [0] * 26
        	for t in tasks:
            		count[ord(t) - ord('A')] += 1

        	count.sort(reverse = True)

        	maxf = count[0]
        	idle = (maxf - 1) * n

        	for t in count[1:]:
            		if t == maxf:
                		idle += 1
            		idle -= t

        	return max(0, idle) + len(tasks)


class Twitter:

	def __init__(self):
		'''Design Twitter

		Space Complexity: O(m * n) -> Users and Tweets

  		Values: Number of Users (m), number of tweets (n)
  		'''
        	self.count = 0
        	self.tweets = defaultdict(list)
        	self.follows = defaultdict(set)

	def postTweet(self, userId: int, tweetId: int) -> None:
		'''Post Tweet

  		Time Complexity: O(1) -> List Append

    		Args:
      			userId (int): User 
	 		tweetId (int): Tweet
    		'''
        	self.tweets[userId].append((self.count, tweetId))
        	self.count -= 1

	def getNewsFeed(self, userId: int) -> List[int]:
		'''Get Top 10 Tweets for User

  		Time Complexity: O(m + log n) -> Tweet Iteration

    		Values: Number of users (m), Number of tweets (n)

      		Args:
			userId (int): User

   		Returns:
     			feed (list): Tweet Ids
		'''
        	feed = []
        	post_heap = []
        	self.follows[userId].add(userId)

        	for follower in self.follows[userId]:
            		if follower in self.tweets:
                		ix = len(self.tweets[follower]) - 1
                		c, tid = self.tweets[follower][ix]
                		heapq.heappush(post_heap, [c, tid, follower, ix])

        	while post_heap and len(feed) < 10:
            		c, tid, follower, ix = heapq.heappop(post_heap)
            		feed.append(tid)
            		
			if ix > 0:
                		c, tid = self.tweets[follower][ix - 1]
                		heapq.heappush(post_heap, [c, tid, follower, ix - 1])
        	return feed
            

    	def follow(self, followerId: int, followeeId: int) -> None:
		'''Add Follow connection

  		Time Complexity: O(1) -> Set Add

    		Args:
      			followerId (int): Follower
	 		followeeId (int): Followee
		'''
        	self.follows[followerId].add(followeeId)

	def unfollow(self, followerId: int, followeeId: int) -> None:
		'''UnFollow connection

  		Time Complexity: O(1) -> Set Remove

    		Args:
      			followerId (int): Follower
	 		followeeId (int): Followee
		'''
        	if followeeId in self.follows[followerId]:
            		self.follows[followerId].remove(followeeId)
