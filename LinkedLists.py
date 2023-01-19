class Node:
   def __init__(self, value):
	    self.value = value
	    self.next = None

class LinkedLists:
   def __init__(self, value):
       new_node = Node(value)
       self.head = new_node
       self.tail = new_node
       self.length = 1
	
   def Print_list(self):
	    temp = self.head
	    while temp is not None:
		    print(temp.value)
		    temp = temp.next
		
   def append(self, value):
	    new_node = Node(value)
	    if self.length == 0:
		    self.head = new_node
		    self.tail = new_node
	    else:
		    self.tail.next = new_node
		    self.tail = new_node
	    self.length +=1
	
   def pop(self):
	    if self.length == 0:
		    return None
	    temp = self.head
	    pre = self.head
	    while(temp.next is not None):
		    pre = temp
		    temp = temp.next
	    self.tail = pre
	    self.tail.next = None
	    self.length -= 1
	    if self.length == 0:
		    self.head = None
		    self.tail = None
	    return temp
  
   def prepend(self, value):
	    new_node = Node(value)
	    if self.length == 0:
		    self.head = new_node
		    self.tail = new_node
	    else:
		    new_node.next = self.head
		    self.head =new_node
	    self.length += 1
	    return True
	
   def pop_first(self, value):
	if self.length == 0:
		return None
	temp = self.head
	self.head = self.head.next
	temp.next = None
	self.length -= 1
	if self.length == 0:
		self.tail = None
	return temp.value

   def get(self, index):
	if index < 0 or index >= self.length:
		return None
	temp = self.head
	for _ in range(index):
		temp = temp.next
	return temp




my_linked_lists = LinkedLists(4)
my_linked_lists = LinkedLists(12)
my_linked_lists = LinkedLists(13)
my_linked_lists.Print_list()
my_linked_lists.append(17)
print('head:', my_linked_lists.head.value)
print('tail:',my_linked_lists.tail.value)
print('Length:', my_linked_lists.length)
#returns 2 nodes
my_linked_lists.pop()
my_linked_lists.Print_list()
#returns 1 node
my_linked_lists.pop()
my_linked_lists.Print_list()
#returns None
my_linked_lists.pop()
my_linked_lists.Print_list()
my_linked_lists.prepend(41)
my_linked_lists.Print_list()
#returns 2 nodes
print(my_linked_lists.pop_first())
#returns 1 node
print(my_linked_lists.pop_first())
#returns None
print(my_linked_lists.pop_first())
print(my_linked_lists.get(3))
