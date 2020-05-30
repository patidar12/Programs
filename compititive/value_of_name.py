'''

You are given Name of chef's friend and using chef's new method of calculating value of string , chef have to find the value of all the names. Since chef is busy , he asked you to do the work from him . The method is a function f(x) as follows -

f(x) = 1 , if x is a consonent

f(x) = 0 , if x is a vowel

Your task is to apply the above function on all the characters in the string S and convert the obtained binary string in decimal number N. Since the number N can be very large, compute it modulo 109+7 .

Input:

First line will contain T, number of testcases. Then the testcases follow.
Each test line contains one String S composed of lowercase English alphabet letters.

Output:
For each case, print a single line containing one integer N modulo 109+7 .

Sample Input:
1
codechef
Sample Output:
173



Solution : (not working)

t = int(input())
vowel = ['a','e','i','o','u']
for i in range(t):
    name = input()
    n = len(name)
    num = 0
    p = 1
    mod = 1000000007
    for i in range(n-1,-1,-1):
        if not name[i] in vowel:
            num = (num+p)%mod
        p = 2*p
    print(num)

'''

def return_binary_code(string):
    binary_code = []
    for i in string:
        if i in ['a','e','i','o','u']:
            binary_code.append(0)
        else:
            binary_code.append(1)
    return binary_code

def convert_to_decimal(binary_code):
    decomal_output = 0
    binary_code.reverse()
    for i in range(len(binary_code)):
        if binary_code[i] == 1:
            decomal_output += pow(2,i)%1000000007
    return decomal_output%1000000007

def main():
    t = eval(input())
    output_list = []
    for i in range(t):
        output_list.append(convert_to_decimal(return_binary_code(input().rstrip().lstrip())))

    for i in range(t):
        print(output_list[i])

main()
