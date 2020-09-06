"""

Codingnija has given you N rectangels, which are centered in the center 
of the Cartesian system and their sides are parallel to the coordinat
axes. Each rectangle is uniquely identified with its width(along the x-
axis) and height (along the y-axis). Navdeep has coloured each rectangle 
in a certain colour and now wants to know the area of the coloured part
of the paper. Please refer to the image below for more details. The given 
image for the test case.

Imput Format:
N (1 <= N <= 1000000)
X and Y (2 <= X,Y <= 10^7)



Input:
3
8 2
4 4
2 6

Output:
28

Input:
5
2 10
4 4
2 2
8 8
6 6

Output:
68

def merge(arr, left, mid, right):
    i = left
    j = mid
    k = 0
    temp = [None]*(right-left+1)
    while(i < mid and j <= right):
        if(arr[i][0] > arr[j][0]):
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1
    while(i < mid):
        temp[k] = arr[i]
        k += 1
        i += 1
    while(j <= right):
        temp[k] = arr[j]
        k += 1
        j += 1
    k = 0
    for i in range(left,right+1):
        arr[i] = temp[k]
        k += 1

def mergeSort(arr,left, right):
    if(left < right):
        mid = left + (right-left)//2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        merge(arr, left,mid+1,right)

def calArea(arr,n):
    mergeSort(arr,0,n-1)
    curr = arr[0]
    area = 0
    i = 1
    while(i < n):
        if(curr[1] < arr[i][1]):
            x = curr[0] - arr[i][0]
            y = curr[1]
            area += (x*y)
            curr = arr[i]
        i += 1       
    x = curr[0] - 0
    y = curr[1]
    area += (x*y)
    return area

n = int(input())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))
print(calArea(arr,n))


"""




n = int(input())
'''
maximum range of height is 10^7
So we are taking half size of array
'''
height = [0]*(5000000+2)
max_x = 0
for i in range(n):
    x,y = map(int,input().split())
    if(height[x//2] < y):
        height[x//2] = y
    if(max_x < x//2):
        max_x = x//2
area = 0
for i in range(max_x,0,-1):
    if(height[i] < height[i+1]):
        height[i] = height[i+1]
    area += height[i]

print(2*area)


