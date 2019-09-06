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
