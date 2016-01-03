#!/usr/local/bin/python3
from data_structs.graphs import GraphNode, DirectedGraph, BTreeNode
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
	print('st, end', st_index, end_index)
	if end_index < st_index:
		return None
	midpoint = (st_index + end_index) // 2
	root = BTreeNode(arr[midpoint])
	root.left = minimal_tree(arr, st_index, midpoint-1)
	root.right = minimal_tree(arr, midpoint+1, end_index)
	return root

# 4.2 List of Depths
def list_of_depths(root, depth=0, depth_list=[]):
	if len(depth_list) <= depth:
		depth_list += [SinglyLinkedList()]
	depth_list[depth].append_to_tail(root.data)
	if root.left: list_of_depths(root.left, depth+1, depth_list)
	if root.right: list_of_depths(root.right, depth+1, depth_list)
	return depth_list




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
	arr = [i for i in range(16)]
	min_tree_root = minimal_tree(arr, 0, len(arr)-1)
	depth_list = list_of_depths(min_tree_root)
	for x in depth_list:
		x.print_list()

	

main()