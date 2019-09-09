# -*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self,capacity:int):
        self.capacity = capacity
        self.hashmap = {}
        # 新建头指针和尾指针
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表为head<->tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # 定义将链表中某个节点移到末尾
    def moveNodetoTail(self,key):
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
    def get(self,key:int):
        # 如果已经在链表中，把它移到队尾变为最新访问的
        if key in self.hashmap:
            self.moveNodetoTail(key)
        # 找不到key时返回-1
        res = self.hashmap.get(key,-1)
        if res == -1:
            return res
        
