'''
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Solution(itretive):

class Solution:
    
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[-1 for i in range(l2+1)] for j in range(l1+1)]
        for i in range(l2+1):
            dp[0][i] = i
        for i in range(l1+1):
            dp[i][0] = i
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if(word1[i-1] == word2[j-1]):
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
        return dp[l1][l2]    


'''

# recursive
class Solution:
    def getDistance(self,word1,word2,len1,len2,dp):
        if(len1 == 0):
            return len2
        if(len2 == 0):
            return len1
        if(dp[len1-1][len2-1] != -1):
            return dp[len1-1][len2-1]
        if(word1[len1-1] == word2[len2-1]):
            result = self.getDistance(word1,word2,len1-1,len2-1,dp)
            dp[len1-1][len2-1] = result
            return result
        replace = self.getDistance(word1,word2,len1-1,len2-1,dp)
        delete = self.getDistance(word1,word2,len1-1,len2,dp)
        insert = self.getDistance(word1,word2,len1,len2-1,dp)
        result =  1+min(replace,min(delete,insert))
        dp[len1-1][len2-1] = result
        return result

    def minDistance(self, word1: str, word2: str) -> int:

        dp = [[-1 for i in range(len(word2))] for j in range(len(word1))]
        return self.getDistance(word1,word2,len(word1),len(word2),dp)
