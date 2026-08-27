class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    """
    - we can use a hash map of the key and the nodes they are pointing too
    - search and put are easy, now its the recently used part
        - ==A key is considered used if a `get` or a `put` operation is called on it.==
        - we can use the order of the doubly linked list
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.right = Node(0, 0)  # the right most node is just a placeholder
        self.left = Node(0, 0)  # the left most node is just a placeholder
        # meaning any new nodes go to the left of the right most node and vice versa
        # think of them like pointers at the end where we can use them
        # to access the ends of the linked list
        self.left.next = self.right
        self.right.prev = self.left

    # for inserting to the very right (most recently used)
    def insert_to_right(self, node):
        # finding the left and right of where
        # we want to insert the node
        prev, nxt = self.right.prev, self.right
        # making the connection
        self.right.prev = node
        node.next = self.right
        prev.next = node
        node.prev = prev

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert_to_right(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        new_node = Node(key, value)
        self.insert_to_right(new_node)
        self.cache[key] = new_node

        if self.cap < len(self.cache):
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            