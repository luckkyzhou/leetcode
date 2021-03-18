class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def reverseList(self, head, tail):
        """
        :param head: ListNode
        :param tail: ListNode
        :return: ListNode
        """
        cur = head
        prev = None

        while cur != tail:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        res = ListNode(0)
        res.next = head
        cur = res

        while head:
            tail = head
            for i in range(k):
                if tail != None:
                    tail = tail.next
                else:
                    return res.next
            # 设置头节点，翻转完之后方便链接
            start = cur.next
            prev = self.reverseList(head, tail)
            # 向前链接
            cur.next = prev
            # 向后链接
            start.next = tail
            # 重置
            cur = start
            head = tail
        return res.next
