import random
import time
import turtle

# Function to generate a random number
def random_num(value):
    value = random.randint(0, value - 1)
    return value

# Function to create a random board
def random_board(board_size, board):
    for x in range(board_size):
        for y in range(board_size):
            if (x % 2) != 0:
                board[x][y] = 1
                if y == board_size - 1:
                    random_path = random_num(board_size)
                    board[x][random_path] = 0
            else:
                board[x][y] = 0

# Funtion to set a random destination to the board
def random_destination(board_size, board):
    x = random_num(board_size)
    y = random_num(board_size)
    if (x % 2) != 0:
        x += 1
    board[x][y] = 3

# Function to find the path from start to destination and assign to the board
def find_and_assign_path(board_size, board):
    queue = [(0, 0, [(0, 0)])]
    visited = set([(0, 0)])

    while queue:
        x, y, path = queue.pop(0)

        if board[x][y] == 3:
            for x, y in path:
                if (x == 0 and y == 0):
                    continue
                elif (board[x][y]!= 3):
                    board[x][y] = 2
            return path + [(x, y)]

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < board_size and 0 <= ny < board_size and (nx, ny) not in visited and board[nx][ny]!= 1:
                queue.append((nx, ny, path + [(nx, ny)]))
                visited.add((nx, ny))

# Function to draw a square in turtle
def draw_square(turtle, side_length, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    turtle.end_fill()

# Function to draw the blue board to turtle
def blue_board(board_size, board, grid_size):
    grid_turtle.penup()
    grid_turtle.goto(-150, 150)
    grid_turtle.pendown()
    y_axis = 150
    for x in range(board_size):
        for y in range(board_size):
            draw_square(grid_turtle, grid_size, "blue")
            grid_turtle.penup()
            grid_turtle.forward(grid_size)
            grid_turtle.pendown()
        grid_turtle.penup()
        grid_turtle.goto(-150, y_axis - grid_size)
        grid_turtle.pendown()
        y_axis = y_axis - grid_size
    grid_turtle.hideturtle()

# Function to draw the board to turtle
def draw_board(board_size, board, grid_size):
    grid_turtle.penup()
    grid_turtle.goto(-150, 150)
    grid_turtle.pendown()
    y_axis = 150
    for x in range(board_size):
        for y in range(board_size):
            if x == 0 and y == 0:
                draw_square(grid_turtle, grid_size, "red")
                grid_turtle.penup()
                grid_turtle.forward(grid_size)
                grid_turtle.pendown()
            elif board[x][y] == 0:
                draw_square(grid_turtle, grid_size, "white")
                grid_turtle.penup()
                grid_turtle.forward(grid_size)
                grid_turtle.pendown()
            elif board[x][y] == 1:
                draw_square(grid_turtle, grid_size, "black")
                grid_turtle.penup()
                grid_turtle.forward(grid_size)
                grid_turtle.pendown()
            elif board[x][y] == 2:
                draw_square(grid_turtle, grid_size, "yellow")
                grid_turtle.penup()
                grid_turtle.forward(grid_size)
                grid_turtle.pendown()
            elif board[x][y] == 3:
                draw_square(grid_turtle, grid_size, "green")
                grid_turtle.penup()
                grid_turtle.forward(grid_size)
                grid_turtle.pendown()
        grid_turtle.penup()
        grid_turtle.goto(-150, y_axis - grid_size)
        grid_turtle.pendown()
        y_axis = y_axis - grid_size
    grid_turtle.hideturtle()


#Driver code

board_size = 9
if ((board_size % 2) == 0):
    board_size += 1
board = [[0 for _ in range(board_size)] for _ in range(board_size)]

# Create a turtle to draw the grid
grid_size = 30
grid_turtle = turtle.Turtle()
grid_turtle.speed(0)

#Calling the Functions

random_board(board_size, board)
draw_board(board_size, board, grid_size)
time.sleep(3)

random_destination(board_size, board)
draw_board(board_size, board, grid_size)
time.sleep(3)

blue_board(board_size, board, grid_size)
time.sleep(3)

find_and_assign_path(board_size, board)
draw_board(board_size, board, grid_size)


