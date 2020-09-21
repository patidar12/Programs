'''
GFG:
    https://www.geeksforgeeks.org/remove-invalid-parentheses/

An expression will be given which can contain open and close parentheses and optionally some characters,
No other operator will be there in string. We need to remove minimum number of parentheses to make the input string valid.
If more than one valid output are possible removing same number of parentheses then print all such output.

Examples:

Input  : str = “()())()” -

Output : ()()() (())()

There are two possible solutions
"()()()" and "(())()"

Input  : str = (v)())()

Output : (v)()()  (v())()

'''

def isParenthesis(ch):
    return (ch == ')' or ch == '(')

def isValidString(str1):
    count = 0
    for i in range(len(str1)):
        if(str1[i] == '('):
            count += 1
        if(str1[i] == ')'):
            count -= 1
        if(count < 0):
            return False
    return (count == 0)
def removeInvalidPrenth(exp):
    if(len(exp) == 0):
        return
    q = []
    visited = set()
    level = False
    q.append(exp)
    visited.add(exp)
    while(len(q) > 0):
        exp = q.pop(0)
        if(isValidString(exp)):
            print(exp)
            level = True
        if(level == True):
            continue
        for i in range(len(exp)):
            if(not isParenthesis(exp[i])):
                continue
            temp = exp[0:i] + exp[i+1:]
            if temp not in visited:
                q.append(temp)
                visited.add(temp)

exp = input()
removeInvalidPrenth(exp)
