'''
GFG
https://www.geeksforgeeks.org/merge-sort-for-linked-list/

Merge Sort for Linked Lists

Merge sort is often preferred for sorting a linked list.
The slow random-access performance of a linked list makes some other algorithms
(such as quicksort) perform poorly, and others (such as heapsort) completely impossible.

Input:
N = 5
value[]  = {3,5,2,4,1}
Output: 1 2 3 4 5
Explanation: After sorting the given
linked list, the resultant matrix
will be 1->2->3->4->5.


'''
# Python

def getMiddle(head):
    if(head == None):
        return head
    slow = head
    fast = head
    while(fast.next != None and fast.next.next != None):
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left,right):
    if(left == None):
        return right
    if(right == None):
        return left
    
    if(left.data < right.data):
        result = left
        result.next = merge(left.next,right)
    else:
        result = right
        result.next = merge(left,right.next)
    return result

#User function Template for python3
def mergeSort(head):
    '''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
    '''
    if(head == None or head.next == None):
        return head
    mid = getMiddle(head)
    nextOfMid = mid.next
    mid.next = None
    left = mergeSort(head)
    right = mergeSort(nextOfMid)
    return merge(left,right)
