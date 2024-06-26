'''
AlphaCode-Question
Send Feedback
Alice and Bob need to send secret messages to each other and are discussing ways to encode their messages:
Alice: “Let’s just use a very simple code: We’ll assign ‘A’ the code word 1, ‘B’ will be 2, and so on down to ‘Z’ being assigned 26.”

Bob: “That’s a stupid code, Alice. Suppose I send you the word ‘BEAN’ encoded as 25114. You could decode that in many different ways!”

Alice: “Sure you could, but what words would you get? Other than ‘BEAN’, you’d get ‘BEAAD’, ‘YAAD’, ‘YAN’, ‘YKD’ and ‘BEKD’. I think you would be able to figure out the correct decoding. And why would you send me the word ‘BEAN’ anyway?”

Bob: “OK, maybe that’s a bad example, but I bet you that if you got a string of length 5000 there would be tons of different decodings and with that many you would find at least two different ones that would make sense.”

Alice: “How many different decodings?”

Bob: “Jillions!”
For some reason, Alice is still unconvinced by Bob’s argument, so she requires a program that will determine how many decodings there can be for a given string using her code.
Input
Input will consist of multiple input sets. Each set will consist of a single line of at most 5000 digits representing a valid encryption (for example, no line will begin with a 0). There will be no spaces between the digits. An input line of ‘0’ will terminate the input and should not be processed.
Output
For each input set, output the number of possible decodings for the input string. Print your answer taking modulo "10^9+7"
Sample Input:
25114
1111111111
3333333333
0
Sample Output:
6
89
1

'''

def numOfDecoding(code):
    n = len(code)
    dp = [0]*n
    dp[0] = 1
    mod = 1000000007
    for i in range(1,n):
        x = int(code[i-1:i+1])
        if(code[i] != '0'):
            dp[i] = dp[i-1]
        if(x >= 10 and x <= 26 and i > 1 ):
            dp[i] += dp[i-2]
        elif(x >= 10 and x <= 26):
            dp[i] += 1
        dp[i] = dp[i]%mod
    return dp[n-1]

def numOfdecoding(code,n,dp):
    if(n == 0):
        return 1
    if(n == 1):
        return 1
    mod = 1000000007
    if(dp[n] != -1):
        return dp[n]
    x = int(code[n-2:n])
    output = 0
    if(code[n-1] != '0'):
        output = numOfdecoding(code,n-1,dp)
    if(x >= 10 and x <= 26):
        output += numOfdecoding(code,n-2,dp)
    dp[n] = output%mod
    return output%mod

def alphaCode(s,n,dp):
    if(n == 0 or n == 1):
        return 1
    mod = 1000000007
    count = 0
    if(dp[n] != -1):
        return dp[n]
    if(s[n-1] > "0"):
        count = alphaCode(s,n-1,dp)
    if(s[n-2] == '1' or (s[n-2] == '2' and s[n-1] < '7')):
        count += alphaCode(s,n-2,dp)
    dp[n] = count%mod
    return count%mod

while(True):
    code = input().strip()
    if(code == '0'):
        break
    print(numOfDecoding(code))
    #n = len(code)
    #dp = [-1]*(n+1)
    #print(numOfdecoding(code,n,dp))
    #print(alphaCode(code,n,dp))
