"""
Binary Tree PseudoCode

Operations:
Searching
Insert Node
Deletion
Traversal
Verification
MinValue
MaxValue

class Node
  Node left
  Node right
  value

Advantages over Hash Table;
Memory Efficient - The do not reserve more memory than they need
BST may be traversed to list off all element in order
range searches efficiently

Applications:

Complexities:


BFS and DFSs of above Tree

Breadth First Traversal : 1 2 3 4 5

Depth First Traversals:
      Preorder Traversal : 1 2 4 5 3
      Inorder Traversal  :  4 2 5 1 3
      Postorder Traversal : 4 5 2 3 1

"""

import random;
from Queue import QNode
from Queue import Queue



class Node:

  def __init__(self, val):
    self.left = None
    self.right = None
    self.value = val

class BST:
  def __init__(self, n):
    self.root = n;


  def search_rec(self, n, v):
    '''
    Start at root
    if n is null:
      return not found err
    else if search val == cur value
      return found message
    else if(search val < cur value)
      search(cur.left, val)
    else
      search(cur.right, value)

    O(log n)
    '''

    if(n is None):
      return None
    elif v == n.value:
      return n
    elif v < n.value:
      return self.search_rec(n.left, v)
    else:
      return self.search_rec(n.right, v)

  def search(self, val):
    return self.search_rec(self.root, val)


  def insert_rec(self, n, v):
    '''
    If v < n.value
      if n.val is null
        n.left = new Node(v)
      else
        insert_rec(n.left, v)
    elif v > n.value
      if n.val is null
        n.right = new Node(v)
      else
        insert_rec(n.right, v)
    else:
      return duplicate err
    '''
    if v < n.value:
      if n.left is None:
        n.left = Node(v)
      else:
        self.insert_rec(n.left, v)
    elif v >n.value:
        if n.right is None:
          n.right = Node(v)
        else:
          self.insert_rec(n.right, v)
    else:
      print "Duplicate item"

  def insert(self, v):
    self.insert_rec(self.root, v)

  def find_min_iter(self,n):
    '''
    Go left until the left child is null
    return that child
    O(log n)
    '''
    while(n.left is not None):
      n = n.left
    return n

  def find_min(self):
    return self.find_min_iter(self.root)

  def find_max_iter(self,n):
    '''
    Go right until the right child is null
    return that child
    O(log n)
    '''
    while(n.right is not None):
      n = n.right
    return n
  def find_max(self):
    return self.find_max_iter(self.root)

  def min(self):
    return self.find_min().value

  def max(self):
    return self.find_max().value

  def remove_rec(self, n, v):
    if n is None:
      return None
    if v < n.value:
      # Node is in the left subtree
      n.left = self.remove_rec(n.left, v)
    elif v > n.value:
      # Node is in the right subtree
      n.right = self.remove_rec(n.right, v)
    else:
      # Node has 1 child
      if n.left is None:
        temp = n.right
        n = None
        return temp
      elif n.right is None:
        temp = n.left
        n = None
        return temp

      # Node with 2 children
      temp = self.find_min_iter(n.right)

      # copy inorder successor
      n.value = temp.value

      # delete the inorder successor
      n.right = self.remove_rec(n.right, temp.key)
    return n

  def remove(self, v):
    return self.remove_rec(self.root, v)

  def isBST_rec(self, n, minV, maxV):
    # this should no doubtedly always be true.
    if n is None:
      return True
    if n.value < minV or n.value > maxV:
      return False
    return self.isBST_rec(n.left, minV, n.value) and self.isBST_rec(n.right, n.value, maxV)

  def isBST(self):
    return self.isBST_rec(self.root, self.min(), self.max())

  def in_order_rec(self,n,callback):
    if n is None:
      return
    self.in_order_rec(n.left,callback)
    callback(n)
    self.in_order_rec(n.right,callback)
  def in_order(self):
    self.in_order_rec(self.root, print_node)

  def post_order_rec(self,n,callback):
    if n is None:
      return
    self.post_order_rec(n.left,callback)
    self.post_order_rec(n.right,callback)
    callback(n)

  def post_order(self):
    self.post_order_rec(self.root, print_node)

  def pre_order_rec(self,n,callback):
    if n is None:
      return
    callback(n)
    self.pre_order_rec(n.left,callback)
    self.pre_order_rec(n.right,callback)

  def pre_order(self):
    self.pre_order_rec(self.root, print_node)

  def BFS(self):
    # n = QNode(self.root)
    Q = Queue(self.root)
    while(Q.size > 0):
      n = Q.head
      if n.data is not None: # we have a leaf node skip
        Q.enqueue(QNode(n.data.left))
        Q.enqueue(QNode(n.data.right))
      old = Q.dequeue()
      if old.data is None:
        print ","
      else:
        print old.data.value
    return Q


def print_node(n):
  print n.value


n = 50
node = Node(n)

tree = BST(node)

for i in range(0,50):
  n = random.randint(0, 100)
  tree.insert(n)

tree.BFS()
