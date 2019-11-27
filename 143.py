class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def reorderList(self, head: ListNode) -> None:
        table = []
        cur = head
        while cur:
            table.append(cur.val)
            cur = cur.next
        i = 0
        j = len(table) - 1
        while i <= j:
            if i == j:
                head.val = table[i]
                head = head.next
            else:
                head.val = table[i]
                head = head.next
                head.val = table[j]
                head = head.next
            i += 1
            j -= 1

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    res = solution.reorderList(head)
    while res:
        print(res.val)
        res = res.next