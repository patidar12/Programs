'''
Help Me Pradyumana!

Pradyumn is tired of using auto - correct feature in his smartphone. He needs to correct his auto - correct more times than the auto - correct corrects him.
Pradyumn is thinking to make his own app for mobile which will restrict auto - correct feature, instead it will provide auto - completion. 
Whenever Pradyumn types factorial, auto - correct changes it to fact. Pradyumn's App will show options such as fact, factorial, factory.
Now, he can chose from any of these options. As Pradyumn is busy with his front - end work of his App. He asks you to help him. 
He said "You will be given set of words(words may repeat too but counted as one only). Now, as user starts the app, he will make queries(in lowercase letters only).
So, you have to print all the words of dictionary which have the prefix same as given by user as input. And if no such words are available, add this word to your dictionary."
As you know, Pradyumn want this app to be as smart as him :P So, implement a program for him such that he can release it on Fun Store.

INPUT CONSTRAINTS
1≤N≤30000
sum(len(string[i]))≤2∗10^5
1≤Q≤10^3

INPUT FORMAT
Single integer N which denotes the size of words which are input as dictionary
N lines of input, where each line is a string of consisting lowercase letter
Single integer Q which denotes the number of queries.
Q number of lines describing the query string on each line given by user

OUTPUT FORMAT
If auto - completions exists, output all of them in lexicographical order else output "No suggestions" without quotes

NOTE: All strings are lowercase

SAMPLE INPUT
3
fact
factorial
factory
2
fact
pradyumn

SAMPLE OUTPUT
fact
factorial
factory
No suggestions

'''
class TrieNode:
    def __init__(self):
        self.arr = [None]*26
        self.pre = set()

def insert(head, string):
    n = len(string)
    temp = head
    for i in range(n):
        index = ord(string[i]) - ord('a')
        if not temp.arr[index]:
            temp.arr[index] = TrieNode()
        temp = temp.arr[index]
        temp.pre.add(string)

def query(head, string):
    temp = head
    n = len(string)
    for i in range(n):
        index = ord(string[i]) - ord('a')
        temp = temp.arr[index]
        if not temp:
            insert(head, string)
            return ['No suggestions']
    return temp.pre

n = int(input().strip())
head = TrieNode()
for i in range(n):
    string = input().strip()
    insert(head, string)

q = int(input().strip())
for i in range(q):
    string = input().strip()
    ans = query(head, string)
    ans = sorted(ans)
    for val in ans:
        print(val)

