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
	
	
my_linked_lists = LinkedLists(4)
my_linked_lists = LinkedLists(12)
my_linked_lists = LinkedLists(13)
my_linked_lists.Print_list()
my_linked_lists.append(17)
print('head:', my_linked_lists.head.value)
print('tail:',my_linked_lists.tail.value)
print('Length:', my_linked_list.length)
