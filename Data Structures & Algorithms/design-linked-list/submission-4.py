class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0        

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        return self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        return self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if (index > self.size or index < 0):
            return
        else:
            cur = self.head
            node = ListNode(val)
            for _ in range(index):
                cur = cur.next


            node.next = cur.next
            cur.next = node
            
            self.size+=1
        

    def deleteAtIndex(self, index: int) -> None:
        if (index >= self.size or index < 0):
            return
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            cur.next = cur.next.next
            self.size-=1
