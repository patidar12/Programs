'''
As lockdown is going on so no is allowed to go outside , so Chef has come with an innovative idea for food home delivery using drone. But there is an issue with it , the drone can move forward or backward a fix number of steps x .

All the houses and chef restaurant are all in a straight line . Homes which need delivery are located at H[i] and chef is located at y coordinate .

If Drone is at a location R, then it can move to R−x or R+x .

Help chef find maximum value of x to complete all the deliveries as he is busy managing the orders.

Input:
First line will contain n and R, number of houses that need delivery and the correct coordinate of chef (Drone).
Second line contains n integers , the coordinate of all homes that need delivery.
Output:
The maximum value of x , so that drone delivers to all houses.

Sample Input:
3 1
3 5 11
Sample Output:
2

Solution 1:
    def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

    a = [4, 10, 16, 14]
    n,r=map(int,input().split())
    lst=[r]
    lst.extend(list(map(int,input().split())))
    nlst=[]
    for i in range(0,n-1):
	nlst.append(lst[i+1]-lst[i])
    result = nlst[0]
    for i in nlst[1:]:
       result = gcd(result, i)
 
    print(result)

'''

# cook your dish here
def find_gcd(x, y):
    while(y):
        x, y = y, x % y

    return x

n,r=map(int,input().split())
l=list(map(int,input().split()))
b=[l[0]-r]
for i in range(n-1):
    b.append(l[i+1]-l[i])

num1=b[0]
num2=b[1]
gcd=find_gcd(num1,num2)
for j in range(2,len(b)):
    gcd=find_gcd(gcd,b[i])
print(gcd)
