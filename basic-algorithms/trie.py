import collections
basic_trie = {
    # a and add word
    'a': {
        'd': {
            'd': {'word_end': True},
            'word_end': False},
        'word_end': True},
    # hi word
    'h': {
        'i': {'word_end': True},
        'word_end': False}}


print('Is "a"   a word: {}'.format(basic_trie['a']['word_end']))
print('Is "ad"  a word: {}'.format(basic_trie['a']['d']['word_end']))
print('Is "add" a word: {}'.format(basic_trie['a']['d']['d']['word_end']))


def is_word(word):
    """
    Look for the word in `basic_trie`
    """
    current_node = basic_trie

    for char in word:
        if char not in current_node:
            return False

        current_node = current_node[char]

    return current_node['word_end']


# Test words
test_words = ['ap', 'add']
for word in test_words:
    if is_word(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))


class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.is_word


word_list = ['apple', 'bear', 'goo', 'good',
             'goodbye', 'goods', 'goodwill', 'gooses', 'zebra']
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.add(word)

# Test words
test_words = ['bear', 'goo', 'good', 'goos']
for word in test_words:
    if word_trie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root

        for char in word:
            current_node = current_node.children[char]

            current_node.is_word = True

    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node.is_word


# Add words
valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their']
word_trie = Trie()
for valid_word in valid_words:
    word_trie.add(valid_word)

# Tests
assert word_trie.exists('the')
assert word_trie.exists('any')
assert not word_trie.exists('these')
assert not word_trie.exists('zzz')
print('All tests passed!')

