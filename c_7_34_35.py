
 """Modify the PositionalList class to support a method swap(p, q) that causes
the underlying nodes referenced by positions p and q to be exchanged for
each other. Relink the existing nodes; do not create any new nodes."""

#----------------------------- method-------------------------------

def swap(self,p,q):
    """Swaps underlying nodes at positions p and q"""
    node1 = self._validate(p)
    node2 = self._validate(q)
    # Swap two neigbour nodes. node1 and node2 become node2 and node1, node1._prev
    # becomes node2,node2._next becomes node1,node2._prev = node1._prev
    #(we keep a record of node1_prev), node1._prev._next become node2  
    if node1._next == node2:                    
      temp = node1._prev
      node1._next = node2._next
      node2._next._prev = node1
      node1._prev = node2
      node2._next = node1

      node2._prev = temp
      temp._next = node2
    # Swap two distant nodes. Exchange all six pointers.First make a 
    # record of one node's pointers
    else:
      temp1 = node1._next
      temp2 = node1._prev
      node1._next = node2._next
      node2._next._prev = node1
      node1._prev = node2._prev
      node2._prev._next = node1
      node2._next = temp1
      temp1._prev = node2
      node2._prev = temp2
      temp2._next = node2

#-----------------------------source code -------------------------
  
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
    
  # C-7.33 Modify the DoublyLinkedBase class to include a reverse method that re-
  # verses the order of the list, yet without creating or destroying any nodes.
  def _reverse(self):
    """Reverses the order of the list"""
    # Start swapping the elements at both ends of the list
    # Stop when the middle is reached if length of the list is odd
    # or when cursors go past each other if length of the list is even
    cursor = self._trailer._prev
    forward = self._header._next
    while cursor != forward or cursor._next != forward._next:
      forward._element,cursor._element = cursor._element,forward._element
      forward = forward._next
      cursor = cursor._prev
          




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
    
  """C-7.35 To implement the iter method of the PositionalList class, we relied on the
  convenience of Python’s generator syntax and the yield statement. Give
  an alternative implementation of iter by designing a nested iterator class.
  (See Section 2.3.4 for discussion of iterators.)"""

  class _Iterator:
    """Returns an iterator that iterates over the list"""
    
    def __init__(self,sequence):
      self._sequence = sequence
      self._start =  sequence._header
        
    def __next__(self):
      self._start = self._start._next
      if self._start != self._sequence._trailer:
        return self._start._element
      else:
        raise StopIteration()
    
    def __iter__(self):
      return self
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
    return self._Iterator(self) 
      


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

  """Modify the PositionalList class to support a method swap(p, q) that causes
the underlying nodes referenced by positions p and q to be exchanged for
each other. Relink the existing nodes; do not create any new nodes."""
      
  def swap(self,p,q):
    """Swaps underlying nodes at positions p and q"""
    node1 = self._validate(p)
    node2 = self._validate(q)
    # Swap two neigbour nodes. node1 and node2 become node2 and node1, node1._prev
    # becomes node2,node2._next becomes node1,node2._prev = node1._prev
    #(we keep a record of node1_prev), node1._prev._next become node2  
    if node1._next == node2:                    
      temp = node1._prev
      node1._next = node2._next
      node2._next._prev = node1
      node1._prev = node2
      node2._next = node1

      node2._prev = temp
      temp._next = node2
    # Swap two distant nodes. Exchange all six pointers.First make a 
    # record of one node's pointers
    else:
      temp1 = node1._next
      temp2 = node1._prev
      node1._next = node2._next
      node2._next._prev = node1
      node1._prev = node2._prev
      node2._prev._next = node1
      node2._next = temp1
      temp1._prev = node2
      node2._prev = temp2
      temp2._next = node2
   
    

    
  def __repr__(self):
      return str([x for x in self])
      
