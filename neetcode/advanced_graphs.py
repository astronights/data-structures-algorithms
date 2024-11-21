# Advanced Graphs Solutions
import heapq
from collections import defaultdict

class Solution:
	# Solution Functions

	def findItinerary(self, tickets: List[List[str]]) -> List[str]:
		'''Build complete Itinerary

  		Space Complexity: O(n) -> Number of edges
    		Time Complexity: O(n log n) -> Tim Sort

      		Args:
			tickets (list): Ticket edges

   		Returns:
     			route (list): Itinerary
		'''
        	paths = defaultdict(list)
        
		for src, dst in tickets:
            		paths[src].append(dst)
		for src in paths:
            		paths[src].sort(reverse=True)

        	stack = ['JFK']
        	route = []

        	while stack:
            		cur = stack[-1]
            		if paths[cur]:
                		stack.append(paths[cur].pop())
            		else:
                		route.append(stack.pop())

        	return route[::-1]

	def minCostConnectPoints(self, points: List[List[int]]) -> int:
		'''Minimum cost to connect all points

  		Space Complexity: O(n ^ 2) -> Min Heap of All Pairs
    		Time Complexity: O (n ^ 2 * log n) -> All Pairs Heap IO

      		Args:
			points (list): Iterable of co-ordinates

   		Returns:
     			cost (int): Minimum cost
		'''
        	n = len(points)
        	dists = defaultdict(list)
        
		for i in range(n):
            		for j in range(i+1, n):
                		a, b = points[i]
                		x, y = points[j]
				d = abs(a-x) + abs(b-y)
                
				dists[i].append((d, j))
                		dists[j].append((d, i))

        	cost = 0
        	seen = set()
        	min_heap = [(0, 0)]

        	while len(seen) < n:
            		d, cur = heapq.heappop(min_heap)

            		if cur in seen:
                		continue
            
            		cost += d
            		seen.add(cur)

            		for p in dists[cur]:
                		heapq.heappush(min_heap, p)
        	return cost

	def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
		'''Calculate network delay time

  		Space Complexity: O(V + E) -> DFS
    		Time Complexity: O(E * log V) -> Heap IO

      		Values: Number of nodes (V), number of edges (E)

      		Args:
			times (list): Edge timings
   			n (int): Number of nodes
      			k (int): Starting node

  		Returns:
    			min_time (int): Minimum propagation time
       		'''
        	paths = {i: [] for i in range(1, n + 1)}
        	for u, v, t in times:
            		paths[u].append((t, v))

        	min_time = 0
        	seen = set()
        	min_heap = [(0, k)]

        	while len(seen) < n and min_heap:
            		t, v = heapq.heappop(min_heap)
            		if v in seen:
                		continue

            		min_time = t
            		seen.add(v)

            		for node in paths[v]:
				if node[1] not in seen:
                			heapq.heappush(min_heap, (node[0] + t, node[1]))

        	return min_time if len(seen) == n else -1

	def swimInWater(self, grid: List[List[int]]) -> int:
		'''Swim in Rising Water

  		Space Complexity: O(n ^ 2) -> Grid dimensions
    		Time Complexity: O(n ^ 2 * log n) -> BFS + Heap IO

      		Args:
			grid (list): Square matrix of heights

   		Returns:
     			t (int): Minimum time to swim
		'''
        	R, C = len(grid), len(grid[0])

        	t = 0
        	seen = set()
        	min_heap = [(grid[0][0], 0, 0)]

        	dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        	while min_heap:
            		t, x, y = heapq.heappop(min_heap)

            		if x == R - 1 and y == C - 1:
                		return t

            		if (x, y) in seen:
                		continue
			seen.add((x, y))

            	for dx, dy in dirs:
                	nx, ny = x + dx, y + dy
                	if nx >= 0 and nx < R and ny >= 0 and ny < C:
                    		heapq.heappush(min_heap, (max(t, grid[nx][ny]), nx, ny))
				
