#!/usr/local/bin/python3
from nodes import Node

class Stack(object):

	def __init__(self):
		self.top = None

	def push(self, data):
		node = Node(data)
		if self.is_empty():
			self.top = node
		else:
			node.next = self.top
			self.top = node

	def pop(self):
		if self.top == None:
			return None
		temp = self.top
		self.top = temp.next
		return temp

	def peek(self):
		return self.top

	def is_empty(self):
		return self.top == None

	def print_stack(self):
		print('Top', end='')
		current = self.top
		while current:
			print('->' + str(current.data), end='')
			current = current.next
		print()

class Queue(object):

	def __init__(self):
		self.head = None
		self.tail = None

	def enqueue(self, data):
		node = Node(data)
		if self.is_empty():
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	def dequeue(self):
		if self.is_empty():
			print('Queue is empty')
			return None
		if self.head.next == None:
			temp = self.head
			self.head = None
			self.tail = None
			return temp
		temp = self.head
		self.head = self.head.next
		return temp

	def peek(self):
		return self.top

	def is_empty(self):
		return self.head == None

	def print_queue(self):
		print('Head', end='')
		current = self.head
		while current:
			print('->' + str(current.data), end='')
			current = current.next
		print('->Tail', end='\n')

# def main():
# 	pass

# main()
