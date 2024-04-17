<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->

- [Maze Generator](#maze-generator)
   * [Algorithm Overview](#algorithm-overview)
   * [Easy Code Explanation](#easy-code-explanation)
      + [Initialization](#initialization)
      + [Drawing Functions](#drawing-functions)
      + [Maze Generation](#maze-generation)
      + [Path Existence Checking](#path-existence-checking)
      + [Main Loop](#main-loop)
   * [Dependencies](#dependencies)
   * [Advanced Code Explanation](#advanced-code-explanation)
   * [Usage](#usage)

<!-- TOC end -->


<!-- TOC --><a name="maze-generator"></a>
# Maze Generator
This Python script generates a maze using the recursive backtracking algorithm. It utilizes the Turtle module for visualization. The maze consists of cells represented by squares, with passages connecting adjacent cells. The algorithm ensures that there is a clear path from the starting point to the ending point within the maze.

<!-- TOC --><a name="algorithm-overview"></a>
## Algorithm Overview
The maze generation algorithm used in this script is recursive backtracking. It works as follows:

1. Start from a cell in the grid.
2. Randomly choose a neighboring cell that has not been visited.
3. Move to the chosen cell, marking the current cell and the chosen cell as visited.
4. Repeat steps 2 and 3 recursively until there are no unvisited neighboring cells.
5. Backtrack to the previous cell that has unvisited neighbors and repeat steps 2-4.
6. Continue this process until all cells have been visited.
This algorithm ensures that the maze is fully connected, meaning there is a path between any two cells.

<!-- TOC --><a name="easy-code-explanation"></a>
## Easy Code Explanation
<!-- TOC --><a name="initialization"></a>
### Initialization
- The script initializes the Turtle screen with dimensions 600x600 pixels.
- It sets the cell size to 20 pixels and calculates the number of cells based on the screen dimensions.
- The grid is initialized as a 2D list with all cells initially set to 0, representing unvisited cells.
<!-- TOC --><a name="drawing-functions"></a>
### Drawing Functions
- draw_cell(x, y): Draws a cell at the given position (x, y) on the screen.
- draw_start_end(): Draws the start and end points of the maze. It checks if there is a path from the start point to the end point using the path_exists() function.
<!-- TOC --><a name="maze-generation"></a>
### Maze Generation
- generate_maze(x, y): Implements the recursive backtracking algorithm to generate the maze. It starts from the given position (x, y) and explores neighboring cells recursively.
- find_start_position(): Finds a suitable starting position for maze generation. It ensures that there is a clear path from the starting point to the ending point.
<!-- TOC --><a name="path-existence-checking"></a>
### Path Existence Checking
- path_exists(x, y): Checks if there is a path from the given position (x, y) to the end of the maze. It uses depth-first search (DFS) to explore possible paths.
<!-- TOC --><a name="main-loop"></a>
### Main Loop
- The script continuously generates mazes until it finds a valid maze where there is a path from the starting point to the ending point.
- Once a valid maze is generated, it draws the start and end points and displays the maze on the screen.
<!-- TOC --><a name="dependencies"></a>
## Dependencies
- Python 3.x
- Turtle module (standard library)

<!-- TOC --><a name="advanced-code-explanation"></a>
## Advanced Code Explanation

First, for our `path_exists()` function:

Let \( P(x, y) \) represent the existence of a path from point (x, y) to the bottom-right corner of the grid.

```math
P(x, y) = 
\begin{cases} 
    \text{True} & \text{if } x = \text{grid\_width} - 1 \text{ and } y = \text{grid\_height} - 2 \\
    \text{False} & \text{if } \text{grid}[y][x] = 1 \text{ (visited) or } x < 0 \text{ or } y < 0 \text{ or } x \geq \text{grid\_width} \text{ or } y \geq \text{grid\_height} \\
    P(x+1, y) \lor P(x, y+1) \lor P(x-1, y) \lor P(x, y-1) & \text{otherwise}
\end{cases}
```

Where:
- \( \text{grid\_width} \) and \( \text{grid\_height} \) are the width and height of the grid respectively.
- \( \text{grid}[y][x] \) represents the value at position (x, y) in the grid. If it's 0, it means the cell is unvisited and can be traversed. If it's 2, it means the cell has been visited.
- \( P(x, y) \) recursively checks if there is a path to the bottom-right corner from the current position (x, y) by exploring adjacent cells. If any of the adjacent cells leads to the bottom-right corner, the function returns True, indicating a path exists. Otherwise, it returns False.

The `generate_maze()` function generates a maze using a recursive backtracking algorithm.

Let's denote the grid as a 2D array with elements representing the cells. We'll use the following symbols:

- \( G \) represents the grid, where \( G[i][j] \) denotes the cell at row \( i \) and column \( j \).
- \( (x, y) \) represents the current cell being visited.
- \( (dx, dy) \) represents the direction to move from the current cell.
- \( (nx, ny) \) represents the coordinates of the cell two steps away in the direction \( (dx, dy) \).

Now, let \( V(x, y) \) be a function that marks cell \( (x, y) \) as visited. We can define this function as follows:

```math
V(x, y) = 
\begin{cases} 
1 & \text{if the cell at }(x, y)\text{ is visited} \\
0 & \text{otherwise} 
\end{cases}
```

Next, let \( M(x, y) \) be a function that generates a maze starting from cell \( (x, y) \). We can define this function recursively as follows:

```math
M(x, y) = \begin{cases} 
\text{Draw passage at }(x, y) & \text{for each direction }(dx, dy)\text{ in a random order, if } (x + 2dx, y + 2dy)\text{ is within bounds and unvisited, }\\
& \text{then }V(x, y) = 1\text{, draw passage at }(x + dx, y + dy)\text{ and call }M(x + 2dx, y + 2dy) \\
& \text{else do nothing}
\end{cases}
```

Let's represent our main loop.

Let \( F \) be the function representing the Python code. 

\( F \) takes no explicit parameters and returns a boolean value. It operates as follows:

1. It initializes a grid with dimensions \( \text{grid\_width} \times \text{grid\_height} \), where each cell is initially set to 0.
2. It finds a suitable starting position \( (start\_x, start\_y) \) within the grid.
3. It generates a maze starting from the position \( (start\_x, start\_y) \) using the function \( \text{generate\_maze} \).
4. It marks the start position as the end position, \( (end\_x, end\_y) \), which is set to \( (\text{grid\_width} - 2, \text{grid\_height} - 2) \).
5. It iterates through each cell in the grid, resetting any cells marked as visited (value 2) to unmarked (value 0).
6. It checks if a path exists from the start position to the end position using the function \( \text{path\_exists} \).
7. If a path exists, it breaks out of the loop, indicating a valid maze has been generated.

Now, let's represent this process symbolically:

```math
F() = \begin{cases} 
\text{True} & \text{if a valid maze is generated} \\
\text{False} & \text{otherwise}
\end{cases}
```

Where \( F \) is the function described above. The functions \( \text{generate\_maze} \) and \( \text{path\_exists} \) are assumed to be defined elsewhere.

<!-- TOC --><a name="usage"></a>
## Usage
1. Make sure Python is installed on your system.
2. Run the script in a Python environment.
3. The maze will be displayed on the screen with the start and end points marked.

Enjoy exploring the generated mazes!
