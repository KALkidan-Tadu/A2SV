class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class MyLinkedList:
    head = Node()
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr != None:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.head.next = None
        else:
            newNode.next = self.head
            self.head = newNode

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            return self.addAtHead(val)
        newNode = Node(val)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = newNode
        newNode.next = None

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            return self.addAtHead(val)
        current = self.head
        newNode = Node(val)

        i = 0
        while current:
            if i == index - 1:
                if current.next == None:
                    current.next = newNode
                    newNode.next = None
                else:
                    after = current.next
                    current.next = newNode
                    newNode.next = after
                return 
            current = current.next
            i += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            current = self.head.next
            self.head = current
            return 
        current = self.head
        i = 0
        while current.next:
            if i == index-1:
                current.next = current.next.next
                return
            i += 1
            current = current.next
        return 
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
