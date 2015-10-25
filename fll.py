# Not related to Okazaki's linked list implementation
# tried to implement a list in a more functional style

class mt(object):
  def __init__(self):
    self.value = None

  def __str__(self):
    return "[]"

  __repr__ = __str__

class link(object):
  def __init__(self, lst, value):
    self.value = value
    self.next = lst

  def __str__(self):
    return str(self.value) + " :: " + str(self.next)

  __repr__ = __str__

def append(lst, val):
  return link(lst, val)

def prepend(lst, val):
  if lst.value == None:
    return link(mt(), val)
  else:
    return link(prepend(lst.next, val), lst.value)


def length(lst):
  return len_hlp(lst, 0)

def len_hlp(lst, acc):
  if lst.value == None:
    return acc
  else:
    return len_hlp(lst.next, acc + 1)

def ins(lst, val, idx):
  if idx == 0:
    return link(lst, val)
  elif lst.value == None:
    raise
  else:
    return link(ins(lst.next, val, idx - 1), lst.value)

def pp(lst1, lst2):
  if lst1.value == None:
    return lst2
  else:
    return link(pp(lst1.next, lst2), lst1.value)






