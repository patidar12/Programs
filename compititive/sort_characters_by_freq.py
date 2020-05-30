'''
Given a string, sort it in decreasing order based on the frequency of characters.
Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

sooluction by leetcode :
      def frequencySort(self, s: str) -> str:
          return ''.join(c*x for x,c in Counter(s).most_common())

'''
class Solution(object):
    def merge(self,arr,start,mid,end):
        i = start
        j = mid
        temp = [None]*(end-start+1)
        k = 0
        while(i < mid and j <= end):
            if(arr[i][1] > arr[j][1]):
                temp[k] = arr[i]
                i += 1
                k += 1
            else:    
                temp[k] = arr[j]
                j += 1
                k += 1
        while(i < mid):
            temp[k] = arr[i]
            i += 1
            k += 1
        while (j <= end):
            temp[k] = arr[j]
            j += 1
            k += 1
        k = 0    
        for i in range(start,end+1):
            arr[i] = temp[k]
            k += 1    
    
    def merge_sort(self,arr,start,end):
        if(start >= end):
            return
        mid = start+(end-start)//2
        self.merge_sort(arr,start,mid)
        self.merge_sort(arr,mid+1,end)
        self.merge(arr,start,mid+1,end)    
    
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        fr_dict = {}
        for ch in s:
            if ch in fr_dict:
                fr_dict[ch] += 1
            else :
                fr_dict[ch] = 1        
        freq = []
        for char,count in fr_dict.items():
            freq.append((char, count))
        self.merge_sort(freq,0,len(freq)-1)  
        result = ''
        for i in freq:
            result += i[0]*i[1]
        return result    

s = input()
print(Solution().frequencySort(s))

