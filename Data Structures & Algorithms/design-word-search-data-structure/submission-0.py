class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        def dfs(i, root):
            curr = root
            for j in range(i, len(word)):
                if word[j] == '.':
                    for child in curr.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                
                else:
                    if word[j] not in curr.children:
                        return False
                    curr = curr.children[word[j]]
            return curr.is_end
        return dfs(0, self.root)

        
