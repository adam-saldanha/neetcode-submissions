class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._remove(node)
        self._insert(node)
        return node.value

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


    def _insert(self, node):
        node.prev = self.left
        node.next  = self.left.next
        self.left.next.prev = node
        self.left.next = node
        
    

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            self._remove(node)
            node.value = value
        else:
            node = Node(key, value)
            self.nodes[key] = node
        self._insert(node)
        if len(self.nodes) > self.capacity:
            least_recent = self.right.prev
            self._remove(least_recent)
            del self.nodes[least_recent.key]
        
