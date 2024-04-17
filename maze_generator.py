import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Maze Generator")
turtle.speed(0)  # Fastest speed
turtle.penup()
turtle.hideturtle()

# Maze dimensions and cell size
cell_size = 20
grid_width = int(screen.window_width() / cell_size)
grid_height = int(screen.window_height() / cell_size)

# Initialize the grid
grid = [[0] * grid_width for _ in range(grid_height)]

# Function to draw a cell at a given position
def draw_cell(x, y):
    screen_x = -screen.window_width() / 2 + x * cell_size
    screen_y = screen.window_height() / 2 - (y + 1) * cell_size
    turtle.goto(screen_x, screen_y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(cell_size)
        turtle.left(90)
    turtle.penup()

def path_exists(x, y):
  if x == grid_width - 1 and y == grid_height - 2:  # Reached the end
      return True
  grid[y][x] = 2  # Mark as visited (different value to distinguish from maze walls)
  for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
      nx, ny = x + dx, y + dy
      if 0 <= nx < grid_width and 0 <= ny < grid_height and grid[ny][nx] == 0:
          if path_exists(nx, ny):
              return True
  return False

def draw_start_end():
  start_x, start_y = 1, 1
  # Check if a path exists from the start
  if path_exists(start_x, start_y):
      turtle.goto(-screen.window_width() / 2 + cell_size / 2, screen.window_height() / 2 - cell_size / 2)
      turtle.dot(cell_size // 2, "green")  # Draw start if path exists

  # Reset grid for checking path to the end
  for y in range(grid_height):
      for x in range(grid_width):
          if grid[y][x] == 2:
              grid[y][x] = 0  # Unmark visited cells from previous check

  end_x, end_y = grid_width - 2, grid_height - 2  # Potential end position
  if path_exists(end_x, end_y):
      turtle.goto(screen.window_width() / 2 - cell_size / 2, -screen.window_height() / 2 + cell_size / 2)
      turtle.dot(cell_size // 2, "red")     # Draw end if path exists

def find_start_position():
  while True:
      start_x, start_y = random.randrange(1, grid_width, 2), random.randrange(1, grid_height, 2)
      if path_exists(start_x, start_y):
          return start_x, start_y

# Recursive backtracking algorithm to generate the maze
def generate_maze(x, y):
    grid[y][x] = 1  # Mark as visited

    # Shuffle directions to randomize maze generation
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx * 2, y + dy * 2  # Check cell two steps away
        if 0 <= nx < grid_width and 0 <= ny < grid_height and grid[ny][nx] == 0:
            grid[y + dy][x + dx] = 1  # Mark intermediate cell as visited
            draw_cell(x + dx, y + dy)  # Draw passage
            generate_maze(nx, ny)  # Recursive call

while True:  # Keep trying until a valid maze is generated
  # Initialize the grid
  grid = [[0] * grid_width for _ in range(grid_height)]

  # Find a suitable start position
  start_x, start_y = find_start_position()

  # Generate the maze
  generate_maze(start_x, start_y)

  # Check if an end position is possible
  end_x, end_y = grid_width - 2, grid_height - 2
  for y in range(grid_height):
      for x in range(grid_width):
          if grid[y][x] == 2:
              grid[y][x] = 0  # Unmark visited cells

  if path_exists(end_x, end_y):
      break  # Valid maze found! Exit the loop

draw_start_end()

turtle.done()
