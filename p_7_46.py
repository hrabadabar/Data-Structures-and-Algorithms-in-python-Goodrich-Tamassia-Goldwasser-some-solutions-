"""Although we have used a doubly linked list to implement the positional
list ADT, it is possible to support the ADT with an array-based imple-
mentation. The key is to use the composition pattern and store a sequence
of position items, where each item stores an element as well as that ele-
ment’s current index in the array. Whenever an element’s place in the array
is changed, the recorded index in the position must be updated to match.
Given a complete class providing such an array-based implementation of
the positional list ADT. What is the efficiency of the various operations?"""

class PositionalList:
	"""Class representing a positional list ADT implemented with
	an array based implementation"""
	
	class Position:
		"""A lightwight class representing a single object"""
		
		def __init__(self,element,index = 0):
			self._element = element
			self._index = index
			self._size = 0
			
		def element(self):
			"""Returns the element at given position"""
			return self._element
			
	def __init__(self):
		"""Create an empty list"""
		self._sequence = []
		self._size = 0
		
	def _validate(self,p):
		"""Returns position index if position exists"""
		if not isinstance(p, self.Position):
			raise ValueError('Must be a proper position type')
		
		return p._index
		
		
	def is_empty(self):
		"""Returns True if empty else False"""
		return self._size == 0
		
#------------------------accessors------------------------------
		
	def first(self):
		"""Returns the first position of the list"""
		return self._sequence[0]
		
	def last(self):
		"""Returns the last position of the list"""
		return self._sequence[-1]
		
	def after(self,p):
		"""Returns the position after position p"""
		data = self._validate(p)
		return self._sequence[data+1]
	
	def before(self,p):
		"""Returns the position just before position p"""
		data = self._validate(p)
		return self._sequence[data-1]
	
#-----------------------mutators----------------------------------		
		
	def add_first(self,e):
		"""Adds an element at the front of the list"""
		new = self.Position(e,0)
		self._sequence.append(new)
		self._size += 1
		return new
		
	def add_last(self,e):
		new = self._make_position(e,self._size + 1)
		self._sequence.append(new)
		self._size += 1
		return new
		
	def add_after(self,p,e):
		"""Adds an element after given position and returns the new position"""
		
		if self.is_empty():
			raise ValueError('Empty')
		data = self._validate(p)
		new = self.Position(e,data + 1)	# new element is after p
		self._sequence.insert(data+1,new)
		for j in range(new._index+1,len(self._sequence)):
			self._sequence[j]._index += 1		# adjust indexes accordingly
		self._size += 1
		return new
			
	def add_before(self,p,e):
		"""Adds a new element before given position and returns new
		position"""
	
		if self.is_empty():
			raise ValueError('Empty')
		data = self._validate(p)
		new = self.Position(e,data) # new element will have the index of the current element
		self._sequence.insert(data,new)
		for j in range(new._index+1,len(self._sequence)):
			self._sequence[j]._index += 1	# adjust indexes acordingly
		self._size += 1
		return new
		
	def delete(self,p):
		"""Deletes and returns position p"""
		data = self._validate(p)
		for j in range(len(self._sequence)-1,data,-1):	# until p is reached
			self._sequence[j]._index -= 1 # decrement indexes
		return self._sequence.pop(p._index)
		
	def replace(self,p,e):
		"""Replace the element at position p with e
		Return the element formerly at position p"""
		if not isinstance(p, self.Position):
			raise ValueError('Must be a proper position type')
		old = p._element 
		p._element = e
		return old
		
			
	def __repr__(self):
		"""String represetation of the list"""
		return str([(x._element,x._index) for x in self._sequence])
			
			
			

