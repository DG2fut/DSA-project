from collections import deque
import heapq
import random

# This code can be used to create a maze at random
''' import random

def create_maze(rows, cols):
    maze = [[1 for i in range(cols)] for j in range(rows)]
    
    start_row = random.randint(0, rows-1)
    start_col = random.randint(0, cols-1)
    
    end_row = random.randint(0, rows-1) 
    end_col = random.randint(0, cols-1)
    
    while end_row == start_row and end_col == start_col:
        end_row = random.randint(0, rows-1)
        end_col = random.randint(0, cols-1)
        
    maze[start_row][start_col] = 0
    maze[end_row][end_col] = 0
    
    return maze, (start_row, start_col), (end_row, end_col)
'''

# Define the maze
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Define the starting and ending positions
start = (1, 1)
end = (8, 8)

# Define the possible movements (up, down, left, right)
movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# maze, start, end = create_maze(10, 10)

def print_path(path, visited_count):
    if path:
        print("Path found:")
        for cell in path:
            print(cell)
        print("Number of nodes visited:", visited_count)
    else:
        print("No path found.")

def bfs(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start, [])])
    visited_count = 0

    while queue:
        current, path = queue.popleft()
        x, y = current

        if current == end:
            return path + [current], visited_count

        if visited[x][y]:
            continue

        visited[x][y] = True
        visited_count += 1

        for dx, dy in movements:
            new_x = x + dx
            new_y = y + dy

            if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y] and maze[new_x][new_y] == 0:
                queue.append(((new_x, new_y), path + [current]))

    return None, visited_count

def dfs(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    stack = [(start, [])]
    visited_count = 0

    while stack:
        current, path = stack.pop()
        x, y = current

        if current == end:
            return path + [current], visited_count

        if visited[x][y]:
            continue

        visited[x][y] = True
        visited_count += 1

        for dx, dy in movements:
            new_x = x + dx
            new_y = y + dy

            if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y] and maze[new_x][new_y] == 0:
                stack.append(((new_x, new_y), path + [current]))

    return None, visited_count

def heuristic(position, end):
    x1, y1 = position
    x2, y2 = end
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    cost_so_far = {start: 0}
    came_from = {}  
    visited_count = 0

    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        x, y = current

        if current == end:
            path = [current]
            while current != start:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, visited_count

        if visited[x][y]:
            continue

        visited[x][y] = True
        visited_count += 1

        for dx, dy in movements:
            new_x = x + dx
            new_y = y + dy

            if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y] and maze[new_x][new_y] == 0:
                new_cost = cost_so_far[current] + 1
                if (new_x, new_y) not in cost_so_far or new_cost < cost_so_far[(new_x, new_y)]:
                    cost_so_far[(new_x, new_y)] = new_cost
                    heapq.heappush(priority_queue, (new_cost + heuristic((new_x, new_y), end), (new_x, new_y)))
                    came_from[(new_x, new_y)] = current  

    return None, visited_count

def dijkstra(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    cost_so_far = {start: 0}
    came_from = {}  
    visited_count = 0

    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        x, y = current

        if current == end:
            path = [current]
            while current != start:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, visited_count

        if visited[x][y]:
            continue

        visited[x][y] = True
        visited_count += 1

        for dx, dy in movements:
            new_x = x + dx
            new_y = y + dy

            if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y] and maze[new_x][new_y] == 0:
                new_cost = cost_so_far[current] + 1
                if (new_x, new_y) not in cost_so_far or new_cost < cost_so_far[(new_x, new_y)]:
                    cost_so_far[(new_x, new_y)] = new_cost
                    heapq.heappush(priority_queue, (new_cost, (new_x, new_y)))
                    came_from[(new_x, new_y)] = current  

    return None, visited_count



# Solve the maze using BFS
path, visited_count = bfs(maze, start, end)
print("BFS:")
print_path(path, visited_count)
print()

# Solve the maze using DFS
path, visited_count = dfs(maze, start, end)
print("DFS:")
print_path(path, visited_count)
print()

# Solve the maze using A*
path, visited_count = a_star(maze, start, end)
print("A*:")
print_path(path, visited_count)
print()

# Solve the maze using Dijkstra's algorithm
path, visited_count = dijkstra(maze, start, end)
print("Dijkstra's:")
print_path(path, visited_count)
