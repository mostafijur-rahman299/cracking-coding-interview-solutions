
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
                return False
            current = current.children[index]
                
        return True
    
    
    def word_break(self, string):
        if len(string) == 0:
            return  # Base case for string length 1

        for index in range(1, len(string) + 1):
            first = string[0:index]
            second = string[index:len(string)]
            if self.search(first) and self.word_break(second):  # Recursive call on the instance
                return True
            print(second)

        return False  # Return a value to indicate completion
    
    
words = ["i", "like", "sam", "samsung", "mobile", "ice"]

trie = Trie()

for word in words:
    trie.insert_word(word)

    
# trie.print_nodes()



trie.word_break("ilikesamsung")
