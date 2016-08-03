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

"""

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
      print "Not found"
    elif v == n.value:
      print "Found: ", n.value
    elif v < n.value:
      self.search_rec(n.left, v)
    else:
      self.search_rec(n.right, v)

  def search(self, val):
    self.search_rec(self.root, val)


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

  def find_min(self):
    '''
    Go left until the left child is null
    return that child
    O(log n)
    '''
    n = self.root
    while(n.left is not None):
      n = n.left
    return n

  def find_max(self):
    '''
    Go right until the right child is null
    return that child
    O(log n)
    '''
    n = self.root
    while(n.right is not None):
      n = n.right
    return n

  def min(self):
    return self.find_min().value

  def max(self):
    return self.find_max().value


  def delete_rec(self, n, v):
    '''
    if key < n.value
      self.delete_rec(n.left, v)
    '''



n = 10
node = Node(n)

tree = BST(node)

while(n < 50):
  n= n + 1
  tree.insert(n)

print tree.max()
print tree.find_min().value
