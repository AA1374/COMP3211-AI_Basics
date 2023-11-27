import argparse
import heapq
import math

def read_maze(file_path):
    with open(file_path, 'r') as file:
        dimensions = file.readline()  # Read the dimensions line and discard it
        maze = [list(map(int, line.strip().split())) for line in file.readlines()]
    return maze

def write_output(maze, path, nodes, student_id):
    path_maze = [row.copy() for row in maze]
    nodes_maze = [row.copy() for row in maze]

    for p in path:
        path_maze[p[0]][p[1]] = 2

    for n in nodes:
        nodes_maze[n[0]][n[1]] = 3

    with open("path_file.txt", 'w') as file:
        file.write(str(student_id) + '\n')
        for row in path_maze:
            file.write(''.join(map(str, row)) + '\n')

    with open("nodes_file.txt", 'w') as file:
        file.write(str(student_id) + '\n')
        for row in nodes_maze:
            file.write(''.join(map(str, row)) + '\n')


def a_star_algorithm(maze, start, goal, heuristic):
    """
    Navigate through a maze using the A* algorithm.

    Parameters:
    - maze (list of lists): A 2D list representing the maze.
    - start (tuple): A tuple of (row, col) indicating the starting point.
    - goal (tuple): A tuple of (row, col) indicating the goal point.

    Returns:
    - path: A list of tuples representing the path from start to goal. Returns an empty list if no path is found.
    - nodes: A list of tuples representing the nodes explored during the search process. Returns an empty list if no path is found.
    """
    # Define the heuristic functions
    def h1(node):
        return 0

    def h2(node):
        return (node[0] - goal[0]) + (node[1] - goal[1])

    def h3(node):
      return math.sqrt((node[0] - goal[0])**2 + (node[1] - goal[1])**2)

    # Initialize data structures
    visited = set()
    heap = []
    if(heuristic == "h1"):
      heapq.heappush(heap, (h1(start), 0, start, []))
    # Manhattan Distance
    elif(heuristic == "h2"):
      heapq.heappush(heap, (h2(start), 0, start, []))
    # Euclidean Distance
    elif(heuristic == "h3"):
      heapq.heappush(heap, (h3(start), 0, start, []))
    else:
      print("Wrong heuristic.")
      return

    while heap:
        _, cost, current, path = heapq.heappop(heap)

        if current == goal:
            visited.add(current)
            return path + [current], list(visited)

        if current in visited:
            continue

        visited.add(current)

        for neighbor in get_neighbors(current, maze):
            new_cost = cost + 1
            new_path = path + [current]
            if heuristic == "h1":
                heapq.heappush(heap, (new_cost + h1(neighbor), new_cost, neighbor, new_path))
            elif heuristic == "h2":
                heapq.heappush(heap, (new_cost + h2(neighbor), new_cost, neighbor, new_path))
            elif heuristic == "h3":
                heapq.heappush(heap, (new_cost + h3(neighbor), new_cost, neighbor, new_path))

    return [], []


def get_neighbors(node, maze):
    """
    Get the neighboring nodes of a given node in the maze.

    Parameters:
    - node (tuple): A tuple of (row, col) indicating the current node.
    - maze (list of lists): A 2D list representing the maze.

    Returns:
    - neighbors: A list of tuples representing the neighboring nodes.
    """
    rows, cols = len(maze), len(maze[0])
    row, col = node

    neighbors = []
    if row > 0 and maze[row - 1][col] == 0:  # Up
        neighbors.append((row - 1, col))
    if row < rows - 1 and maze[row + 1][col] == 0:  # Down
        neighbors.append((row + 1, col))
    if col > 0 and maze[row][col - 1] == 0:  # Left
        neighbors.append((row, col - 1))
    if col < cols - 1 and maze[row][col + 1] == 0:  # Right
        neighbors.append((row, col + 1))

    return neighbors


# maze = [[0, 0, 1, 1, 1],
#         [1, 0, 0, 0, 1],
#         [1, 0, 1, 0, 1],
#         [1, 0, 0, 0, 1],
#         [1, 1, 1, 0, 0]]

# start = (0, 0)
# goal = (4, 4)

# heuristic = "h3"

# path, nodes = a_star_algorithm(maze, start, goal, heuristic)
# print("Path:", path)
# print("Nodes:", nodes)

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--maze", help="Path to the maze file", required=True)
    parser.add_argument("-p", "--path", help="Path to the output path file", required=True)
    parser.add_argument("-n", "--nodes", help="Path to the output nodes file", required=True)
    args = parser.parse_args()

    # Read the maze from the input file
    maze = read_maze(args.maze)

    # Define the start and goal positions
    start = (0, 0)
    goal = (len(maze) - 1, len(maze[0]) - 1)

    # Define the heuristic to use
    heuristic = "h3"    # Find the path and nodes using the A* algorithm
    path, nodes = a_star_algorithm(maze, start, goal, heuristic)

    # Write the output to files
    write_output(maze, path, nodes, "SID")

    # Print the path and nodes for visualization
    print("Path:", path)
    print("Nodes:", nodes)

if __name__ == "__main__":
    main()