#!/usr/local/bin/python3
import math

# 1.1 Is Unique
def is_unique(string):
	ascii_bit_vec = [0 for _ in range(256)]
	for char in string:
		if ascii_bit_vec[ord(char)] == 0:
			ascii_bit_vec[ord(char)] = 1
		else:
			return False
	return True

# 1.2 Check Permutation
def check_permutation(s1, s2):
	return sorted(s1) == sorted(s2)

# 1.3 URLify
def urlify(string, strlen):
	string = [c for c in string]
	in_str = strlen - 1
	out_str = len(string) - 1
	while in_str >= 0:
		if string[in_str] == ' ':
			string[out_str-2] = '%'
			string[out_str-1] = '2'
			string[out_str] = '0'
			out_str -= 3
			in_str -= 1
		else:
			string[out_str] = string[in_str]
			out_str -= 1
			in_str -= 1
	return ''.join(string)

# 1.4 Palindrome Permutation
def palindrome_permutation(string):
	char_ct = {}
	for char in instring:
		if char in char_ct:
			char_ct[char] += 1
		else:
			char_ct[char] = 1
	flag = 0
	for char in char_ct:
		if char_ct[char] % 2 == 1:
			if flag == 1:
				return False
			else:
				flag = 1
	return True

# 1.5 One Away
def one_away(s1, s2):
	if s1 == s2:
		return True
	if s1[0] == s2[0]:
		if len(s1) == 1 or len(s2) == 1:
			if abs(len(s1) - len(s2)) <= 1:
				return True
			else:
				return False
		return one_away(s1[1:], s2[1:])
	elif len(s1) == len(s2):
		return s1[1:] == s2[1:]
	elif len(s1) > len(s2):
		return s1[1:] == s2
	elif len(s1) < len(s2):
		return s1 == s2[1:]

def string_compression(string):
	ret_string = []
	count = 1
	for i in range(0, len(string)):
		if i == len(string) - 1:
			if count > 1:
				ret_string += (string[i] + str(count))
			else:
				ret_string += string[i]
		elif string[i] == string[i+1]:
			count += 1
		else:
			if count > 1:
				ret_string += (string[i] + str(count))
			else:
				ret_string += string[i]
			count = 1
	if len(ret_string) >= len(string):
		return string
	return ''.join(ret_string)

# 1.7 Rotate Matrix
def rotate_matrix(matrix, N):
	for layer in range(N//2):
		first = layer
		last = (N-1) - layer
		for i in range(first, last):
			offset = i - first
			top = matrix[first][i]
			matrix[first][i] = matrix[last-offset][first]
			matrix[last-offset][first] = matrix[last][last-offset]
			matrix[last][last-offset] = matrix[i][last]
			matrix[i][last] = top
	return matrix

# 1.8 Zero Matrix
def zero_matrix(matrix):
	M = len(matrix)
	N = len(matrix[0])
	rows, cols = [], []
	for i in range(0, M):
		for j in range(0, N):
			if matrix[i][j] == 0:
				rows.append(i)
				cols.append(j)
	print(rows, cols)
	for row in rows:
		for j in range(N):
			matrix[row][j] = 0
	for col in cols:
		for i in range(M):
			matrix[i][col] = 0
	return matrix

# 1.9 String Rotation
def string_rotation(s1, s2):
	return s1 in s2 + s2

# def edit_distance(str_A, str_B):
# 	if len(str_A) == 0:
# 		return len(str_B)
# 	if len(str_B) == 0:
# 		return len(str_A)
# 	M, N = len(str_A), len(str_B)
# 	dist = [[None for _ in range(M)] for _ in range(N)]
# 	for i in range(0, M):
# 		dist[0][i] = i
# 	for j in range(0, N):
# 		dist[j][0] = j

# 	for j in range(1, N):
# 		for i in range(1, M):
# 			add = dist[j][i-1] + 1
# 			delete = dist[j-1][i] + 1
# 			sub_or_none = dist[j-1][i-1]
# 			if str_A[i] != str_B[j]:
# 				sub_or_none += 2
# 			dist[j][i] = min(add, delete, sub_or_none)
# 	return dist[N-1][M-1]


matrix_str = [
	["1", "2", "3", "0"],
	["5", "6", "7", "8"],
	["9", "10", "11", "12"],
	["13", "14", "15", "16"],
	]
matrix_int = [
	[0, 2, 2, 9],
	[5, 6, 7, 7],
	[3, 8, 10, 8],
	[1, 3, 4, 0],
	] 

def main():
	#print(is_unique('a?bjshdlk?r'))
	#print(check_permutation('assface', 'faceass'))
	#print(urlify("Mr John Smith    ", 13))
	#print(PalPerm("dowgaegod"))
	#print(one_away("abale", "abal"))
	#print(string_compression("aabbccaaa"))
	#print(rotate_matrix(matrix, 4))
	#print(zero_matrix(matrix_int))
	print(string_rotation('waterbottle', 'erbottlewat'))



main()