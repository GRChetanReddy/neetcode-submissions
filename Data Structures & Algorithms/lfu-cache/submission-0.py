class DLL:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev, self.next = None, None

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dk = {}
        self.df = {}
        self.right, self.left = DLL(0, 0), DLL(0, 0)
        self.right.prev = self.left
        self.left.next = self.right

    def insert(self, node):
        nxt, prv = self.right, self.right.prev
        prv.next, nxt.prev = node, node
        node.next = nxt
        node.prev = prv

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv 

    def get(self, key: int) -> int:
        if key in self.dk:
            self.remove(self.dk[key])
            self.insert(self.dk[key])
            self.df[key]+=1
            return self.dk[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dk:
            self.remove(self.dk[key])
            self.dk[key] = DLL(key, value)
            self.df[key]+=1
            self.insert(self.dk[key])
        else:
            if len(self.dk)==self.capacity:
                m = min(self.df.values())
                h = self.left.next
                while self.df[h.key]!=m:
                    h = h.next
                self.remove(self.dk[h.key])
                del self.dk[h.key]
                del self.df[h.key]
            self.df[key] = 1
            self.dk[key] = DLL(key, value)
            self.insert(self.dk[key])


        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)