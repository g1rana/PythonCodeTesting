class TrieNode(object):
    def __init__(self):
        self.member = {}
        self.isWord = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.member:
                cur.member[c] = TrieNode()
            cur = cur.member[c]
        cur.isWord =True

    def findWord(self,word):
        cur = self.root
        for c in word:
            if c not in cur.member:
                return False
            cur = cur.member[c]

        return cur.isWord

    def findPrefixMatchWord(self,prefix):
        cur = self.root

        for c in prefix:
            if c not in cur.member:
                return []
            cur = cur.member[c]

    #prefix match now find all words
        ret = []
        path = list(prefix)
        self.collection_word(cur,path,ret)
        return ret



    def collection_word(self,node, path, ret):
        if node.isWord:
            ret.append(" ".join(path))
        #backtracking
        for c,member in node.member.items():
            path.append(c)
            self.collection_word(member,path,ret)
            path.pop()


if __name__ == "__main__":

    T = Trie()
    s1 = "ABE"
    T.addWord(s1)
    # print(T.findPrefixMatchWord(s1))
    s2 = "AB"
    T.addWord(s2)
    s3 = "ABD"
    T.addWord(s3)
    s3 = "ABC"
    T.addWord(s3)
    print(T.findPrefixMatchWord("AB"))
