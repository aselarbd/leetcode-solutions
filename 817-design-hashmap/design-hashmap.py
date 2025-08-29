class MyHashMap:

    def __init__(self):
        self.keys =[]
        self.vals = []
        

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            idx = self.keys.index(key)
            self.vals[idx] = value
        else:
            self.keys.append(key)
            self.vals.append(value)
        

    def get(self, key: int) -> int:
        if key in self.keys:
            return self.vals[self.keys.index(key)]
        return -1

    def remove(self, key: int) -> None:
        if key in self.keys:
            idx = self.keys.index(key)
            del self.keys[idx]
            del self.vals[idx]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)