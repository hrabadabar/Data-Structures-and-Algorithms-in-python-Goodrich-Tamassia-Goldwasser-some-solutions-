 """R-8.26 The collections.deque class supports an extend method that adds a col-
  lection of elements to the end of the queue at once. Reimplement the
  breadthfirst method of the Tree class to take advantage of this feature."""
  
  
  def breadthfirst(self):
     """Generate a breadth-first iteration of the positions of the tree."""
     if not self.is_empty():
      fringe = collections.deque()             # known positions not yet yielded
      fringe.enqueue(self.root())        # starting with the root
      while not fringe.is_empty():
          p = fringe.dequeue()
          yield p
          fringe.extend([j for j in self.children(p)])  

#----------------------source code-------------------------------------          
 
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

import collections

class LinkedQueue:
  """FIFO queue implementation using a singly linked list for storage."""

  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'         # streamline memory usage

    def __init__(self, element, next):
      self._element = element
      self._next = next

  #------------------------------- queue methods -------------------------------
  def __init__(self):
    """Create an empty queue."""
    self._head = None
    self._tail = None
    self._size = 0                          # number of queue elements

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise ValueError('Queue is empty')
    return self._head._element              # front aligned with head of list

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise ValueError('Queue is empty')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():                     # special case as queue is empty
      self._tail = None                     # removed head had been the tail
    return answer

  def enqueue(self, e):
    """Add an element to the back of queue."""
    newest = self._Node(e, None)            # node will be new tail node
    if self.is_empty():
      self._head = newest                   # special case: previously empty
    else:
      self._tail._next = newest
    self._tail = newest                     # update reference to tail node
    self._size += 1



import collections

class Tree:
  """Abstract base class representing a tree structure."""

  #------------------------------- nested Position class -------------------------------
  class Position:
    """An abstraction representing the location of a single element within a tree.

    Note that two position instaces may represent the same inherent location in a tree.
    Therefore, users should always rely on syntax 'p == q' rather than 'p is q' when testing
    equivalence of positions.
    """

    def element(self):
      """Return the element stored at this Position."""
      raise NotImplementedError('must be implemented by subclass')
      
    def __eq__(self, other):
      """Return True if other Position represents the same location."""
      raise NotImplementedError('must be implemented by subclass')

    def __ne__(self, other):
      """Return True if other does not represent the same location."""
      return not (self == other)            # opposite of __eq__

  # ---------- abstract methods that concrete subclass must support ----------
  def root(self):
    """Return Position representing the tree's root (or None if empty)."""
    raise NotImplementedError('must be implemented by subclass')

  def parent(self, p):
    """Return Position representing p's parent (or None if p is root)."""
    raise NotImplementedError('must be implemented by subclass')

  def num_children(self, p):
    """Return the number of children that Position p has."""
    raise NotImplementedError('must be implemented by subclass')

  def children(self, p):
    """Generate an iteration of Positions representing p's children."""
    raise NotImplementedError('must be implemented by subclass')

  def __len__(self):
    """Return the total number of elements in the tree."""
    raise NotImplementedError('must be implemented by subclass')

  # ---------- concrete methods implemented in this class ----------
  def is_root(self, p):
    """Return True if Position p represents the root of the tree."""
    return self.root() == p

  def is_leaf(self, p):
    """Return True if Position p does not have any children."""
    return self.num_children(p) == 0

  def is_empty(self):
    """Return True if the tree is empty."""
    return len(self) == 0

  def depth(self, p):
    """Return the number of levels separating Position p from the root."""
    if self.is_root(p):
      return 0
    else:
      return 1 + self.depth(self.parent(p))

  def _height1(self):                 # works, but O(n^2) worst-case time
    """Return the height of the tree."""
    return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

  def _height2(self, p):                  # time is linear in size of subtree
    """Return the height of the subtree rooted at Position p."""
    if self.is_leaf(p):
      return 0
    else:
      return 1 + max(self._height2(c) for c in self.children(p))

  def height(self, p=None):
    """Return the height of the subtree rooted at Position p.

    If p is None, return the height of the entire tree.
    """
    if p is None:
      p = self.root()
    return self._height2(p)        # start _height2 recursion

  def __iter__(self):
    """Generate an iteration of the tree's elements."""
    for p in self.positions():                        # use same order as positions()
      yield p.element()                               # but yield each element

  def positions(self):
    """Generate an iteration of the tree's positions."""
    return self.preorder()                            # return entire preorder iteration

  def preorder(self):
    """Generate a preorder iteration of positions in the tree."""
    if not self.is_empty():
      for p in self._subtree_preorder(self.root()):  # start recursion
        yield p

  def _subtree_preorder(self, p):
    """Generate a preorder iteration of positions in subtree rooted at p."""
    yield p                                           # visit p before its subtrees
    for c in self.children(p):                        # for each child c
      for other in self._subtree_preorder(c):         # do preorder of c's subtree
        yield other                                   # yielding each to our caller

  def postorder(self):
    """Generate a postorder iteration of positions in the tree."""
    if not self.is_empty():
      for p in self._subtree_postorder(self.root()):  # start recursion
        yield p

  def _subtree_postorder(self, p):
    """Generate a postorder iteration of positions in subtree rooted at p."""
    for c in self.children(p):                        # for each child c
      for other in self._subtree_postorder(c):        # do postorder of c's subtree
        yield other                                   # yielding each to our caller
    yield p                                           # visit p after its subtrees
    
  """R-8.26 The collections.deque class supports an extend method that adds a col-
  lection of elements to the end of the queue at once. Reimplement the
  breadthfirst method of the Tree class to take advantage of this feature."""
  
  
  def breadthfirst(self):
     """Generate a breadth-first iteration of the positions of the tree."""
     if not self.is_empty():
      fringe = collections.deque()             # known positions not yet yielded
      fringe.enqueue(self.root())        # starting with the root
      while not fringe.is_empty():
          p = fringe.dequeue()
          yield p
          fringe.extend([j for j in self.children(p)])  

  """def breadthfirst(self):
    Generate a breadth-first iteration of the positions of the tree.
    if not self.is_empty():
      fringe = LinkedQueue()             # known positions not yet yielded
      fringe.enqueue(self.root())        # starting with the root
      while not fringe.is_empty():
        p = fringe.dequeue()             # remove from front of the queue
        yield p                          # report this position
        for c in self.children(p):
          fringe.enqueue(c)             # add children to back of queue"""

