"""Write a Scoreboard class that maintains the top 10 scores for a game ap-
plication using a singly linked list, rather than the array that was used in
Section 5.5.1."""

#-------------------------------my class -----------------------------

class Scoreboard:
	"""Maintains the top 10 scores of a game using a positional list
	as underlying storage"""
	
	def __init__(self):
		"""Create empty positional list"""
		self._data = SinglyLinkedListBase()

	
		
	def first(self):
		"""Return the score at first position"""
		return self._data.first().element()
		
	def last(self):
		"""Returns the score at the last position"""
		return self._data.last().element()
	
	def new_score(self,score):
		"""Insert the new score if qualifies among the top 10 scores"""
		if self._data.is_empty():
			self._data.add_first(score)
		elif score <= self.last() and len(self._data) < 10:
			self._data.add_last(score)		# append new score if maximum length is not reached	
		else:
			if score > self.first():
				self._data.add_first(score)
			else:
				start = self._data.first()
				
				# the score after which we insert the new score
				# has to be bigger or at least equal to the new score
				# the next must be smaller
				while self._data.after(start).element() >= score: 
					start = self._data.after(start)
				self._data.add_after(start,score)
			if len(self._data) > 10:
				self._data.delete_last() 
				
#----------------------------source code ---------------------------------------------

# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class _DoublyLinkedBase:
  """A base class providing a doubly linked list representation."""

  #-------------------------- nested _Node class --------------------------
  # nested _Node class
  class _Node:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    __slots__ = '_element', '_prev', '_next'            # streamline memory

    def __init__(self, element, prev, next):            # initialize node's fields
      self._element = element                           # user's element
      self._prev = prev                                 # previous node reference
      self._next = next                                 # next node reference

  #-------------------------- list constructor --------------------------

  def __init__(self):
    """Create an empty list."""
    self._header = self._Node(None, None, None)
    self._trailer = self._Node(None, None, None)
    self._header._next = self._trailer                  # trailer is after header
    self._trailer._prev = self._header                  # header is before trailer
    self._size = 0                                      # number of elements

  #-------------------------- public accessors --------------------------

  def __len__(self):
    """Return the number of elements in the list."""
    return self._size

  def is_empty(self):
    """Return True if list is empty."""
    return self._size == 0

  #-------------------------- nonpublic utilities --------------------------

  def _insert_between(self, e, predecessor, successor):
    """Add element e between two existing nodes and return new node."""
    newest = self._Node(e, predecessor, successor)      # linked to neighbors
    predecessor._next = newest
    successor._prev = newest
    self._size += 1
    return newest

  def _delete_node(self, node):
    """Delete nonsentinel node from the list and return its element."""
    predecessor = node._prev
    successor = node._next
    predecessor._next = successor
    successor._prev = predecessor
    self._size -= 1
    element = node._element                             # record deleted element
    node._prev = node._next = node._element = None      # deprecate node
    return element                                      # return deleted element
    



# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.



class PositionalList(_DoublyLinkedBase):
  """A sequential container of elements allowing positional access."""

  #-------------------------- nested Position class --------------------------
  class Position:
    """An abstraction representing the location of a single element.

    Note that two position instaces may represent the same inherent
    location in the list.  Therefore, users should always rely on
    syntax 'p == q' rather than 'p is q' when testing equivalence of
    positions.
    """

    def __init__(self, container, node):
      """Constructor should not be invoked by user."""
      self._container = container
      self._node = node
    
    def element(self):
      """Return the element stored at this Position."""
      return self._node._element
      
    def __eq__(self, other):
      """Return True if other is a Position representing the same location."""
      return type(other) is type(self) and other._node is self._node

    def __ne__(self, other):
      """Return True if other does not represent the same location."""
      return not (self == other)               # opposite of __eq__
    
  #------------------------------- utility methods -------------------------------
  def _validate(self, p):
    """Return position's node, or raise appropriate error if invalid."""
    if not isinstance(p, self.Position):
      raise TypeError('p must be proper Position type')
    if p._container is not self:
      raise ValueError('p does not belong to this container')
    if p._node._next is None:                  # convention for deprecated nodes
      raise ValueError('p is no longer valid')
    return p._node

  def _make_position(self, node):
    """Return Position instance for given node (or None if sentinel)."""
    if node is self._header or node is self._trailer:
      return None                              # boundary violation
    else:
      return self.Position(self, node)         # legitimate position
    
  #------------------------------- accessors -------------------------------
  def first(self):
    """Return the first Position in the list (or None if list is empty)."""
    return self._make_position(self._header._next)

  def last(self):
    """Return the last Position in the list (or None if list is empty)."""
    return self._make_position(self._trailer._prev)

  def before(self, p):
    """Return the Position just before Position p (or None if p is first)."""
    node = self._validate(p)
    return self._make_position(node._prev)

  def after(self, p):
    """Return the Position just after Position p (or None if p is last)."""
    node = self._validate(p)
    return self._make_position(node._next)

  def __iter__(self):
    """Generate a forward iteration of the elements of the list."""
    cursor = self.first()
    while cursor is not None:
      yield cursor.element()
      cursor = self.after(cursor)
      


  #------------------------------- mutators -------------------------------
  # override inherited version to return Position, rather than Node
  def _insert_between(self, e, predecessor, successor):
    """Add element between existing nodes and return new Position."""
    node = super()._insert_between(e, predecessor, successor)
    return self._make_position(node)

  def add_first(self, e):
    """Insert element e at the front of the list and return new Position."""
    return self._insert_between(e, self._header, self._header._next)

  def add_last(self, e):
    """Insert element e at the back of the list and return new Position."""
    return self._insert_between(e, self._trailer._prev, self._trailer)

  def add_before(self, p, e):
    """Insert element e into list before Position p and return new Position."""
    original = self._validate(p)
    return self._insert_between(e, original._prev, original)

  def add_after(self, p, e):
    """Insert element e into list after Position p and return new Position."""
    original = self._validate(p)
    return self._insert_between(e, original, original._next)

  def delete(self, p):
    """Remove and return the element at Position p."""
    original = self._validate(p)
    return self._delete_node(original)  # inherited method returns element

  def replace(self, p, e):
    """Replace the element at Position p with e.

    Return the element formerly at Position p.
    """
    original = self._validate(p)
    old_value = original._element       # temporarily store old element
    original._element = e               # replace with new element
    return old_value                    # return the old element value
    

  def max(self):
      """Returns the max element from an instance containing 
      comparable elements"""
      first = self.first()
      max_el = first.element()
      while first != self.last():              
          first = self.after(first)             
          if first.element() > max_el:
              max_el = first.element()
      return max_el
      
      
  def _find(self,e,start):
      """Returns the position of the first occurance of element 'e' in 
      the list"""
      if start == self._trailer:
          return None
      if start._element == e:
          return start
      return self._find(e,start._next)
      
  def find(self,e):
      """Public method for finding the position of the first 
      occurence of 'e' in the list"""
      return self._find(e,self._header._next)
      
  def __repr__(self):
      return str([x for x in self])
      
 

"""Write a Scoreboard class that maintains the top 10 scores for a game ap-
plication using a singly linked list, rather than the array that was used in
Section 5.5.1."""

class SinglyLinkedListBase:
	""" Base Class representing SinglyLinkedList"""
	
	class _Node:
		"""A lightweight object representing a single node"""
		slots = '_element', '_next'
		
		def __init__(self,element,next):
			self._element = element
			self._next = next
			
		def element(self):
			"""Returns given node's element"""
			return self._element
	
	def __init__(self):
		"""Create an empty list"""
		self._header = self._Node(None,None)
		self._tail = None
		self._size = 0
		
	def __len__(self):
		"""Returns the length of the list"""
		return self._size
		
	def is_empty(self):
		"""Returns True if list is empty False otherwise"""
		return self._size == 0
		
	def add_last(self,e):
		"""Adds an element at the back of the list"""
		new = self._Node(e,None)
		if self.is_empty():
			self._tail = new
			self._header._next = self._tail
		else:
			self._tail._next = new
			self._tail = new
		self._size += 1
		
	def add_first(self,e):
		"""Adds an element at the front of the list"""
		if self.is_empty():
			new = self._Node(e,None)
			self._header._next = new
			self._tail = new
		else:
			new = self._Node(e,self._header._next)
			self._header._next = new
		self._size += 1
		
	def add_after(self,n,e):
		"""Adds a new node after given node"""
		new = self._Node(e,n._next)
		n._next = new
		self._size += 1
		
	def delete_last(self):
		"""Delete and returns last node"""
		if self.is_empty():
			raise ValueError('Empty')
		start = self._header
		while start._next != self._tail:
			start = start._next
		start._next = None
		self._tail = None
		self._tail = start
		self._size -= 1
		
		
	def first(self):
		"""Returns the element at the front of the list"""
		return self._header._next
		
	def last(self):
		"""Returns the element at the back of the list"""
		return self._tail
	
	def after(self,n):
		"""Returns the node after n"""
		return n._next
		
	def __iter__(self):
		"""Iterates over the elements of the list"""
		start = self._header._next
		while start is not None:
			yield start._element
			start=  start._next
			
"""Write a Scoreboard class that maintains the top 10 scores for a game ap-
plication using a singly linked list, rather than the array that was used in
Section 5.5.1."""

class Scoreboard:
	"""Maintains the top 10 scores of a game using a positional list
	as underlying storage"""
	
	def __init__(self):
		"""Create empty positional list"""
		self._data = SinglyLinkedListBase()

	
		
	def first(self):
		"""Return the score at first position"""
		return self._data.first().element()
		
	def last(self):
		"""Returns the score at the last position"""
		return self._data.last().element()
	
	def new_score(self,score):
		"""Insert the new score if qualifies among the top 10 scores"""
		if self._data.is_empty():
			self._data.add_first(score)
		elif score <= self.last() and len(self._data) < 10:
			self._data.add_last(score)		# append new score if maximum length is not reached	
		else:
			if score > self.first():
				self._data.add_first(score)
			else:
				start = self._data.first()
				
				# the score after which we insert the new score
				# has to be bigger or at least equal to the new score
				# the next must be smaller
				while self._data.after(start).element() >= score: 
					start = self._data.after(start)
				self._data.add_after(start,score)
			if len(self._data) > 10:
				self._data.delete_last() 
				
				
				
	def __repr__(self):
		"""String representation of the list"""
		return str([x for x in self._data])
		
		

