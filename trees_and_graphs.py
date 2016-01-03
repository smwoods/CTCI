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


# For testing
def print_tree(root):
	if root.left: print_tree(root.left)
	print(root.data)
	if root.right: print_tree(root.right)


def main():
	# nodes = [GraphNode(i) for i in range(6)]
	# nodes[0].add_child(nodes[1])
	# nodes[0].add_child(nodes[2])
	# nodes[1].add_child(nodes[3])
	# nodes[1].add_child(nodes[4])
	# nodes[2].add_child(nodes[3])
	# nodes[2].add_child(nodes[4])
	# nodes[3].add_child(nodes[4])
	# nodes[4].add_child(nodes[5])
	# dir_graph = DirectedGraph()
	# for node in nodes:
	# 	dir_graph.insert_node(node)
	# print(route_between_nodes_breadth(nodes[5], nodes[0]))
	arr = [i for i in range(63)]
	min_tree_root = minimal_tree(arr, 0, len(arr)-1)
	bst = BST()
	bst.insert_node(5)
	bst.insert_node(3)
	bst.insert_node(1)
	bst.insert_node(4)
	bst.insert_node(6)
	bst.insert_node(7)
	print(check_balanced(bst.root))

	

main()