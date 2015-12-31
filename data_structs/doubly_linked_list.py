#!/usr/local/bin/python3

class Node(object):

	def __init__(self, data):
		self.next = None
		self.prev = None
		self.data = data


class DoublyLinkedList(object):

	def __init__(self):
		self.head = None
		self.tail = None

	def append_to_tail(self, data):
		node = Node(data)
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	def delete_node(self, data):
		if self.head == None:
			print('Empty list')
		elif self.head.data == data and self.head == self.tail:
			self.head = None
			self.tail = None
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
						tail = current
				if current.next:
					current = current.next
				else:
					break


	def print_list(self):
		if self.head == None:
			print('Empty list')
		else:
			current = self.head
			while current.next:
				print(str(current.data) + '->', end='')
				current = current.next
			print(current.data)

def main():
	ll = DoublyLinkedList()
	for i in range(10):
		ll.append_to_tail(i)
	ll.delete_node(8)
	ll.delete_node(0)
	ll.print_list()

main()
