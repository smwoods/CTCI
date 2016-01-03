#!/usr/local/bin/python3
from data_structs.graphs import GraphNode, DirectedGraph

def route_between_nodes_depth(start, end):
	if start == end: return True
	for child in start.children:
		if not child.visited:
			child.visited = True
			return route_between_nodes_depth(child, end)
	return False

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


def main():
	nodes = [GraphNode(i) for i in range(6)]
	nodes[0].add_child(nodes[1])
	nodes[0].add_child(nodes[2])
	nodes[1].add_child(nodes[3])
	nodes[1].add_child(nodes[4])
	nodes[2].add_child(nodes[3])
	nodes[2].add_child(nodes[4])
	nodes[3].add_child(nodes[4])
	nodes[4].add_child(nodes[5])
	dir_graph = DirectedGraph()
	for node in nodes:
		dir_graph.insert_node(node)
	print(route_between_nodes_breadth(nodes[5], nodes[0]))
	

main()