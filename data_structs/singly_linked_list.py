#!/usr/local/bin/python3
from nodes import Node

class SinglyLinkedList(object):

	def __init__(self):
		self.head = None
		self.tail = None

	def append_to_tail(self, data):
		node = Node(data)
		if self.head == None:
			self.head = node
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = node

	def insert_at_head(self, data):
		node = Node(data)
		if self.head == None:
			self.head = node
		else:
			node.next = self.head
			self.head = node

	def delete_node(self, data):
		if self.head == None:
			print('Empty list')
		elif self.head.data == data and self.head.next == None:
			self.head = None
		elif self.head.data == data:
			self.head = self.head.next
		else:
			current = self.head
			while current.next:
				if current.next.data == data:
					if current.next.next:
						current.next = current.next.next
					else:
						current.next = None
				if current.next:
					current = current.next
				else:
					break

	def reverse_list(self):
		rev_head = self.reverse(self.head)
		self.head = rev_head

	def reverse(self, head):
		if not head or not head.next:
			return head
		rev_head = self.reverse(head.next)
		head.next.next = head
		head.next = None
		return rev_head

	def length(self):
		length = 1
		current = self.head
		while current.next:
			current = current.next
			length += 1
		return length

	def join_lists(self, linked_list):
		if self.head == None:
			self.head = linked_list.head
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = linked_list.head

	def print_list(self):
		if self.head == None:
			print('Empty list')
		else:
			current = self.head
			while current.next:
				print(str(current.data) + '->', end='')
				current = current.next
			print(current.data)

# def main():
# 	ll1 = SinglyLinkedList()
# 	for i in range(10):
# 		ll1.append_to_tail(i)
# 	ll2 = SinglyLinkedList()
# 	for i in range(10):
# 		ll2.append_to_tail(i)
# 	ll1.join_lists(ll2)


# main()
