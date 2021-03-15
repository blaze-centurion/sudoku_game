# !/usr/bin/env python3




import pygame
import sys


pygame.init()

WIDTH, HEIGHT = 550, 550
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


FONT = pygame.font.SysFont('comicsans', 40)


# number_grid = [
# 	[1, 2, 3, 0, 5, 6, 7, 8, 9],
# 	[1, 2, 3, 1, 5, 6, 7, 8, 9],
# 	[1, 2, 3, 2, 5, 6, 7, 8, 9],
# 	[1, 2, 3, 3, 0, 6, 7, 8, 9],
# 	[1, 2, 3, 5, 5, 6, 7, 8, 9],
# 	[1, 2, 3, 6, 5, 6, 7, 8, 9],
# 	[1, 2, 0, 8, 5, 6, 7, 8, 9],
# 	[1, 2, 3, 9, 5, 6, 7, 8, 9],
# 	[1, 2, 0, 1, 5, 6, 1, 8, 9],
# ]

number_grid = [
	[5, 3, 0, 0, 7, 0, 0, 0, 0],
	[6, 0, 0, 1, 9, 5, 0, 0, 0],
	[0, 9, 8, 0, 0, 0, 0, 6, 0],
	[8, 0, 0, 0, 6, 0, 0, 0, 3],
	[4, 0, 0, 8, 0, 3, 0, 0, 1],
	[7, 0, 0, 0, 2, 0, 0, 0, 6],
	[0, 6, 0, 0, 0, 0, 2, 8, 0],
	[0, 0, 0, 4, 1, 9, 0, 0, 5],
	[0, 0, 0, 0, 8, 0, 0, 7, 9]
]


board = [x[:] for x in number_grid]


offset = 20

key_var = 65

SquareColor = (0,255, 0)


pressed = 0


GREY = (230, 230, 230)




print("This is Simple Sudoku Game Made By Roshan: ")
print("Guide:- \nPress R for restart the game\nPress D for Solve Automatically\nPress ESC. to exit the game")
print("Enjoy The Game :)")




def solve_sudoku(grid):


	find = find_empty(grid)
	if find == None:
		return True
	else:
		row, col = find



	for i in range(1,10):
		if validate_number(grid, row+1, col+1, i):

			if solve_sudoku(grid):
				return True

			grid[row][col] = 0

	return  False






def find_empty(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 0:
				return i,j

	return None


def validate_number(grid, row, col, number):

	grid[row-1][col-1] = number


	# Check row
	row_list = []
	ROWS = 9
	for i in range(ROWS):
		row_list.append(grid[i][col-1])

	same_no_in_row = [x for x in range(len(row_list)) if row_list[x] == number ]


	if len(same_no_in_row) != 1:
		grid[row-1][col-1] = 0
		return False


	# check col
	col_list = grid[row-1]
	same_no_in_col = [i for i in range(len(col_list)) if col_list[i] == number ]

	if len(same_no_in_col) != 1:
		grid[row-1][col-1] = 0
		return False


	# Check box
	r = row -1
	c = col -1
	bx = r // 3
	by = c // 3

	box_list = []
	for i in range(bx * 3, bx * 3 + 3):
		for j in range(by * 3, by * 3 + 3):
			box_list.append(grid[i][j])

	same_no_in_box = [i for i in range(len(box_list)) if box_list[i] == number]

	if len(same_no_in_box) != 1:
		grid[row-1][col-1] = 0
		return False

	return True


solved_grid = [x[:] for x in number_grid]
solved_board = solve_sudoku(solved_grid)


def reset():
	global board
	board = [x[:] for x in number_grid]
	return



def get_row_col(x,y):

	ROWS, COLS = 9,9
	row = 0
	col = 0
	i = 1
	j = 1

	for row in range(ROWS):
		if (y < i*61):
			row = i
			break
		i+=1

	for col in range(COLS):
		if (x < j*61):
			col = j
			break
		j+=1

	return row, col





def blit_number():
	ROWS, COLS = 9, 9


	for row in range(ROWS):
		for col in range(COLS):
			number = int(board[row][col])
			if number_grid[row][col] == 0:
				pygame.draw.rect(WIN, pygame.Color("white"), (col * 61, row * 61, 61,61))
			if number !=0:
				text = FONT.render(str(number), True, pygame.Color("black"))
			else:
				text = FONT.render("", True, pygame.Color("black"))
			WIN.blit(text, (col*61 + offset, row*61 + offset))




def get_row_col_of_square(x,y):
	row, col = get_row_col(x,y)
	return row, col


def get_pos(row, col):
	posX = (col-1)*61
	posY = (row-1)*61

	return posX, posY



def get_numbers(key):
	key_list = [49, 50, 51, 52, 53, 54, 55, 56, 57]
	if key in key_list:
		return chr(key)
	else:
		return 0



def add_numbers(row, col):
	global SquareColor
	key = key_var
	number = get_numbers(key)


	if number_grid[row-1][col-1] == 0 and number !=  0:
		valid = validate_number(board, row, col, int(number))
		if valid:
			SquareColor = (0,255, 0)
		else:
			SquareColor = (255,0,0)

	elif number_grid[row-1][col-1] == 0 and number == 0:
		board[row-1][col-1] = 0
		return
	else:
		return




def draw_square(row, col):
	posX, posY = get_pos(row, col)
	pygame.draw.rect(WIN, SquareColor, (posX, posY, 61, 61), 5 )
	return posX, posY




def draw(row, col):
	WIN.fill(GREY)
	blit_number()
	i = 1
	while i < 9:
		line_width = 2 if (i%3 != 0) else 4
		pygame.draw.line(WIN, pygame.Color("black"), (i*61, 0), (i*61, HEIGHT),  line_width)
		pygame.draw.line(WIN, pygame.Color("black"), (0, i*61), (HEIGHT, i*61),  line_width)

		i+=1

	draw_square(row, col)

	pygame.display.update()





def main():
	global key_var
	global pressed
	global board

	row, col = 0,0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				x,y = pygame.mouse.get_pos()
				row, col = get_row_col(x,y)
			if event.type == pygame.KEYDOWN:
				key_var = event.key

				add_numbers(row, col)

				if event.key == pygame.K_r:
					reset()

				if event.key == pygame.K_d:
					board = solved_grid
					print("Solved")



		draw(row, col)


main()
