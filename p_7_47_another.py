
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
      
      
h = PositionalList()
new = h.add_first('fsd')
h.add_after(new,'sad')
print(h)


"""Implement a CardHand class that supports a person arranging a group of
cards in his or her hand. The simulator should represent the sequence of
cards using a single positional list ADT so that cards of the same suit are
kept together. Implement this strategy by means of four “fingers” into the
hand, one for each of the suits of hearts, clubs, spades, and diamonds,
so that adding a new card to the person’s hand or playing a correct card
from the hand can be done in constant time. The class should support the
following methods:
• add card(r, s): Add a new card with rank r and suit s to the hand.
• play(s): Remove and return a card of suit s from the player’s hand;
if there is no card of suit s, then remove and return an arbitrary card
from the hand.
iter ( ): Iterate through all cards currently in the hand.
•
• all of suit(s): Iterate through all cards of suit s that are currently in"""

import random
class CardHand:
	"""Class representing a card hand"""
	
	RANKS = [1,2,3,4,5,6,7,8,9,10,'ace','king','queen','jack']
	SUITS = ['hearts','clubs','diamonds','spades']
	
	def __init__(self):
		"""Sequence of cards is represented by a positional list
		Create an empty positional list"""
		"""Create a position for each of the suits"""
		
		self._data = PositionalList()
		self._size = 0
		self._clubs = self._data.add_first('clubs')
		self._hearts = self._data.add_after(self._clubs,'hearts')	
		self._spades = self._data.add_after(self._hearts,'spades')
		self._diamonds = self._data.add_after(self._spades, 'diamonds')
		
	
	def add_card(self,r,s):
		"""Add a card of given suit and given rank to the hand"""
		if r not in CardHand.RANKS or s not in CardHand.SUITS:
			raise ValueError('Card does not exist')
		# add each card of suit s to the correct position
		if s == self._clubs.element():
			self._data.add_after(self._clubs,(r,s))
		elif s == self._hearts.element():
			self._data.add_after(self._hearts,(r,s))
		elif self._spades.element() == s:
			self._data.add_after(self._spades,(r,s))
		else:
			self._data.add_after(self._diamonds,(r,s))
		self._size += 1
		
	def _find_suit(self,s):
		"""Finds the position for given suit"""
		if s == 'clubs':
			pos = self._clubs
		elif s == 'hearts':
			pos = self._hearts
		elif s == 'diamonds':
			pos = self._diamonds
		elif s == 'spades':
			pos = self._spades
		else:
			raise ValueError('Must be a proper suit')
		return pos
			
	def play(self,s):
		"""Play and return a card from suit s
		if there are no cards of suit s, play any card"""
		if not s in CardHand.SUITS:
			raise ValueError('Must be a proper suit')
		if self._data.is_empty():
			raise ValueError('No cards in the hand')
		find = self._data.after(self._find_suit(s))
		if find != None and find.element()[1] == s:
			old = self._data.delete(find)
		else:
			card = random.choice(CardHand.SUITS)
			return self.play(card)
		self._size -= 1
		return str(old[0]) + ' of ' + old[1]
		
	def all_of_suit(self,s):
		"""Iterates through all cards of given suit currently in the hand"""
		find = self._data.after(self._find_suit(s))
		if find is not None:
			while find.element()[1] == s:
				print(find.element())
				find = self._data.after(find)
			
		
			
	def __iter__(self):
		"""Iterates over the sequence"""
		start = self._data.after(self._data.first())
		while start != None:
			if start != self._clubs and start != self._hearts \
			and start != self._spades and start != self._diamonds:
				yield start.element()
			start = self._data.after(start)
		
	def __repr__(self):
		"""String representation of the class"""
		return str([str(x[0]) + ' of ' + x[1] for x in self])		
		



