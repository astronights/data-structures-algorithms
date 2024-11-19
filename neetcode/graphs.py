# Graphs Solutions
from collections import deque

class Node:
	def __init__(self, val = 0, neighbors = None):
		'''Graph Node

    		Args:
      			val (int): Node Value
	 		neighbors (list): Neighboring nodes
		'''
        	self.val = val
        	self.neighbors = neighbors if neighbors is not None else []

class Solution:
	# Solution Functions

	def numIslands(self, grid: List[List[str]]) -> int:
		'''Calculate number of islands

  		Space Complexity: O(m * n) -> Grid shape
    		Time Complexity: O(m * n) -> BFS

      		Values: Grid dimensions (m x n)

      		Args:
			grid (list): Geographical grid

    		Returns:
      			n_isles (int): Number of islands
	 	'''
        	n_isles = 0
        	R, C = len(grid), len(grid[0])
        	dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
		for i in range(R):
            		for j in range(C):
                		if grid[i][j] == '1':
                    			n_isles += 1
                    			seen = set()
                    			island = deque([(i, j)])
                    
					while island:
						# Explore current cell
                        			x, y = island.popleft()
                        			if (x, y) in seen:
                            				continue
                        			seen.add((x, y))
                        			grid[x][y] = '0'

						# Add neighbouring land cells to queue
						for dx, dy in dirs:
                            				nx, ny = x + dx, y + dy
                            				if (nx >= 0 and nx < R 
							    and ny >= 0 and ny < C 
							    and grid[nx][ny] == '1'):
                                				island.append((nx, ny))
        	return n_isles


	def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
		'''Maximum area of island

  		Space Complexity: O(m * n) -> Grid shape
    		Time Complexity: O(m * n) -> BFS

      		Values: Grid dimensions (m x n)

  		Args:
    			grid (list): Grid

       		Returns:
	 		max_area (int): Maximum area of island
    		'''
        	max_area = 0
        	seen = set()
        	R, C = len(grid), len(grid[0])
        	dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
		for i in range(R):
            		for j in range(C):
                		if grid[i][j] == 1:
                    			cur_area = 0
                    			queue = deque([(i, j)])

					# BFS
					while queue:
                        			x, y = queue.popleft()
                        			if (x, y) in seen:
                            				continue
                        			cur_area += 1
                        			seen.add((x, y))

                        			for dx, dy in dirs:
                            				nx, ny = x + dx, y + dy

                            				if (nx >= 0 and nx < R 
							    and ny >= 0 and ny < C 
							    and grid[nx][ny] == 1):
                                				queue.append((nx, ny))

                    			max_area = max(max_area, cur_area)
		return max_area

	def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
		'''Clone Graph

  		Space Complexity: O(V) -> V Nodes
    		Time Complexity: O(V + E) -> Nodes + Edges

      		Values: Vertices (V), Edges (E)

      		Args:
			node (Node): Graph Node

   		Returns:
     			copy_node (Node): Copied Graph Node
		'''		
        	if not node:
            		return None
        	nodes = {}
        	queue = deque([node])
        
		while queue:
            		cur = queue.popleft()
            		nodes[cur] = Node(cur.val)
            		
			for n in cur.neighbors:
                		if n not in nodes:
                    			queue.append(n)
        
        	for key in nodes.keys():
            		nodes[key].neighbors = [nodes[x] for x in key.neighbors]

        	return nodes[node]

	def islandsAndTreasure(self, grid: List[List[int]]) -> None:
		'''Distance to Treasure Chests

  		Space Complexity: O(m * n) -> Grid shape
    		Time Complexity: O(m * n) -> BFS

      		Values: Grid dimensions (m x n)

 		Args:
   			grid (list): Geaographical Grid
		'''
		queue = deque()
        	R, C = len(grid), len(grid[0])
        	
        	for i in range(R):
            		for j in range(C):
                		if grid[i][j] == 0:
                    			queue.append((i, j, 0))

		seen = set()
        	dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        	while queue:
            		x, y, d = queue.popleft()
            
            		if (x, y) in seen:
                		continue

			grid[x][y] = d
            		seen.add((x, y))

            		for dx, dy in dirs:
                		nx, ny = x + dx, y + dy
                
                	if (nx >= 0 and nx < R 
			    and ny >= 0 and ny < C 
			    and grid[nx][ny] == 2147483647):
                    		queue.append((nx, ny, d + 1))

	def orangesRotting(self, grid: List[List[int]]) -> int:
		'''Time to rot all fruits

  		Space Complexity: O(m * n) -> Grid shape
    		Time Complexity: O(m * n) -> BFS

      		Values: Grid dimensions (m x n)

 		Args:
   			grid (list): Grid of fruits

      		Returns:
			max_d (int): Time to rot
   		'''
        	n_fresh = 0
		queue = deque()
        	R, C = len(grid), len(grid[0])
        
        	for i in range(R):
            		for j in range(C):
                		if grid[i][j] == 1:
                    			n_fresh += 1
                		elif grid[i][j] == 2:
                    			queue.append((i, j, 0))

		max_d = 0
        	seen = set()
        	dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

	        while queue:
            		x, y, d = queue.popleft()

            		if (x, y) in seen:
                		continue

            		n_fresh -= min(1, d)
            		seen.add((x, y))

            		max_d = max(max_d, d)

            		for dx, dy in dirs:
                		nx, ny = x + dx, y + dy

                		if (nx >= 0 and nx < R 
				    and ny >= 0 and ny < C 
				    and grid[nx][ny] == 1):
                    			queue.append((nx, ny, d + 1))

        	return max_d if n_fresh == 0 else -1
