"""
**Calcualte Area of ractengle after removing the intersection part!
Input: The input file consist of two line. Each line will be of the form x1,y1,x2,y2 describing the bottom-left and top-right corners of the rectangle.
Output: Single Integer, total area covered by rectangles!

Sample Input:
1 1 3 4
2 3 6 7

Sample Output:
21

"""

x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())
A1 = (x2-x1)*(y2-y1)
A2 = (x4-x3)*(y4-y3)
left = max(x1,x3)
right = min(x2,x4)
bottom = max(y1,y3)
top = min(y2,y4)
Aintr = 0
if(left < right and bottom < top):
    Aintr = (right-left)*(top-bottom)

ans = A1+A2-Aintr
print(ans)
