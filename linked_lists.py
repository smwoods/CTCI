#!/usr/local/bin/python3
from data_structs.singly_linked_list import SinglyLinkedList

# 2.1 Remove Dups
def remove_dups(linked_list):
	head = linked_list.head
	dup_ct = {}
	dup_ct[head.data] = 1
	current = head
	while current.next != None:
		if current.next.data in dup_ct:
			if current.next.next:
				current.next = current.next.next
				continue
			else:
				current.next = None
				linked_list.tail = current
				return linked_list
		else:
			dup_ct[current.next.data] = 1
			if current.next:
				current = current.next
			else:
				return linked_list
	return linked_list

# 2.2 Return Kth to Last
def kth_to_last(linked_list, k):
	trailing = linked_list.head
	leading = trailing
	for i in range(k-1):
		if not leading.next:
			print('Invalid request')
			return
		leading = leading.next
	while leading.next:
		leading = leading.next
		trailing = trailing.next
	return trailing

# 2.3 Delete Middle Node
def delete_middle_node(node):
	node.data = node.next.data
	if node.next.next:
		node.next = node.next.next
	else:
		node.next = None





def main():
	ll = SinglyLinkedList()
	for i in range(10):
		ll.append_to_tail(i)
	ll.print_list()
	middle = ll.head.next.next.next
	delete_middle_node(middle)
	ll.print_list()


main()