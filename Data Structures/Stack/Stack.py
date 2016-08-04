class Node:
  def __init__(self, v):
    self.v = v
    self.next = None

class Stack:
  def __init__(self, o):
    self.head = Node(o)
    self.size = 1

  def push(self, o):
    o = Node(o)
    o.next = self.head
    self.head = o
    self.size = self.size + 1

  def pop(self):
    if self.size == 0:
      return False

    tmp = self.head
    self.head = tmp.next
    self.size = self.size - 1
    return tmp

  def top(self):
    return self.head

  def size(self):
    return self.size

  def isEmpty(self):
    if self.size < 1:
      return True
    return False


stack = Stack(9)
stack.push(10)
stack.push(11)
stack.push(12)
stack.push(133)
stack.push(15)
stack.push(16)
stack.push(1540)

print stack.top().v
stack.pop()
print stack.top().v
stack.pop()
print stack.top().v
stack.pop()
print stack.top().v
stack.pop()
print stack.top().v
stack.pop()
print stack.top().v
stack.pop()
print stack.top().v
stack.pop()
print stack.top().v
stack.pop()
print stack.top()