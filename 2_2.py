# -*- coding:utf-8 -*-

# 定义链表
class listNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def addTwoNumbers(l1:listNode,l2:listNode):
    node = listNode(0)
    cur = node
    carry = 0
    while(l1 or l2):
        if l1: x = l1.val
        else: x = 0
        if l2: y = l2.val
        else: y = 0
        sum = x + y + carry
        carry = sum // 10
        node.next = listNode(sum % 10)
        node = node.next
        if l1 != None: l1 = l1.next
        if l2 != None: l2 = l2.next
    if carry > 0:
        node.next = listNode(1)
    return cur.next

if __name__ == '__main__':
    node1 = listNode(2)
    head1 = node1
    node1.next = listNode(4)
    node1 = node1.next
    node1.next = listNode(3)

    node2 = listNode(5)
    head2 = node2
    node2.next = listNode(6)
    node2 = node2.next
    node2.next = listNode(4)

    node = addTwoNumbers(head1,head2)
    while node != None:
        print(node.val)
        node = node.next
