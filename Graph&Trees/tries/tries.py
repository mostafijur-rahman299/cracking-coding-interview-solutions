
class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False
        

class Trie:
    def __init__(self):
        self.root = Node()
        
    def print_nodes(self):
        root = self.root
        
        def print_recursive(root):
            if not root:
                return
            
            for child in root.children:
                print(child)
                print_recursive(child)
                
        
        print_recursive(root)
        
    def insert_word(self, word):
        root = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not root.children[index]:
                root.children[index] = Node()
            else:
                root = root.children[index]
                
    
    def search(self, word):
        current = self.root
        
        for char in word:
            index = ord(char) - ord('a')
            if not current.children[index]:
                return
            current = current.children[index]
                
                
words = ["the", "a", "there", "their", "any"]
trie = Trie()

for word in words:
    trie.insert_word(word)

    
trie.print_nodes()

