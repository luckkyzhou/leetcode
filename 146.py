# -*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.hashmap = {}
        # 新建头指针和尾指针
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表为head<->tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # 定义将链表中某个节点移到末尾
    def moveNodetoTail(self, key):
        node = self.hashmap[key]
        # 将node置于prev和next中间
        node.prev.next = node.next
        node.next.prev = node.prev
        # 将node插入到尾指针前
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    # 获取数据
    def get(self, key:int) -> int:
        # 如果在链表中，把它移到队尾变为最新访问的
        if key in self.hashmap:
            self.moveNodetoTail(key)
        # 找不到key时返回-1
        res = self.hashmap.get(key,-1)
        if res == -1:
            return res
        else:
            return res.value

    # 写入数据
    def put(self, key:int, value:int) -> None:
        # 如果在链表中，不需要加入新节点。但要更新节点值，并将其移到队尾。
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.moveNodetoTail(key)
        else:
            if len(self.hashmap) ==self.capacity:
                # 去掉最久没有被访问的节点，即head节点后的第一个节点。pop方法去除dict中指定key
                self.hashmap.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            new = ListNode(key, value)
        # 如果key不在链表中，就插入到队尾前
        new = ListNode(key, value)
        self.hashmap[key] = new
        new.prev = self.tail.prev
        new.next = self.tail
        self.tail.prev.next = new
        self.tail.prev = new

