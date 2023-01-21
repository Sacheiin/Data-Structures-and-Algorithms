#Node is an class object that is connected to one another to form a LinkedList
class Node:
   def __init__(self, value):
	    self.value = value
	    self.next = None
#A linked list is a linear collection of data elements whose order is not given by their physical placement in memory. 
class LinkedLists:
   def __init__(self, value):
       new_node = Node(value)
       self.head = new_node
       self.tail = new_node
       self.length = 1
# A method to print the list	
   def Print_list(self):
	    temp = self.head
	    while temp is not None:
		    print(temp.value)
		    temp = temp.next
#method to append values into list	
   def append(self, value):
	    new_node = Node(value)
	    if self.length == 0:
		    self.head = new_node
		    self.tail = new_node
	    else:
		    self.tail.next = new_node
		    self.tail = new_node
	    self.length +=1
# pop is a method to remove tail value from linked list
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
  # prepend is a method to add head value into linkedlist
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
# pop first is a method remove head value from linked list	
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
# get method is used to fetch value from a linked list
   def get(self, index):
	if index < 0 or index >= self.length:
		return None
	temp = self.head
	for _ in range(index):
		temp = temp.next
	return temp
# set value is a method to replace existing values in a linkedlist
    def set_value(self, index, value):
	temp = self.get(index)
	if temp is not None:
		temp.value = value
		return True
	return False
# insert method is used to insert a value anywhere into a linked list
   def insert(self, index, value):
	if index < 0 or index > self.length:
		return False
	if index == 0:
		return self.prepend(value)
	if index == self.length:
		return self.append(value)
	new_node = Node(value)
	temp = self.get(index - 1)
	new_node.next = temp.next
	temp.next = new_node
	self.length += 1
	return True
# to remove a value from the linked list
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        if index > 0 or index < self.length:
            pre = self.get(index-1)
            temp = self.get(index)
            #pre.next = self.get(index + 1) why not this?
            pre.next = temp.next
            temp.next = None
            self.length -= 1
            return True
        return False
# This method is used to reverse a linked list
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
#This is Node Class for Doubly linked list difference between singular linked list is that this node is linked to its previous node as well 		
class D_Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
# This is a doubly linked list class is a collection of nodes that is with nodes linked to previous and next nodes    
class DoublyLinkedLists:
    def __init__(self, value):
        new_node = D_Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
# This is a simple print list method to return all the values present in doubly linked list       
    def Print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
# this is a append method to add values as a tail to the linked list         
    def append(self, value):
        new_node = D_Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
            return True

'''
my_doubly_linked_list = DoublyLinkedLists(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.Print_list()
my_linked_lists = LinkedLists(1)
my_linked_lists.insert(2, 2)
my_linked_lists.set_value(3, 3)
my_linked_lists.Print_list()
my_linked_lists.append(4)
my_linked_lists.append(5)
my_linked_lists.append(6)
my_linked_lists.Print_list()
print('\n')
my_linked_lists.reverse()
my_linked_lists.Print_list()
my_linked_lists.remove(6)
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
'''
