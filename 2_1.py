# -*- coding:utf-8 -*-

class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def addTwoNumbers(l1:ListNode,l2:ListNode):
    node = ListNode(0)
    cur = node
    carry = 0
    while (l1 or l2):
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        s = carry + x + y
        carry = s // 10
        node.next = ListNode(s % 10)
        node = node.next
        if(l1 != None):l1 = l1.next
        if(l2 != None):l2 = l2.next
    if(carry>0):
        node.next = ListNode(1)
    return cur.next

if __name__ == '__main__':
    node1 = ListNode(2)
    head1 = node1
    node1.next = ListNode(4)
    node1 = node1.next
    node1.next = ListNode(3)

    node2 = ListNode(5)
    head2 = node2
    node2.next = ListNode(6)
    node2 = node2.next
    node2.next = ListNode(4)

    node = addTwoNumbers(head1,head2)

    while node != None:
        print(node.val)
        node = node.next

