class QNode:
  def __init__(self, n):
    self.data = n
    self.next = None

class Queue:
  def __init__(self, n):
    m = QNode(n)
    self.head = m
    self.tail = m
    self.size = 1
  def enqueue(self,n):
    self.tail.next = n
    self.tail = n
    self.size = self.size + 1
  def dequeue(self):
    temp = self.head
    self.head = temp.next;
    self.size = self.size - 1
    return temp