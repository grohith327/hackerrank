"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""

def Insert(head, data):
    if(head == None):
        head = Node()
        head.data = data
        return head
    temp = Node()
    prev = Node()
    temp = head
    while(temp != None):
        prev = temp
        temp = temp.next
    t = Node()
    t.data = data
    prev.next = t
    return head

  
  
  
  
  
  
