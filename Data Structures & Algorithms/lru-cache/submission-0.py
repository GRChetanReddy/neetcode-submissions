class DLL:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.right, self.left = DLL(0, 0), DLL(0, 0)
        self.right.prev = self.left
        self.left.next = self.right

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv

    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next, nxt.prev = node, node
        node.prev = prv
        node.next = nxt
        

    def get(self, key: int) -> int:
        if key in self.d:
            self.remove(self.d[key])
            self.insert(self.d[key])
            return self.d[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
            self.d[key] = DLL(key, value)
            self.insert(self.d[key])
        else:
            if len(self.d)==self.capacity:
                self.d.pop(self.left.next.key)
                self.remove(self.left.next)
            self.d[key] = DLL(key, value)
            self.insert(self.d[key])
        
