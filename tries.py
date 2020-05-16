"""
Trie: Type of Tree

Spell check: word is valid or not

One solution is hashmap of all known words
O(1) to see if the word exists,
but O(n * m) space
n: number of words
m: length of the word

Trie: decrease memory usage, improve time performance
"""

basic_trie = {
    'a': {
        'd': {
            'd': {
                'word_end': True
            },
            'word_end': False
        },
        'word_end': True
    }
}

# print(basic_trie)
# print('Is "a"   a word: {}'.format(basic_trie['a']['word_end']))
# print('Is "add" a word: {}'.format(basic_trie['a']['d']['d']['word_end']))


def is_word(word):
    current_node = basic_trie

    for char in word:
        if char not in current_node:
            return False
        current_node = current_node[char]

    return current_node['word_end']


# print(is_word('a'))    # True
# print(is_word('ad'))   # False
# print(is_word('add'))  # True

class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def exists(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.is_word


# Test simple case
word_trie = Trie()
word_trie.add('the')
# print(word_trie.exists('the'))  # True
# print(word_trie.exists('that'))  # False

valid_words = ['apple', 'bear', 'goo', 'good',
               'goodbye', 'goods', 'goodwill', 'gooses', 'zebra']
word_trie = Trie()

for valid_word in valid_words:
    word_trie.add(valid_word)

test_words = ['bear', 'goo', 'good', 'goos']

for word in test_words:
    if word_trie.exists(word):
        print('"{} is a word'.format(word))
    else:
        print('"{}" is not a word'.format(word))
