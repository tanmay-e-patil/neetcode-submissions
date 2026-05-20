class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
        

    def search(self, word: str) -> bool:
        return self.search_helper(0, word, self.root)

    def search_helper(self, idx, word, cur):
        if idx == len(word):
            return cur.word
        c = word[idx]
        if c == ".":
            for v in cur.children.values():
                res =  self.search_helper(idx + 1, word, v)
                if res:
                    return True
            return False
        elif c not in cur.children:
            return False
        else:
            return self.search_helper(idx + 1, word, cur.children[c])
        

        
