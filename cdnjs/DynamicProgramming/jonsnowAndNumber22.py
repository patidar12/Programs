'''
Jon Snow and his favourite number

Jon Snow now has to fight with White Walkers. He has n rangers, each of which has his own strength. Also Jon Snow has his favourite number x.
Each ranger can fight with a white walker only if the strength of the white walker equals his strength. He however thinks that his rangers are 
weak and need to improve. Jon now thinks that if he takes the bitwise XOR of strengths of some of rangers with his favourite number x,
he might get soldiers of high strength. So, he decided to do the following operation k times:
Arrange all the rangers in a straight line in the order of increasing strengths.
Take the bitwise XOR of the strength of each alternate ranger with x and update it's strength.
Suppose, Jon has 5 rangers with strengths [9, 7, 11, 15, 5] and he performs the operation 1 time with x = 2. He first arranges them 
in the order of their strengths, [5, 7, 9, 11, 15]. Then he does the following:

The strength of first ranger is updated to 5 xor 2, i.e. 7.
The strength of second ranger remains the same, i.e. 7.
The strength of third ranger is updated to 9 xor 2, i.e. 11.
The strength of fourth ranger remains the same, i.e. 11.
The strength of fifth ranger is updated to 15 xor 2, i.e. 13.
The new strengths of the 5 rangers are [7, 7, 11, 11, 13]

Now, Jon wants to know the maximum and minimum strength of the rangers after performing the above operations k times. He wants your help for this task. Can you help him?

Input
First line consists of three integers n, k, x (1 ≤ n ≤ 10^5, 0 ≤ k ≤ 10^5, 0 ≤ x ≤ 10^3) — number of rangers Jon has,
the number of times Jon will carry out the operation and Jon's favourite number respectively.

Second line consists of n integers representing the strengths of the rangers a1, a2, ..., an (0 ≤ ai ≤ 10^3).

Output
Output two integers, the maximum and the minimum strength of the rangers after performing the operation k times.

Sample Input
5 1 2
9 7 11 15 5

Sample Output
13 7

'''

n,k,x = map(int, input().split())
arr = [int(x) for x in input().split()]
freq = [[0 for i in range(1024)] for j in range(2)]
ma = 0
for i in range(n):
    a = arr[i]
    ma = max(ma, a)
    ma = max(ma, a^x)
    freq[0][a] += 1
    freq[1][a] += 1

ma = min(2*ma, 1023)
for i in range(k):
    c = 0
    for j in range(ma+1):
        if(freq[0][j] == 0):
            continue
        if(c%2 == 0):
            p = (freq[0][j]+1)//2
            freq[1][j^x] += p
            freq[1][j] -= p
        else:
            p = freq[0][j]//2
            freq[1][j^x] += p
            freq[1][j] -= p
        c += freq[0][j]
    for j in range(ma+1):
        freq[0][j] = freq[1][j]

for i in range(ma, -1, -1):
    if(freq[0][i] > 0):
        print(i, end = ' ')
        break

for i in range(ma+1):
    if(freq[0][i] > 0):
        print(i, end = ' ')
        break


