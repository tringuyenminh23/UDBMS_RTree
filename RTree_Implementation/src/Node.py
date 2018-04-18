from Entry import Entry
import math 

class Node:

	"""RTree Node
	
	Attributes:
	    filtered (bool): True if this node if filtered
	    link (list): a list contains linked element with this node
	    max_n_children (int): maximum number of child Node
	    parent (Node): parent Node
	    boundary [[int, int], [int, int]]: MBR
	    						  Each tuple contains list of 2 ints [lower_bound, upper_bound] of a dimension
	    children [Node]: list of children nodes
	    entries [Entry]: list of entries (if this node is a leaf node)
	"""
	
	def __init__(self, max_n_children):
		self.max_n_children = max_n_children
		self.parent = None
		self.children = []
		self.boundary = []
		self.entries = []
		self.filtered = False
		self.link = []
	
	def update_boundary(self, coordinates):
		n_dimensions = len(coordinates)

		# if boundary is empty
		if (not self.boundary):
			for i in range(n_dimensions):
				self.boundary.append([coordinates[i], coordinates[i]])
		# Go through each dimension
		for i in range(n_dimensions):
			boundary[i][0] = min(boundary[i][0], coordinates[i])
			boundary[i][1] = max(boundary[i][1], coordinates[i])


	
	def dynamic_add(self, entry : Entry):
		# If this node is a leaf node
		if (len(self.children) == 0):
			# add entry to this node
			self.entries.append(entry)
			# if the boundary is empty or entry is not inside the boundary -> update boundary
			if (not boundary) or (not entry.is_inside(boundary)):
				self.update_boundary(entry.coordinates)
			# if this leaf node contains more than allowed entries -> split
			if (len(self.entries) > max_n_entries):
				self.split


	def print_node(self, level = 0):
		"""Summary
		Simple implementation to print this node and its children
		Args:
		    level (int, optional): current level for printing
		"""
		if (len(self.entries) > 0):
			print('\t' * level, self.boundary, 'is Leaf')
			for i in range(len(self.entries)):
				print('\t' * (level + 1), self.entries[i].coordinates)
		else:
			print('\t' * level, self.boundary)
			for child in self.children:
				child.print_node(level + 1)


	def print_node_not_filtered(self, level = 0):
		"""Summary
		Simple implementation to print this node and its children
		Args:
		    level (int, optional): current level for printing
		"""
		if not self.filtered:
			if (len(self.entries) > 0):
				print('\t' * level, self.boundary, 'is Leaf')
				for i in range(len(self.entries)):
					print('\t' * (level + 1), self.entries[i].coordinates)
			else:
				print('\t' * level, self.boundary)
				for child in self.children:
					child.print_node_not_filtered(level + 1)