#!/usr/local/bin/python3
from data_structs.graphs import GraphNode, DirectedGraph, BTreeNode, BST
from data_structs.singly_linked_list import SinglyLinkedList
# 4.1 Route Between Nodes (DFS)
def route_between_nodes_depth(start, end):
	if start == end: return True
	for child in start.children:
		if not child.visited:
			child.visited = True
			return route_between_nodes_depth(child, end)
	return False

# 4.1 Route Between Nodes (BFS)
def route_between_nodes_breadth(start, end):
	q = []
	start.visited = True
	q.append(start)
	while len(q) > 0:
		current = q[0]
		q = q[1:]
		if current == end:
			return True
		for child in current.children:
			if not child.visited:
				child.visited = True
				q.append(child)
	return False

# 4.2 Minimal Tree
def minimal_tree(arr, st_index, end_index):
	if end_index < st_index:
		return None
	midpoint = (st_index + end_index) // 2
	root = BTreeNode(arr[midpoint])
	root.left = minimal_tree(arr, st_index, midpoint-1)
	root.right = minimal_tree(arr, midpoint+1, end_index)
	return root

# 4.3 List of Depths
def list_of_depths(root, depth=0, depth_list=[]):
	if len(depth_list) <= depth:
		depth_list += [SinglyLinkedList()]
	depth_list[depth].append_to_tail(root.data)
	if root.left: list_of_depths(root.left, depth+1, depth_list)
	if root.right: list_of_depths(root.right, depth+1, depth_list)
	return depth_list

# 4.4 Check Balanced
def check_balanced(root):
	if root.left:
		left_height = check_balanced(root.left)
	else:
		left_height = 0
	if root.right:
		right_height = check_balanced(root.right)
	else:
		right_height = 0
	if left_height != -1 and right_height != -1:
		if abs(left_height - right_height) > 1:
			return -1
		else:
			return 1 + max(left_height, right_height)
	else:
		return -1

# 4.5 Validate BST
def validate_bst(root, floor=None, ceil=None):
	if floor != None:
		if root.data < floor:
			return False
	if ceil != None:
		if root.data > ceil:
			return False
	if root.left:
		new_ceil = root.data
		left_val = validate_bst(root.left, floor, new_ceil)
	else:
		left_val = True
	if root.right:
		new_floor = root.data
		right_val = validate_bst(root.right, new_floor, ceil)
	else:
		right_val = True
	return (left_val and right_val)

# 4.6 Successor
def successor(node):
	if node.right:
		successor = node.right
		while successor.left:
			successor = successor.left
			return successor
	elif node.parent:
		while node.parent:
			if node.parent.left == node:
				return parent
			else:
				node = node.parent
		return None

	else:
		return None

# 4.7 Build Order
# def build_order(projects, dependencies):

# 4.8 First Common Ancestor
# def first_common_ancestor(root, node1, node2):

# 4.9 BST Sequences
# def bst_sequences(root):
# 	result = []

# 4.10 Check Subtree
NULL_NODE = -9999
def check_subtree(tree, subtree):
	result_tree = []
	result_subtree = []	
	preorder_with_null(tree.root, result_tree)
	preorder_with_null(subtree.root, result_subtree)
	tree_string = ''.join(str(x) for x in result_tree)
	subtree_string = ''.join(str(x) for x in result_subtree)
	return subtree_string in tree_string

def preorder_with_null(root, result):
	if root == None:
		return
	result += [root.data]
	if root.left:
		preorder_with_null(root.left, result)
	else:
		result += [NULL_NODE]
	if root.right:
		preorder_with_null(root.right, result)
	else:
		result += [NULL_NODE]




	


# For testing
def print_tree(root):
	if root.left: print_tree(root.left)
	print(root.data)
	if root.right: print_tree(root.right)


def main():
	# projects = 'a b c d e f'.split()
	# dep = [('d', 'a'), ('b', 'f'), ('d', 'b'), ('a', 'f'), ('c', 'd')]
	# print(build_order(projects, dep))
	tree = BST()
	sub = BST()
	ins1 = [10, 5, 3, 7, 1, 4, 20, 15, 17, 25, 28]
	ins2 = [20, 15, 25, 17, 28]
	for i in ins1:
		tree.insert_node(i)
	for j in ins2:
		sub.insert_node(j)
	print(check_subtree(tree, sub))


	

main()