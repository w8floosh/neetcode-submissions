type LRUCache struct {
    data     map[int]*LRUCacheNode
    capacity int
    head     *LRUCacheNode
    tail     *LRUCacheNode
}

type LRUCacheNode struct {
    key   int
    value int
    prev  *LRUCacheNode
    next  *LRUCacheNode
}
func Constructor(capacity int) LRUCache {
    return LRUCache{
        data:     make(map[int]*LRUCacheNode, capacity),
        capacity: capacity,
    }
}

func (this *LRUCache) Get(key int) int {
	if node, ok := this.data[key]; ok {
		this.mvHead(node)
		return node.value
	}
	return -1
}

func (this *LRUCache) Put(key int, value int) {
    if node, ok := this.data[key]; ok {
		node.value = value
		this.mvHead(node)
		return
	}

	// If cache is full, remove LRU (tail)
	if len(this.data) >= this.capacity && this.tail != nil {
		delete(this.data, this.tail.key)
		this.rm(this.tail)
	}

	newNode := &LRUCacheNode{
		key: key,
		value: value,
	}
	this.prepend(newNode)
	this.data[key] = newNode
}

func (this *LRUCache) mvHead(node *LRUCacheNode) {
	this.rm(node)
	this.prepend(node)
}

func (this *LRUCache) rm(node *LRUCacheNode) {
	// X <-> Y <-> Z
	// X <------- Z, X ------> Z
	// X <-> Z

	// Left link
	if node.prev != nil {
		node.prev.next = node.next
	} else {
		this.head = node.next
	}

	// Right link
	if node.next != nil {
		node.next.prev = node.prev
	} else {
		this.tail = node.prev
	}
}

func (this *LRUCache) prepend(node *LRUCacheNode) {
	node.prev = nil
	node.next = this.head

	if this.head != nil {
		this.head.prev = node
	}

	this.head = node

	if this.tail == nil {
		this.tail = node
	}
}