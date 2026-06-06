type WordDictionary struct {
    trie *TrieNode
}

type TrieNode struct {
	key byte
	children map[byte]*TrieNode
	eow bool
}

func Constructor() WordDictionary {
    return WordDictionary{
		trie: &TrieNode{
			children: make(map[byte]*TrieNode),
			eow: false,
		},
	}
}

func (this *WordDictionary) AddWord(word string)  {
    if len(word) == 0 {
		return
	}

	addWordRecursive(word, this.trie)
}

func addWordRecursive(word string, cur *TrieNode){
	if len(word) == 0 {
		cur.eow = true
		return
	}

	next := cur.children[word[0]]

	if next == nil {
		next = &TrieNode{
			key: word[0],
			children: make(map[byte]*TrieNode, 0),
		}
		cur.children[word[0]] = next
	}
	addWordRecursive(word[1:], next)
}

func (this *WordDictionary) Search(word string) bool {
    if len(word) == 0 {
		return true
	}

	return searchRecursive(word, this.trie)
}

func searchRecursive(word string, cur *TrieNode) bool {
	if len(word) == 0 {
		return cur.eow
	}

	query := word[0]
	for key, node := range cur.children {
		if query == '.' || key == query {
			if searchRecursive(word[1:], node) {
				return true
			}
		}
	}

	return false
}
