class ListNode:
  def __init__(self, val=-1, next=None):
    self.val = val
    self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = ListNode()
        h = self.front
        for _ in range(1, k):
            h.next = ListNode()
            h = h.next
        h.next = self.front
        self.rear = self.front
        self.c = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front.val = value
            self.rear = self.front
        else:
            self.rear = self.rear.next
            self.rear.val = value
        self.c+=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front.val = -1
        self.front = self.front.next 
        self.c-=1
        return True

    def Front(self) -> int:
        return self.front.val if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.rear.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        if self.c==0:
            return True
        return False

    def isFull(self) -> bool:
        if self.c==self.k:
            return True
        return False 


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()