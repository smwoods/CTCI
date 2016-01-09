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

def main():
	print(triple_step(5))

main()