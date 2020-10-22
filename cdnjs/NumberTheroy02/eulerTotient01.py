'''
given a number N calculate euler tutient function for value from 1 to N

Input:
10

Output:
Euler Totient Phi For:  1 is 1
Euler Totient Phi For:  2 is 1
Euler Totient Phi For:  3 is 2
Euler Totient Phi For:  4 is 2
Euler Totient Phi For:  5 is 4
Euler Totient Phi For:  6 is 2
Euler Totient Phi For:  7 is 6
Euler Totient Phi For:  8 is 4
Euler Totient Phi For:  9 is 6
Euler Totient Phi For:  10 is 4


'''


def eulerFun(n):
    phi = [i for i in range(n+1)]
    for i in range(2, n+1):
        if phi[i] == i:
            phi[i] = i-1
            for j in range(2*i,n+1,i):
                phi[j] = (phi[j]*(i -1))//i

    for i in range(1, n+1):
        print("Euler Totient Phi For: ",i,'is',phi[i])

n = int(input())
eulerFun(n)
