'''
Maximum XOR Subarray

Given an array of n integers, find subarray whose xor is maximum.

Input Format
First line contains single integer n (1<=n<=1000000).
Next line contains n space separated integers.

Output Format
Print xor of the subarray whose xor of all elements in subarray is maximum over all subarrays.

Constraints
1 <= n <= 1000000
1 <= A[i] <=100000 

Sample Input
4
1 2 3 4

Sample Output
7

'''
class TrieNode:
    def __init__(self):

        self.left = None
        self.right = None
def insert(head, num):
    temp = head
    for i in range(31,-1,-1):
        b = (num >> i)&1
        if(b == 0):
            if(not temp.left):
                temp.left = TrieNode()
            temp = temp.left
        else:
            if(not temp.right):
                temp.right = TrieNode()
            temp = temp.right

def getMax(head, num):

    temp = head
    maxXor = 0
    for i in range(31, -1, -1):
        b = (num >> i)&1
        if(b == 0):
            if(temp.right):
                maxXor += pow(2,i)
                temp = temp.right
            else:
                temp = temp.left

        else:
            if(temp.left):
                maxXor += pow(2,i)
                temp = temp.left
            else:
                temp = temp.right
    return maxXor


n = int(input())
arr = [int(x) for x in input().split()]
maxXor = -2**31
preXor = 0
head = TrieNode()
for i in range(n):
    preXor ^= arr[i]
    insert(head, preXor)
    maxXor = max(maxXor, getMax(head, preXor))

print(maxXor)
