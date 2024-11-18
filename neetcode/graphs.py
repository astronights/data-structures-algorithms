# Graphs Solutions
from collections import deque

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

