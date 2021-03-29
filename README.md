# Data-Structures-and-Algorithms-in-python-Goodrich-Tamassia-Goldwasser-some-solutions-
# The solutions are to the below exercises. Many of these don't require coded solutions,
# I gave it an attempt anyway. I suspect many of my solutions can take some improvement

C-7.24 Give a complete implementation of the stack ADT using a singly linked
list that includes a header sentinel.

C-7.26 Implement a method, concatenate(Q2) for the LinkedQueue class that
takes all elements of LinkedQueue Q2 and appends them to the end of the
original queue. The operation should run in O(1) time and should result
in Q2 being an empty queue.

C-7.28 Describe a fast recursive algorithm for reversing a singly linked list.

C-7.30 Exercise P-6.35 describes a LeakyStack abstraction. Implement that ADT
using a singly linked list for storage.

C-7.31 Design a forward list ADT that abstracts the operations on a singly linked
list, much as the positional list ADT abstracts the use of a doubly linked
list. Implement a ForwardList class that supports such an ADT.

C-7.34 Modify the PositionalList class to support a method swap(p, q) that causes
the underlying nodes referenced by positions p and q to be exchanged for
each other. Relink the existing nodes; do not create any new nodes.

C-7.35 To implement the iter method of the PositionalList class, we relied on the
convenience of Python’s generator syntax and the yield statement. Give
an alternative implementation of iter by designing a nested iterator class.
(See Section 2.3.4 for discussion of iterators.)

C-7.36 Give a complete implementation of the positional list ADT using a doubly
linked list that does not include any sentinel nodes.

C-7.37 Implement a function that accepts a PositionalList L of n integers sorted
in nondecreasing order, and another value V , and determines in O(n) time
if there are two elements of L that sum precisely to V . The function should
return a pair of positions of such elements, if found, or None otherwise.

C-7.38 There is a simple, but inefficient, algorithm, called bubble-sort, for sorting
a list L of n comparable elements. This algorithm scans the list n−1 times,
where, in each scan, the algorithm compares the current element with the
next one and swaps them if they are out of order. Implement a bubble sort
function that takes a positional list L as a parameter. What is the running
time of this algorithm, assuming the positional list is implemented with a
doubly linked list?

C-7.41 Write a Scoreboard class that maintains the top 10 scores for a game ap-
plication using a singly linked list, rather than the array that was used in
Section 5.5.1.

P-7.46 Although we have used a doubly linked list to implement the positional
list ADT, it is possible to support the ADT with an array-based imple-
mentation. The key is to use the composition pattern and store a sequence
of position items, where each item stores an element as well as that ele-
ment’s current index in the array. Whenever an element’s place in the array
is changed, the recorded index in the position must be updated to match.
Given a complete class providing such an array-based implementation of
the positional list ADT. What is the efficiency of the various operations?

P-7.47 Implement a CardHand class that supports a person arranging a group of
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
• all of suit(s): Iterate through all cards of suit s that are currently in
the hand.

R-8.15 The LinkedBinaryTree class provides only nonpublic versions of the up-
date methods discussed on page 319. Implement a simple subclass named
MutableLinkedBinaryTree that provides public wrapper functions for each
of the inherited nonpublic update methods.

R-8.26 The collections.deque class supports an extend method that adds a col-
lection of elements to the end of the queue at once. Reimplement the
breadthfirst method of the Tree class to take advantage of this feature.

R-8.30 The build expression tree method of the ExpressionTree class requires
input that is an iterable of string tokens. We used a convenient exam-
ple, (((3+1)x4)/((9-5)+2)) , in which each character is its own to-
ken, so that the string itself sufficed as input to build expression tree.
In general, a string, such as (35 + 14) , must be explicitly tokenized
into list [ ( , 35 , + , 14 , ) ] so as to ignore whitespace and to
recognize multidigit numbers as a single token. Write a utility method,
tokenize(raw), that returns such a list of tokens for a raw string.

C-8.38 Add support in LinkedBinaryTree for a method, delete subtree(p), that
removes the entire subtree rooted at position p, making sure to maintain
the count on the size of the tree. What is the running time of your imple-
mentation?

C-8.39 Add support in LinkedBinaryTree for a method, swap(p,q), that has the
effect of restructuring the tree so that the node referenced by p takes the
place of the node referenced by q, and vice versa. Make sure to properly
handle the case when the nodes are adjacent.

C-8.41 Describe how to clone a LinkedBinaryTree instance representing a proper
binary tree, with use of the attach method.

C-8.49 Let the rank of a position p during a traversal be defined such that the first
element visited has rank 1, the second element visited has rank 2, and so
on. For each position p in a tree T , let pre(p) be the rank of p in a preorder
traversal of T , let post(p) be the rank of p in a postorder traversal of T , let
depth(p) be the depth of p, and let desc(p) be the number of descendants
of p, including p itself. Derive a formula defining post(p) in terms of
desc(p), depth(p), and pre(p), for each node p in T .

C-8.50 Design algorithms for the following operations for a binary tree T :
• preorder next(p): Return the position visited after p in a preorder
traversal of T (or None if p is the last node visited).
• inorder next(p): Return the position visited after p in an inorder
traversal of T (or None if p is the last node visited).
• postorder next(p): Return the position visited after p in a postorder
traversal of T (or None if p is the last node visited).
What are the worst-case running times of your algorithms?

C-8.51 To implement the preorder method of the LinkedBinaryTree class, we re-
lied on the convenience of Python’s generator syntax and the yield state-
ment. Give an alternative implementation of preorder that returns an ex-
plicit instance of a nested iterator class. (See Section 2.3.4 for discussion
of iterators.)

C-8.58 Let T be a tree with n positions. Define the lowest common ancestor
(LCA) between two positions p and q as the lowest position in T that has
both p and q as descendants (where we allow a position to be a descendant
of itself ). Given two positions p and q, describe an efficient algorithm for
finding the LCA of p and q. What is the running time of your algorithm?


