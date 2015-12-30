#!/usr/local/bin/python3
from math import log

def AddWithoutPlus(a, b):
	ret_value = ''
	if a > b:
		max_bits = int(log(abs(a), 2)) + 1
	else:
		max_bits = int(log(abs(b), 2)) + 1
	for i in range(0, max_bits):
		a_bit = getNthBit(a, i)
		b_bit = getNthBit(b, i)
		print(a_bit, b_bit)

def getNthBit(num, n):
	if num & 1<<n == 0:
		return 0
	else:
		return 1

def main():
	print(AddWithoutPlus(32, 7))
main()