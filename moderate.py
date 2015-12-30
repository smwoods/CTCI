#!/usr/local/bin/python3

def NumSwapper(a, b):
	if a > b:
		a = a - b
		b = b + a
		a = b - a
		return (a, b)
	elif a < b:
		b = b - a
		a = a + b
		b = a - b
		return (a, b)
	else:
		return (a, b)

def Intersection(seg1, seg2):


def main():
	#print(NumSwapper(3, 19))
	#print(NumSwapper(4, 20))
	print(Intersection([(1, 4), (2, 3)], [(3, 5), (6, 6)]))

main()