'''
SUBXOR

A straightforward question. Given an array of positive integers you have to print the number of subarrays whose XOR is less than K.
Subarrays are defined as a sequence of continuous elements Ai, Ai+1, ..., Aj . XOR of a subarray is defined as Ai ^ Ai+1 ^ ... ^ Aj. Symbol ^ is Exclusive Or.

Input Format
First line contains T, the number of test cases. 
Each of the test case consists of N and K in one line, followed by N space separated integers in next line.

Output Format
For each test case, print the required answer.

Constraints:
1 ≤ T ≤ 5
1 ≤ N ≤ 10^5
1 ≤ A[i] ≤ 10^5
1 ≤ K ≤ 10^6

Sample Input
1
5 2
4 1 3 2 7   

Sample Output
3



'''

class TrieNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.cnt = 0

def insert(head, num):
    temp = head
    for i in range(31,-1,-1):
        b = (num>>i) & 1
        if(b == 0):
            if not temp.left:
                temp.left = TrieNode()
            temp.left.cnt += 1
            temp = temp.left
        else:
            if not temp.right:
                temp.right = TrieNode()
            temp.right.cnt += 1
            temp = temp.right

def query(head, num, k):
    temp = head
    xor = 0
    for i in range(31, -1, -1):
        vb = (num >> i) & 1
        kb = (k >> i) & 1
        if(kb != 0):
            if(vb != 0):
               if temp.right:
                   xor +=  temp.right.cnt
               temp = temp.left
            else:
                if temp.left:
                    xor += temp.left.cnt
                temp = temp.right
        else:
            if vb != 0:
                temp = temp.right
            else:
                temp = temp.left
        if not temp:
            break

    return xor

tcs = int(input())
for tc in range(tcs):
    n, k = map(int, input().split())
    arr = [int(x) for x in input().split()]
    ans = 0
    preXor = 0
    head = TrieNode()
    insert(head, preXor)
    for i in range(n):
        preXor ^= arr[i]
        ans += query(head, preXor, k)
        insert(head, preXor)
    print(ans)

