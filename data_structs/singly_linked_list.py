#!/usr/local/bin/python3

#!/usr/local/bin/python3

class Node(object):

	def __init__(self, data):
		self.next = None
		self.data = data


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
# 	ll = SinglyLinkedList()
# 	for i in range(10):
# 		ll.append_to_tail(i)
# 	ll.delete_node(8)
# 	ll.delete_node(0)
# 	ll.print_list()
# 	ll.reverse_list()
# 	ll.print_list()
# 	ll.delete_node(9)
# 	ll.print_list()
# 	print(ll.length())

# main()
