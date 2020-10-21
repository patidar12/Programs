'''
Extended Euclid Algorithm

Input:
    16 10

Output:
2 2 -3

Input:
    15 10

Output:
5 1 -1

'''


class Triplet:
    x = 0
    y = 0
    gcd = 0

def extendedEuclid(a, b):
    if(b == 0):
        ans = Triplet()
        ans.gcd = a
        # aX + bY = gcd(a,b)
        # if b == 0 then Y = 0
        # aX = a if X = 1
        ans.x = 1
        ans.y = 0
        return ans
    smallAns = extendedEuclid(b, a%b)
    ans = Triplet()
    ans.gcd = smallAns.gcd
    #X = Y1
    #Y = X1 - (a/b)Y1
    ans.x = smallAns.y
    ans.y = smallAns.x - (a//b)*smallAns.y
    return ans

def mInverse(a, m):
    # (a*b) % m  = 1
    # Find B using a and m
    # from multipicative modulo inverse we know that
    # A*B + m*Q = 1
    # AX + BY = 1 from extended eculid algorithm
    # for finding B we have to return value of X from extended Euclid Algorithm
    ans = extendedEuclid(a, m)
    return ans.x

ans = extendedEuclid(16, 10)
print ans.gcd, ans.x, ans.y

ans = extendedEuclid(15, 10)
print ans.gcd, ans.x, ans.y
        

ans = mInverse(5, 17)
print ans

ans = mInverse(5, 12)
print ans
