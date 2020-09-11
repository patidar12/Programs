'''
GFG
https://www.geeksforgeeks.org/sublist-search-search-a-linked-list-in-another-list/

Given two linked lists, the task is to check whether the first list is present in 2nd list or not.

Input  : list1 =  10->20
         list2  = 5->10->20
Output : LIST FOUND

Input  : list1 =  1->2->3->4
         list2  = 1->2->1->2->3->4
Output : LIST FOUND

Input  : list1 =  1->2->3->4
         list2  = 1->2->2->1->2->3
Output : LIST NOT FOUND

'''

# Python

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,value):
        newNode = Node(value)
        if(self.head == None):
            self.head = newNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = newNode

def createList(listInput):
    linkedList = LinkedList()
    for ele in listInput:
        linkedList.append(ele)
    return linkedList

def isContain(lis1, lis2):
    curr1 = lis1
    curr2 = lis2
    while(curr2 != None):
        if(curr1.value == curr2.value):
            curr1 = curr1.next
            curr2 = curr2.next
        else:
            curr1 = lis1
            if(curr1.value == curr2.value):
                curr1 = curr1.next
            curr2 = curr2.next
        if(curr1 == None):
            return True
    return False

lis1 = [int(x) for x in input().split()]
lis2 = [int(x) for x in input().split()]
first = createList(lis1)
second = createList(lis2)
print(isContain(first.head,second.head))
