'''
Winning Lottery
Send Feedback
Harshit knows by his resources that this time the winning lottery number is the smallest number whose sum of the digits is S and the number of digits is D.
You have to help Harshit and print the winning lottery number.

Input Format
The Input line contains two space-separated integers: S,D

Output Format
The output contains a single integer denoting the winning lottery number

Constraints
1 <= D <= 1000
1 <= S <= 9*D

Time Limit: 1 second

Sample Input1:
9 2

Sample Output1:
18

Explanation
There are many other possible numbers like 45, 54, 90, etc with the sum of digits as 9 and number of digits as 2. The smallest of them is 18

'''

def getLotryNumber(S,D):
    arr = [None]*D
    S -= 1
    for i in range(D-1,0,-1):
        if S > 9:
            arr[i] = 9
            S -= 9
        else:
            arr[i] = S
            S = 0
    arr[0] = S + 1
    listToStr = ''.join([str(elem) for elem in arr])
    return listToStr

S,D = [int(x) for x in input().split()]
print(getLotryNumber(S,D))
