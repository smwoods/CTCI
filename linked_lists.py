#!/usr/local/bin/python3
from data_structs.singly_linked_list import SinglyLinkedList
import random

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

# 2.4 Partition
def partition(linked_list, x):
	partitioned = SinglyLinkedList()
	current = linked_list.head
	while current != None:
		if current.data >= x:
			partitioned.append_to_tail(current.data)
		else:
			partitioned.insert_at_head(current.data)
		current = current.next
	return partitioned

# 2.5 Sum Lists
def sum_lists(head1, head2, sum_list):
	while head1 or head2:
		if not head1:
			sum_list.append_to_tail(head2.data)
			return sum_lists(None, head2.next, sum_list)
		elif not head2:
			sum_list.append_to_tail(head1.data, sum_list)
			return sum_lists(head1.next, None)
		else:
			total = head1.data + head2.data
			if total >= 10:
				if head1.next:
					head1.next.data += 1
					sum_list.append_to_tail(total % 10)
					return sum_lists(head1.next, head2.next, sum_list)
				elif head2.next:
					head2.next.data += 1
					sum_list.append_to_tail(total % 10)
					return sum_lists(head1.next, head2.next, sum_list)
				else:
					sum_list.append_to_tail(total % 10)
					sum_list.append_to_tail(1)
					return sum_lists(head1.next, head2.next, sum_list)
			else:
				sum_list.append_to_tail(total)
				return sum_lists(head1.next, head2.next, sum_list)
	return sum_list

# 2.5 Sum Lists (reverse)
def reverse_sum_lists(ll1, ll2):
	head1 = ll1.head
	head2 = ll2.head
	if head1 == None and head2 == None:
		return sum_list
	length1 = ll1.length()
	length2 = ll2.length()
	diff = length1 - length2
	while diff != 0:
		if diff > 0:
			ll2.insert_at_head(0)
			diff -= 1
		elif diff < 0:
			ll1.insert_at_head(0)
			diff += 1
	ll1.reverse_list()
	ll2.reverse_list()
	sum_list = SinglyLinkedList()
	sum_list = sum_lists(ll1.head, ll2.head, sum_list)
	sum_list.reverse_list()
	return sum_list

# 2.6 Palindrome
def palindrome(linked_list):
	stack = []
	length = linked_list.length()
	midpoint = length // 2
	current = linked_list.head
	while midpoint != 0:
		stack.append(current.data)
		current = current.next
		midpoint -= 1
	if length % 2 == 1:
		current = current.next
	while current:
		if current.data == stack.pop():
			current = current.next
		else:
			return False
	return True


def main():
	ll1 = SinglyLinkedList()
	for i in range(1, 8):
		ll1.append_to_tail(i)
	for i in range(5, 0, -1):
		ll1.append_to_tail(i)
	ll1.print_list()
	print(palindrome(ll1))


main()