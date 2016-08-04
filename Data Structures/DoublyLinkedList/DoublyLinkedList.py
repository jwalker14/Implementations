'''
DOUBLY LINKED LIST
Doesn't Check for duplicates
'''


class Node:
  def __init__(self,v):
    self.v = v
    self.next = None
    self.prev = None

class LinkedList:
  def __init__(self,v):
    self.head = Node(v)
    self.tail = self.head

  def add_first(self, v):
    n = Node(v)
    n.next = self.head
    self.head.prev = n
    self.head = n

  def add_last(self, v):
    n = Node(v)
    self.tail.next = n
    n.prev = self.tail
    self.tail = n