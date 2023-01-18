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
	
	
my_linked_lists = LinkedLists(4)
my_linked_lists = LinkedLists(12)
my_linked_lists = LinkedLists(13)
print('head:', my_linked_lists.head.value)
print('tail:',my_linked_lists.tail.value)
print('Length:', my_linked_list.length)
