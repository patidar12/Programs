'''
Maximum Sum In Subarray
Send Feedback
You are given a sequence A[1], A[2], ..., A[N] . ( |A[i]| ≤ 15007 , 1 ≤ N ≤ 50000 ). A query is defined as follows:
Query(x,y) = Max { a[i]+a[i+1]+...+a[j] ; x ≤ i ≤ j ≤ y }.
Given M queries, your program must output the results of these queries.
Input
The first line of the input file contains the integer N.
In the second line, N numbers follow.
The third line contains the integer M.
M lines follow, where line i contains 2 numbers xi and yi.
Output
Your program should output the results of the M queries, one 
query per line.
Sample Input:
3 
-1 2 3 
1
1 2
Sample Output:
2

'''

from sys import maxsize
INT_MIN = -maxsize
class node:
	def __init__(self):
		self.sum = 0
		self.prefixsum = 0
		self.suffixsum = 0
		self.maxsum = 0

def build(tree: list, arr: list, low: int, high: int, index: int):
	if low == high:
		tree[index].sum = arr[low]
		tree[index].prefixsum = arr[low]
		tree[index].suffixsum = arr[low]
		tree[index].maxsum = arr[low]
	else:
		mid = (low + high) >> 1
		build(tree, arr, low, mid, 2 * index + 1)
		build(tree, arr, mid + 1, high, 2 * index + 2)
		tree[index].sum = tree[2 * index + 1].sum + tree[2 * index + 2].sum
		tree[index].prefixsum = max(
			tree[2 * index + 1].prefixsum,
			tree[2 * index + 1].sum + tree[2 * index + 2].prefixsum)
		tree[index].suffixsum = max(
			tree[2 * index + 2].suffixsum,
			tree[2 * index + 2].sum + tree[2 * index + 1].suffixsum)
		tree[index].maxsum = max(tree[index].prefixsum,
			max(tree[index].suffixsum,
				max(tree[2 * index + 1].maxsum,
					max(tree[2 * index + 2].maxsum,
						tree[2 * index + 1].suffixsum +
						tree[2 * index + 2].prefixsum))))

def query(tree: list, index: int, low: int,
		high: int, l: int, r: int) -> node:

	result = node()
	result.sum = result.prefixsum = result.suffixsum = result.maxsum = INT_MIN

	if r < low or high < l:
		return result

	if l <= low and high <= r:
		return tree[index]

	mid = (low + high) >> 1

	if l > mid:
		return query(tree, 2 * index + 2,
						mid + 1, high, l, r)
	if r <= mid:
		return query(tree, 2 * index + 1, low, mid, l, r)

	left = query(tree, 2 * index + 1, low, mid, l, r)
	right = query(tree, 2 * index + 2, mid + 1, high, l, r)

	result.sum = left.sum + right.sum
	result.prefixsum = max(left.prefixsum,
					left.sum + right.prefixsum)

	result.suffixsum = max(right.suffixsum,
						right.sum + left.suffixsum)
	result.maxsum = max(result.prefixsum,
		max(result.suffixsum,
			max(left.maxsum, max(right.maxsum,
			left.suffixsum + right.prefixsum))))

	return result

n = int(input().strip())
tree = [None] * (4 * n)
for i in range(len(tree)):
	tree[i] = node()
arr = [int(x) for x in input().split()]
build(tree,arr, 0, n - 1, 0)
q = int(input().split()[0])
for i in range(q):
    l,r = map(int,input().split())
    print(query(tree, 0, 0, n - 1, l - 1, r - 1).maxsum)

