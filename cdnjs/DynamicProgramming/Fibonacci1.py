'''
Print Nth Fibonacci Number

Input: 
5

Output:
5

Input:
10

Output:
55


'''

#code
def feb(n):
    # Simple recursive solution
    if(n == 0 or n == 1):
        return n
    return feb(n-1) + feb(n-2)

def febR(n, arr):
    # DP recursive solution
    if(n == 0 or n == 1):
        return n
    if(arr[n] > 0):
        return arr[n]
    output = febR(n-1, arr) + febR(n-2, arr)
    arr[n] = output
    return output

def febI(n,arr):
    # DP iterative solution
    arr[0] = 0
    arr[1] = 1
    for i in range(2,n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]

def getNthFeb(n):
    arr = [0]*(n+1)
    print(feb(n))
    print(febR(n,arr))
    print(febI(n,arr))

n = int(input())
getNthFeb(n)
