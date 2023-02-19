# Author: Aline Botti
# GitHub username: Aline_Lima
# Date: 11/01/2022
# Description: 

"""
add method - DONE
remove method  - DONE
contains - DONE
insert - DONE
reverse -
recursive to_plain_list() that converts LL into List
_head attribute with getter - DONE
"""
 #fileName is Linkedlist.py
 #Node will be the individual nodes that makes up the linked list

class Node:
    #attributes through __init__()
    def __init__(self, data):
        self.data = data
        self.next = None

    #LinkedList will be the collection of Nodes that point to the next one
    class LinkedList:
        def __init__(self):
            self._head = Node(None, None)
            self.tail = None
        def get_head(self):
            return self._head

        def add(self, node):
            #The comparison operator == compares whether the two are equal or not equal
            if self._head.next == None:
                #the assignment operator sets a variable to a value
                self._head.next = node
                self.tail = node
            else:
                self.tail.next = node
                self.tail = self.tail.next

        def remove(self, index):
            #if we are only caring about the first item, just remove that first item
             if index == 0:
              self._head.next = self._head.next.next

             else:
                counter = 0
                current = Node(0,self._head.next)

                while counter < index - 1 and current.next != None:
                        counter += 1
                        current.next = current.next.next

                if current.next != None and current.next.next != None:
                    current.next.next = current.next.next.next

        def contains(self, target):
            #we need to iterate through the list, but because it's a custom class we can't use the foreach loop
            current = Node(0, self._head.next)
            while current.next != None:
                if current.next.data == target:
                    return True
                else:
                 current.next = current.next.next
            return False

        def insert(self, node, index):
            if index == 0:
                node.next = self._head.next
                self.head.next = node
            else:
                current = Node(None, self._head.next)
                counter = 0

                while counter < index - 1:
                    counter += 1
                    current = current.next

                node.next = current.next.next
                current.next = node

        def reverse(self):
            # find the node before the tail, add the tail, and set the "current" marker at the one before the tail
            current = Node(None, self._head.next)
            # becuase we are "creating" a new list, both the head and the tail point to the same item to start with
            newHead = self.tail
            newTail = self.tail

            while newTail != self._head.next:
                if current.next.next == newTail:
                    newTail.next = current.next
                    newTail = newTail.next
                    current.next = self._head.next
                else:
                    current.next = current.next.next

            # after all data has been added, set up newTail to be a proper tail
            newTail.next = None
            self._head = newHead
            self.tail = newTail

            # recursive version - a function that calls itself
            def to_plain_list(self, current):
                output = []
                # first goal of recursion: to end
                if current == self.tail:
                    output.append(current.data)
                    return output
                else:
                    output.append(current.data)
                    return output + to_plain_list(current.next)