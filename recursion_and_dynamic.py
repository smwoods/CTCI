#!/usr/local/bin/python3

# 8.1 Triple Step
def triple_step(n):
	step_ct = [0] * n
	step_ct[0] = 1
	for i in range(1, n):
		if i - 3 >= 0:
			step_ct[i] += step_ct[i-3]
		if i - 2 >= 0:
			step_ct[i] += step_ct[i-2]
		if i - 1 >= 0:
			step_ct[i] += step_ct[i-1]
	return step_ct[n-1]

# 8.2 Robot in a Grid
def robot_in_a_grid(grid):
	rows = len(grid)
	cols = len(grid[0])
	visited = [[0 for _ in range(cols)] for _ in range(rows)]
	visited[0][0] = 1
	path = []
	return get_path(grid, visited, rows-1, cols-1, path)

def get_path(grid, visited, row, col, path):
	if row < 0 or col < 0 or grid[row][col] == 0:
		return False
	else:
		success = False
		if row == 0 and col == 0:
			path += [(row, col)]
			success = True
		elif get_path(grid, visited, row-1, col, path) or get_path(grid, visited, row, col-1, path):
			path += [(row, col)]
			success = True
		visited[row][col] = 1
		return success

def main():
	matrix = [
		[1, 0, 1, 0, 1],
		[1, 1, 1, 1, 1],
		[1, 1, 0, 0, 1],
		[1, 1, 0, 0, 1]
	]
	print(robot_in_a_grid(matrix))

main()