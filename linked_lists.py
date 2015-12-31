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
				return linked_list
		else:
			dup_ct[current.next.data] = 1
			if current.next:
				current = current.next
			else:
				return linked_list
	return linked_list






def main():
	ll = SinglyLinkedList()
	ll.append_to_tail(1)
	ll.append_to_tail(1)
	ll.append_to_tail(1)
	ll.append_to_tail(1)
	ll.append_to_tail(1)
	ll.append_to_tail(2)
	ll.append_to_tail(1)
	ll = remove_dups(ll)
	ll.print_list()

main()