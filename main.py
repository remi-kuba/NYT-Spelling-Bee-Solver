class Trie():
    def __init__(self):
        # No need value, but know if it's a valid word
        self.end = False 
        self.children = {}
    
    def get_node(self, key):
        return self if not key else self.children.setdefault(key[0],Trie()).get_node(key[1:])

    def setitem(self,key):
        self.get_node(key).end = True 
    
    def __getitem__(self,key):
        return self.get_node(key)
    

def create_trie(file):
    dictionary = open(file,"r").read().splitlines()
    word_trie = Trie()
    # for char in dictionary[0]:
    #     print(f"'{char}'")
    for word in dictionary:
        word_trie.setitem(word)
    return word_trie


def spelling_bee_solver(letters, trie, required):
    letters.append(required)
    def recurse(inside_trie, part_word = ""):
        if not trie:
            return
        if inside_trie.end:
            valid.append(part_word)
        for l in letters:
            if l in inside_trie.children:
                recurse(inside_trie[l],part_word+l)
    
    valid = []
    recurse(trie)
    res = [i for i in valid if len(i) > 3 and required in i]
    return sorted(res, key = lambda w : (len(w),w))

