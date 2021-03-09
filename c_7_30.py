class LeakyStack:
	"""Implements a stack with limited capacity using a singly list for storage.
	Appending an element to a full stack results in the oldest element being leaked 
	out of the stack"""
	
	class _Node:
		"""A lightweight object representing a single node"""
		
		def __init__(self,element,next):
			self._element = element
			self._next = next
			
	def __init__(self,maxlen = None):
		"""Initiate the stack with maxlen as optional parameter"""
		self._trailor = self._Node(None,None)
		self._head = None
		self._size = 0
		self._maxlen = int(maxlen)
	
	def __len__(self):
		return self._size
		
	def is_empty(self):
		"""Returns True if empty else False"""
		return self._size == 0
		
	def top(self):
		"""Returns the element at the top of the stack"""
		if self.is_empty():
			raise ValueError('Empty')
		return self._head
		
	def push(self,e):
		"""Append element e at the top of the stack"""
		if self.is_empty():
			new = self._Node(e,self._trailor)
			self._head = new
			self._size += 1
		else:
			new = self._Node(e,self._head)
			self._head = new
			if self._size == self._maxlen:
				start = self._head
				# until we reach the last node - the one before the trailer
				while start._next._next != self._trailor: 
					start = start._next
				# delete last node
				start._next = self._trailor
				
				
			else:
				self._size += 1
				
	def pop(self):
		"""Removes and returns the last element in the stack"""
		if self.is_empty():
			raise ValueError('Empty')
		old = self._head._element
		self._head = self._head._next
		self._size -= 1
		return old._element
		
			
	def __iter__(self):
		start = self._head
		while start != self._trailor:
			yield start._element
			start = start._next
			
	def __repr__(self):
		"""String represetation of the queue"""
		return str([x for x in self])
			
			

			
