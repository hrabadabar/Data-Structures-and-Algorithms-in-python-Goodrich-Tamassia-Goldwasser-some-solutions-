class SinglyLinkedListBase:
	"""A base class providing a singly linked list representation"""
	
	class _Node:
		"""A lightweight object representing a single node"""
		
		def __init__(self,element,next):
			self._element = element
			self._next = next
			
	def __init__(self):
		"""Create an empty linked list"""
		self._head = None
		self._trailor = self._Node(None,None)
		self._size = 0
		
	def __len__(self):
		"""Return the length of the list"""
		return self._size
		
	def is_empty(self):
		"""Reuturn True if empty False otherwise"""
		return self._size == 0
		
	def _insert_front(self,e):
		"""Insert element e at position right after j"""
		if self.is_empty():
			new = self._Node(e,self._trailor)
			self._head = new
		else:
			
			new = self._Node(e,self._head)
			self._head = new
		self._size += 1
		return new
			
	def _insert_last(self,e):
		if self.is_empty():
			new = self._Node(e,self._trailor)
			self._head = new
		else:
			start = self._head
			while start._next != self._trailor:
				start = start._next
			new = self._Node(e,self._trailor)
			start._next = new
		self._size += 1
		return new
				
		
	def _delete_node(self,e):
		"""Removes node e and returns element of that node"""
		
		
			
class ForwardList(SinglyLinkedListBase):
	"""A sequential container of elements allowing positional access"""
	
	class Position:
		"""A lightweight object describing a single position"""
		
		def __init__(self,container,node):
			self._node = node
			self._container = container
			
		def element(self):
			"""Return element at that position"""
			return self._node._element
			
		def __eq__(self,other):
			"""Return True if other represents the same position as self"""
			return type(self) is type(other) and other._node is self._node
			
		def __ne__(self,other):
			"""Returns True if other is not the same position"""
			return not(self == other)
			
	def _validate(self,p):
		"""Returns node's positioin or raise error if invalid"""
		if p._container is not self:
			raise ValueError('Not in the list')
		if not isinstance(p, self.Position):
			raise ValueError('Not a position instance')
		
		return p._node
			
	def _make_position(self,node):
		"""Returns node's position or None if sentinel"""
		
		return self.Position(self,node)
		
	def first(self):
		"""Returns the position of the first element"""
		return self._make_position(self._head)
		
	def after(self,p):
		"""Returns the position after position p"""
		node = self._validate(p)
		return self._make_position(node._next)
		
	def last(self):
		"""Returns position of the last element"""
		return self._make_position(self._tail)
	
	def __iter__(self):
		"""Returns an iterator that iterates over the list"""
		start = self.first()
		while start != self._trailor:
			yield start.element()
			start = self.after(start)
		
	def _insert_front(self,e):
		"""Overide method to return position instead of node"""
		node = super()._insert_front(e)
		return self._make_position(node)
		
	def add_first(self,e):
		"""Adds element at the front of the list"""
		return self._insert_front(e)
		
	def add_last(self,e):
		"""Insert an element at position just after position j"""
		self._validate(j)
		return self._insert_last(e)
		
	
