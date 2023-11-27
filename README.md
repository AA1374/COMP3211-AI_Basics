# Assignment 2 : README

This assignment consists of two problems. The first problem is related to image processing and segmentation via features from FCN and K-means, while the second problem is about implementing the A* algorithm for maze solving.

Problem 1:
1. Importing the Libraries and Preprocessing the data
2. Implementing the K-means Clustering Algorithm
3. Finding out the colors of cluster centers
4. Show the segmented images
5. Show segmented images for different values of K = 2, 4, 6, 8, 10

Observation:
As the number of iterations in K Means Clustering increase, more colors are analyzed for image segmentation, i.e., as k increases, image segmentation improves.


# Problem 2: A* for Maze Searching

This is a Python script that solves a maze using the A* algorithm. It takes a maze file as an input and outputs the path and nodes explored during the search process.

## Usage

To run the script, use the following command:

```
python3 SID_problem2.py -m <maze_file> -p <path_file> -n <nodes_file>
```

- `<maze_file>`: The path to the maze file.
- `<path_file>`: The path to the output path file.
- `<nodes_file>`: The path to the output nodes file.

By default, heuristic is set to h3. You can change the heuristic by modifying the below line. 

```
heuristic = "h3" 
```

## Maze File Format

The maze file should be a text file representing the maze. Each line represents a row in the maze, and each element in a line represents a cell in the maze. The values in the maze file can be `0` for empty cells and `1` for walls.

Example maze file:
```
0 0 1 1 1
1 0 0 0 1
1 0 1 0 1
1 0 0 0 1
1 1 1 0 0
```

## Output Files

The script outputs two files: the path file and the nodes file.

### Path File

The path file contains the path from the start position to the goal position. Each line represents a row in the maze, and each element in a line represents a cell in the maze. The values in the path file can be `0` for empty cells, `1` for walls, and `2` for cells in the path.

Example path file:
```
2 2 1 1 1
1 2 0 0 1
1 2 1 0 1
1 2 2 2 1
1 1 1 2 2
```

### Nodes File

The nodes file contains the nodes explored during the search process. Each line represents a row in the maze, and each element in a line represents a cell in the maze. The values in the nodes file can be `0` for empty cells, `1` for walls, and `3` for nodes explored during the search process.

Example nodes file:
```
3 3 1 1 1
1 3 0 0 1
1 3 1 0 1
1 3 3 3 1
1 1 1 3 3
```

## Algorithm

The script uses the A* algorithm to navigate through the maze. It starts from the start position and tries to find a path to the goal position. The algorithm uses different heuristics to estimate the cost of reaching the goal from a given position.


1. Read the maze from the file
2. Visualize the path and nodes
3. Implement the A* algorithm for maze solving

Breakdown of `a_star_algorithm` function:
1. Define three heuristic functions
2. Initialize visited set and heap
3. Push start node, cost, and path to heap
4. While loop until heap is empty
5. Check if current node is goal node, already visited, or unvisited
6. Retrieve neighboring nodes of current node
7. Calculate new cost and path for neighboring nodes
8. Push neighboring nodes to heap depending on selected heuristic
9. Return path and visited nodes or empty lists if no path to goal node is found

The overall function performs the A* algorithm by iteratively exploring the nodes in the maze, finding the shortest path from the start node to the goal node.


```python

```
