class SinglyListStack:
	"""Stack implementation using a singly list with
	a header sentinel as a storage"""
	
	class _Node:
		"""Lightweight object for storing a single node"""
		def __init__(self,element,next):
			self._element = element
			self._next = next
		
	def __init__(self):
		"""Initiate the structure"""
		self._header = self._Node(None,None)
		self._size = 0
		
	def __len__(self):
		return self._size
		
	def is_empty(self):
		"""Returns True if empty else False"""
		return self._size == 0
		
	def top(self):
		"""Returns the element currently at the top of the stack"""
		if self.is_empty():
			raise ValueError('No elements')
		return self._header._next._element
		
	def push(self,e):
		"""Insert element e at the top of the stack"""
		old = self._header._next
		new = self._Node(e,old)
		self._header._next = new
		self._size += 1
		
	def pop(self):
		"""Removes the element currently at the top of the stack"""
		old = self._header._next
		self._header._next = old._next
		old._next = None
		self._size -= 1
		return old._element
		
	def count_el(self):
		"""Counts the number of elements in the stack"""
		start = self._header._next
		count = 0
		while start != None:
			start = start._next
			count += 1
		return count
		
	def __iter__(self):
		n = self._header._next
		while n != None:
			yield n._element
			n = n._next
	
	def __repr__(self):
		"""String representation of the structure"""
		return str([x for x in self])
		

