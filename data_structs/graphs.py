#!/usr/local/bin/python3

class GraphNode(object):

	def __init__(self, data):
		self.data = data
		self.children = []
		self.visited = False

	def add_child(self, node):
		self.children += [node]

class DirectedGraph(object):

	def __init__(self):
		self.nodes = []

	def insert_node(self, node):
		self.nodes += [node]

	def print_graph(self):
		for node in self.nodes:
			print('Node: ', node.data)
			print('Children: ', end='')
			for child in node.children:
				print(child.data, end=' ')
			print()

class BTreeNode(object):

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

