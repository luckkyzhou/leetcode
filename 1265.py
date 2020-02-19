class ImmutableListNode:
    def printValue(self) -> None: # print the value of this node.
        pass
    def getNext(self) -> 'ImmutableListNode': # return the next node.
        pass

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        if not head: return
        self.printLinkedListInReverse(head.getNext())
        head.printValue()