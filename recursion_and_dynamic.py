#!/usr/local/bin/python3
from copy import deepcopy

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
	if get_path(grid, visited, rows-1, cols-1, path):
		return path
	else:
		return False

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

# 8.3 Magic Index
def magic_index(arr, start=0, end=None):
	if end == None: 
		end = len(arr) - 1
	if end < start:
		return -1
	mid = (start + end) // 2
	if arr[mid] == mid:
		return mid
	
	left_index = min(arr[mid], mid-1)
	left = magic_index(arr, start, left_index)
	if left >= 0:
		return left
	right_index = max(arr[mid], mid+1)
	right = magic_index(arr, right_index, end)
	return right

# 8.4 Power Set
def power_set(in_set):
	
	if len(in_set) == 1:
		return [in_set, []]
	return_set = []
	item = in_set.pop()
	not_included = power_set(in_set)
	included = deepcopy(not_included)
	for subset in included:
		subset.append(item)
	return_set += included
	return_set += not_included
	return return_set


def main():
	# matrix = [
	# 	[1, 0, 1, 0, 1],
	# 	[1, 1, 0, 1, 1],
	# 	[1, 1, 0, 0, 1],
	# 	[1, 0, 0, 0, 1],
	# 	[1, 1, 1, 0, 1],
	# ]
	# magic = [-10, -5, 0, 1, 3, 5, 7, 9, 10, 11, 12, 13, 14, 16, 20]
	# print(magic_index(magic))
	all_sets = power_set([1, 2, 3])
	print()
	for each in all_sets:
		print(each)

main()