'''
Design a data structure that supports adding new words and finding if a string matches 
any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or 
false otherwise. word may contain dots '.' where dots can be matched with any letter.
'''
#Using Trie base datastruture to build this solution 
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict()
        self.endWord = False


class WordDictionary:
    def __init__(self):
        self.root=TrieNode()
    
    def addWord(self,word:str):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur =cur.children[w]
        cur.endWord = True
    
    def search(self,word):
        cur = self.root
        return self._searcFrom(cur,word)
    
    def _searcFrom(self,node:TrieNode,word:str)->bool:
        if not word:
            return node.endWord
        
        char = word[0]
        if char == '.':
            for child_node in node.children.values():
                    if self._searcFrom(child_node,word[1:]):
                        return True
        else:
            if char in node.children:
                return self._searcFrom(node.children[char],word[1:])
        return False
    


wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad")) # return False
print(wordDictionary.search("bad")) # return True
print(wordDictionary.search(".ad")) # return True
print(wordDictionary.search(".b.d")) #
print(wordDictionary.search("bad"))