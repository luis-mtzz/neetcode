class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)    
        self.head.next = self.tail
        self.tail.prev = self.head    

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        
        self.remove_node(self.mp[key])
        self.add_node(self.mp[key])
        return self.mp[key].val
    
    def remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_node(self, node: Node):
        prev_node = self.tail.prev
        node.prev = prev_node
        node.next = self.tail
        prev_node.next = node
        self.tail.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.remove_node(self.mp[key]) 
        new_node = Node(key, value)
        self.mp[key] = new_node
        if len(self.mp) > self.capacity:
            del self.mp[self.head.next.key]
            self.remove_node(self.head.next)
        self.add_node(new_node)       
