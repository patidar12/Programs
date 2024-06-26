'''
Search Engine

Let us see how search engines work. Consider the following simple auto complete feature. When you type some characters in the text bar,
the engine automatically gives best matching options among it's database. Your job is simple. Given an incomplete search text, output the best search result.
Each entry in engine's database has a priority factor attached to it. We consider a result / search suggestion best if it has maximum weight 
and completes the given incomplete search query. For each query in the input, print the maximum weight of the string in the database, 
that completes the given incomplete search string. In case no such string exists, print -1.

INPUT
First line contains two integers n and q, which represent number of database entries and number of search queries need to be completed.
Next n lines contain a string s and an integer weight, which are the database entry and it's corresponding priority.

Next q lines follow, each line having a string t, which needs to be completed.

OUTPUT
Output q lines, each line containing the maximum possible weight of the match for given query, else -1, in case no valid result is obtained.

CONSTRAINTS
1 ≤ n, weight, len(s), len(t) ≤ 10^6
1 ≤ q ≤ 10^5
total length of all strings in database entries ≤ 10^6
total length of all query strings ≤ 10^6

SAMPLE INPUT
2 1
hackerearth 10
hackerrank 9
hacker

SAMPLE OUTPUT
10

'''

class TrieNode:
    def __init__(self):
        self.arr = [None]*26
        self.cnt = 0

def insert(head, string, num):
    n = len(string)
    temp = head
    for i in range(n):
        index = ord(string[i]) - ord('a')
        if not temp.arr[index]:
            temp.arr[index] = TrieNode()
        temp = temp.arr[index]
        temp.cnt = max(num, temp.cnt)

def query(head, string):
    temp = head
    n = len(string)
    for i in range(n):
        index = ord(string[i]) - ord('a')
        temp = temp.arr[index]
        if not temp:
            return -1

    return temp.cnt

n, q = map(int, input().split())
head = TrieNode()
for i in range(n):
    string, val = input().split()
    val = int(val)
    insert(head, string, val)

for i in range(q):
    string = input().strip()
    print(query(head, string))
