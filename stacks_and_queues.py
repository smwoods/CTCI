#!/usr/local/bin/python3
from data_structs.stacks_and_queues import Stack, Queue


def main():
	stack = Stack()
	for i in range(10):
		stack.push(i)
	stack.print_stack()
main()
