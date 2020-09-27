'''
SPOJ:
    https://www.spoj.com/problems/LOPOV/

LOPOV - Lopov
#ad-hoc-1
 

The difficult economic situation in the country and reductions in government agricultural subsidy funding have caused Mirko to change his career again, 
this time to a thief. His first professional endeavour is a jewellery store heist. The store contains N pieces of jewellery, and each piece has
some mass Mi and value Vi. Mirko has K bags to store his loot, and each bag can hold some maximum mass Ci. He plans to store all his loot in these bags, 
but at most one jewellery piece in each bag, in order to reduce the likelihood of damage during the escape. Find the maximum total jewellery value that Mirko can “liberate”. 
The difficult economic situation in the country and reductions in government agricultural subsidy funding have caused Mirko to change his career again,
this time to a thief. His first professional endeavour is a jewellery store heist. 

The store contains N pieces of jewellery, and each piece has some mass Mi and value Vi. Mirko has K bags to store his loot, and each bag can hold some maximum mass Ci.
He plans to store all his loot in these bags, but at most one jewellery piece in each bag, in order to reduce the likelihood of damage during the escape. 

Find the maximum total jewellery value that Mirko can “liberate”. 

Input
The first line of input contains two numbers, N and K (1 ≤ N, K ≤ 300 000). 

Each of the following N lines contains a pair of numbers, Mi and Vi (1 ≤ Mi, Vi ≤ 1 000 000).

Each of the following K lines contains a number, Ci (1 ≤ Ci ≤ 100 000 000). 

All numbers in the input are positive integers. 

Output
The first and only line of output must contain the maximum possible total jewellery value. 

Example
Input:
 
2 1 
5 10 
100 100 
11 

Output:
10

Input:
 
3 2 
1 65 
5 23 
2 99 
10 
2 

Output:
164


solution:
    sort value array in decresing order on the basis of value if value is qual than less mass come first
    store loot bag array in multiset
    for every mass in value array:
        find lower_bound in loot_array:
            add value in ans
            remove bag from loot_array

'''
