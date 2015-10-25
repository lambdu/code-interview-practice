"""
tried to transpose tree and red-black tree from Okazaki to python
both work, but the translation makes some of the code sorta clunky.

Not production quality code, may be some lurking bugs.

Red Black tree:

>>> s = tree(5)
>>> y = s.insert(4)
>>> y
5 black [4 red [[], []], []]
>>> z = y.insert(6)
>>> z
5 black [4 red [[], []], 6 red [[], []]]
>>> z = y.insert(3)
>>> z
4 black [3 black [[], []], 5 black [[], []]]
>>> y = s.insert(3)
>>> z = y.insert(4)
>>> z
4 black [3 black [[], []], 5 black [[], []]]
>>> z.member(3)
True

Set:

>>> set(5)
5 [[], []]
>>> set(5,set(4), set(3))
5 [4 [[], []], 3 [[], []]]

"""

# unbalanced set
class mts(object):
  def __init__(self):
    self.value = None

  def member(self, value):
    return False

  def insert(self, value):
    return set(value)

  def __str__(self):
    return "[]"

  __repr__ = __str__

class set(object):
  def __init__(self, value):
    self.value = value
    self.left = mts()
    self.right = mts()

  def insert(self, value):
    if value > self.value:
      if self.left is mts():
        self.left = value
      else:
        self.left = self.left.insert(value)
    elif value == self.value:
      raise
    else:
      if self.right is mts():
        self.right = value
      else:
        self.right = self.right.insert(value)
    return self

  def member(self, value):
    return self.value == value or (self.left.member(value) or self.right.member(value))

  def __str__(self):
    return str(self.value) + " [" + str(self.left) + ", " + str(self.right) + "]"


  __repr__ = __str__

# Red Black trees

class et(object):
  def __init__(self):
    self.value = None
    self.color = "black"

  def __str__(self):
    return "[]"

  def member(self, value):
    return False

class tree(object):
  def __init__(self, value, color="red", left=None, right= None):
    self.value = value
    self.color = color
    if left == None:
      self.left = et()
    else:
      self.left = left
    if right == None:
      self.right = et()
    else:
      self.right = right

  def __str__(self):
    return str(self.value) + " " + str(self.color) + " [" + str(self.left) + ", " + str(self.right) + "]"

  def member(self, value):
    return self.value == value or (self.left.member(value) or self.right.member(value))

  def insert(self, value):
    def ins(ot, nv):
      if type(ot) == type(et()):
        return tree(nv, "red", et(), et())
      if nv < ot.value:
        ot = balance(ot.color, ins(ot.left, nv), ot.value, ot.right)
      elif nv > ot.value:
        ot = balance(ot.color, ot.left, ot.value, ins(ot.right, nv))
      else:
        return ot
      return ot

    self = ins(self, value)
    self.color = "black"
    return self

  __repr__ = __str__

def balance(color, left, value, right):
  if left.color == "red" and left.left.color == "red":
    return tree(left.value, "red", tree(left.left.value, "black",
                  left.left.left, left.left.right),
                  tree(value, "black", left.right, right))
  elif left.color == "red" and left.right.color == "red":
    return tree(left.right.value, "red", tree(left.value, "black",
      left.left, left.right.left), tree(value, "black", left.right.right, right))
  elif right.color == "red" and right.right.color == "red":
    return tree(right.value, "red", tree(right.value, "black", left, right.left),
      tree(right.right.value, "black", right.right.left, right.right.right))
  elif right.color == "red" and right.left.color == "red":
    return tree(right.left.value, "red", tree(value, "black", left, right.left.left),
                tree(right.value, "black", right.left.right, right.right))
  else:
    return tree(value, color, left, right)












