'''
Stream of Characters (August Day 24)

Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
 

Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist
 

Note:

1 <= words.length <= 2000
1 <= words[i].length <= 2000
Words will only consist of lowercase English letters.
Queries will only consist of lowercase English letters.
The number of queries is at most 40000.

>Hide Hint #1

Put the words into a trie, and manage a set of pointers within that trie.

Input:
["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query"]
[[["cd","f","kl"]],["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"],["j"],["k"],["l"]]   

Output:
[null,false,false,false,true,false,true,false,false,false,false,false,true]

'''
class TrieNode: 
	def __init__(self): 
		self.children = [None]*26
		self.isEndOfWord = False
class Trie: 
	def __init__(self): 
		self.root = self.getNode()
        
	def getNode(self):
		return TrieNode()

	def _charToIndex(self,ch):
		return ord(ch)-ord('a')

	def insert(self,key):
		pCrawl = self.root
		length = len(key)
		for level in range(length):
			index = self._charToIndex(key[level])
			if not pCrawl.children[index]:
				pCrawl.children[index] = self.getNode()
			pCrawl = pCrawl.children[index]
		pCrawl.isEndOfWord = True

class StreamChecker:

    def __init__(self, words: List[str]):
        t = Trie()
        for word in words:
            t.insert(word)
        self.trie = t
        self.root = t.root
        

    def query(self, letter: str) -> bool:
        index = self.trie._charToIndex(letter)
        if(self.root.children[index] and self.root.children[index].isEndOfWord == True):
            self.root = self.root.children[index]
            return True
        elif(self.root.children[index]):
            self.root = self.root.children[index]
        else:
            self.root = self.trie.root    
        return False    


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
