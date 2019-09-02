# -*- coding:utf-8 -*-

class ListNode(object):
    def __init__(self):
        self.val = None
        self.next = None

class ListNode_handle():
    def __init__(self):
        self.cur_node = None

    def printListNode(self,node):
        while node:
            print('\nnode:', node, 'value:', node.val, 'next:', node.next)
            node = node.next

def addTwoNumbers(self, l1:ListNode,l2:ListNode):
    re = ListNode(0)
    r = re
    carry = 0
    while (l1 or l2):
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        s = carry+x+y
        carry=s//10
        r.next=ListNode(s%10)
        r=r.next
        if(l1!=None):l1=l1.next
        if(l2!=None):l2=l2.next
    if(carry>0):
        r.next=ListNode(1)
    return re.next