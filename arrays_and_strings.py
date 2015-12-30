#!/usr/local/bin/python3

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

# def StrCompression(instring):
# 	retstring = []
# 	count = 1
# 	for i in range(0, len(instring)):
# 		if i == len(instring) - 1:
# 			if count > 1:
# 				retstring += (instring[i] + str(count))
# 			else:
# 				retstring += instring[i]
# 		elif instring[i] == instring[i+1]:
# 			count += 1
# 		else:
# 			if count > 1:
# 				retstring += (instring[i] + str(count))
# 			else:
# 				retstring += instring[i]
# 			count = 1
# 	if len(retstring) > len(instring):
# 		return instring
# 	return ''.join(retstring)

# def RotateMatrix(m):
# 	n = len(m)
# 	ret_m = [[None]* n] * n
# 	print(ret_m)
# 	for i in range(0, n):
# 		for j in range(0, n):
# 			print(i, j)
# 			ret_m[j][(n-1)-i] = m[i][j]
# 			print(ret_m)
# 	return ret_m

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


matrix = [
	["1a23", "abb2", "4567", "a2f4"],
	["3425", "bbbb", "eate", "7299"],
	["6666", "eeee", "beef", "0426"],
	["7777", "8888", "6729", "9910"],
	]

def main():
	#print(is_unique('a?bjshdlk?r'))
	#print(check_permutation('assface', 'faceass'))
	#print(urlify("Mr John Smith    ", 13))
	#print(PalPerm("dowgaegod"))
	print(one_away("abale", "abal"))
	#print(StrCompression("aabcccccaaa"))
	# print(RotateMatrix(matrix))



main()