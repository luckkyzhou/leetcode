class DoubleLinkedList(object):
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.head = DoubleLinkedList()
        self.tail = DoubleLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.addToHead(node)
            return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache:
            node = DoubleLinkedList(key, value)
            self.cache[key] = value
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                removed_node = self.removeTail()
                self.cache.pop(removed_node.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.addToHead(node)

    def addToHead(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeTail(self):
        node = self.tail.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        return node