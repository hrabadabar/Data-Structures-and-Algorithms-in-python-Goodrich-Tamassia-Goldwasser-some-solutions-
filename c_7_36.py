"""Give a complete implementation of the positional list ADT using a doubly
linked list that does not include any sentinel nodes."""

class _DoublyLinkedBase:
	"""A base class providing a doubly linked list representation"""
	
	# This structure is specifically designed for an exersize and
	# it doesn't iclude the use of sentinels. The begining and end 
	# of the list will be presented by the instances of a separate 
	# Node class. 
	
	class _Node:
		"""A lightweight class representing a single node"""
		slots =  '_element', '_next', '_prev'
		
		def __init__(self,element,prev,next):
			self._element = element
			self._next = next
			self._prev = prev
	
	def __init__(self):
		"""Create an empty doublylinked list"""
		self._tail = None
		self._size = 0
		
	def __len__(self):
		"""Returns the length of the list"""
		return self._size
		
	def is_empty(self):
		"""Returns True if list is empty False otherwise"""
		return self._size == 0
		
	def _insert_between(self,e,predecessor,accessor):
		"""Inserts a new node with element e between two nodes
		and return new node"""
		
		new = self._Node(e,predecessor,accessor)
		start = self._tail._next
		end = self._tail
		while start != predecessor:			# find the node which will 
			start = start._next				# be the one before new node
		while end != accessor:				# find the node,which will come
			end = end._prev					# after the new one
		start._next = new					# link nodes
		end._prev = new	
		self._size += 1
		return new
		
	# we define two more functions for the cases when 
	# we want to insert a node at the front of the list
	# or if we want to append a node at the end of the list
	
	def _insert_first(self,e):
		"""Inserts an element at the begining of the list"""
		if self.is_empty():
			new = self._Node(e,None,None)
			new._next = new		 # initialise circularly
			new._prev = new							
			self._tail = new
			
		else:
			new = self._Node(e,self._tail,self._tail._next)
			self._tail._next._prev = new
			self._tail._next = new
		
		
		self._size += 1
		return self._tail._next
		
	def _insert_last(self,e):
		"""Inserts an element at the end of the list"""
		# initialise new node with next - the begining of the list
		# and previous - the old tale
		if self.is_empty():
			return self._insert_first(e)
		else:
		
			prev = self._tail._next
			new = self._Node(e,self._tail,self._tail._next)
			self._tail._next = new
			self._tail = new
			self._size += 1
			return self._tail
			
			
	def _delete_node(self,e):
		"""Removes and returns a node from the list"""
		search = self._tail._next
		if self._size == 1: # nothing to relink after deletion
			old = self._tail
			self._tail._next._prev = None
			self._tail._next = None
			self._tail = None
		else:
			
			while search != e:
				search = search._next
				if search == self._tail and search != e:
					raise ValueError('Not in the list')
			if search == self._tail:
				self._tail = search._prev     # reasign tail to next element
			search._prev._next = search._next # relink nodes
			search._next._prev = search._prev
			old = search					  # make a record of the node
			search = None # convention for deprecated nodes
		self._size -= 1
		return old
		
	def __iter__(self):
		"""Returns an iterator that iterates over the sequence"""
		start = self._tail._next
		if start == None: # None cannot point to next or previous node
			return self
		else:
			while start != self._tail:				
				yield start._element
				start = start._next
			yield self._tail._element
			
			
	def __repr__(self):
		"""A string representation of the structure"""
		return str([x for x in self])
		
		
	
		
		
class PositionalList(_DoublyLinkedBase):
	"""Positional list implementation"""
	
	# Positional list ADT serves as a wrapper
	# of the nodes that make the _DoublyLinkedList.
	# We create an additional Position class as part
	# of our list.
	# Each instance of the Position class points 
	# to a Node instance
	
	class Position:
		"""A lightweight object that represents a single position"""
		
		def __init__(self,container,node):
			self._container = container   # the sequence, which this  
										  # position is part of
			self._node = node
			
		# As it is possible redundant positions to be created
		# we want to be able to check if two instances of our
		# Position class represent the same position in the list
		# We make use of the built in special methods to compare positions
		
		def __eq__(self,other):
			"""Returns True if other position is the same position"""
			return type(other) == type(self) and other._node is self._node
			
		def __ne__(self,other):
			"""Returns True if other position is not same position"""
			return not (self == other)
			
		def element(self):
			"""Returns the element,which occupies that position"""
			return self._node._element
			
	# We define a non-public method called _validate 
	# to help us check whether a certaion position 
	# belongs to the list or if it still exist
	
	def _validate(self,p):
		"""Returns the position's node if position is valid"""
		if p._container is not self:
			raise ValueError('Don\' belong to this list')
		if p._node._next == None:		# convention for deprecated nodes
			raise ValueError('Not in the list anymore')
		if not isinstance(p, self.Position):
			raise TypeError('Must be a position')
		return p._node
	
	# Create a non-public method that wraps each node into
	# an instance of our Position class
	
	def _make_position(self,node):
		"""Return position for a given node (or None)"""
		return self.Position(self,node)
			
	# define accesors
	
	def first(self):
		"""Returns the first position of the list"""
		if self.is_empty():
			raise ValueError('Empty')
		return self._make_position(self._tail._next)
		
	def last(self):
		"""Returns the last element of the list"""
		if self.is_empty():
			raise ValueError('Empty')
		return self._make_position(self._tail)
		
	def after(self,p):
		"""Returns the position after p"""
		node = self._validate(p)
		return self._make_position(node._next)
		
	def before(self,p):
		"""Returns the position before p"""
		node = self._validate(p)
		return self._make_position(node._prev)
		
	# define mutators
	
	# our methods for inserting elements into
	# the list inherit from our _DoublyLinkedBase 
	# class. We create and return a Position instance for
	# each new node
	# We create a non-public _insert_between method, which inherits
	# from our _DoublyLinkedBase and returns a position
	
	def _insert_between(self,e,predecessor,accessor):
		"""Insert an element between two nodes"""
		node = super()._insert_between(e,predecessor,accessor)
		return self._make_position(node)
	
	def insert_first(self,e):
		"""Inserts an element at the front of the list"""
		node = super()._insert_first(e)
		return self._make_position(node)

	def insert_last(self,e):
		"""Appends an element at the end of the list"""
		node = super()._insert_last(e)
		return self._make_position(node)
		
	def add_after(self,e,p):
		"""Add an element after given position"""
		node = self._validate(p)
		if node == self._tail:
			new = self._insert_last(e)
			return self._make_position(new)
		else:
			return self._insert_between(e,node,node._next)
		
	def add_before(self,e,p):
		"""Add an element before given position"""
		node = self._validate(p)
		if node == self._tail._next:
			new = self._insert_first(e)
			return self._make_position(new)
		else:
			return self._insert_between(e,node._prev,node)	
			
	def delete_node(self,p):
		"""Deletes given position and underlying node"""
		old = self._validate(p)
		return self._delete_node(old)
		

