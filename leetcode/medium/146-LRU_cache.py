"""
    Leetcode # 146
"""


from typing import Dict, List

class DoublyLinkedNode:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.size = 0

        self.capacity = capacity

        self.head = DoublyLinkedNode(-1, -1)
        self.tail = DoublyLinkedNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = dict()

    def __move_node_to_head(self, node: DoublyLinkedNode) -> None:
        pred = self.head
        succ = self.head.next
        succ.prev = node
        pred.next = node
        node.prev = pred
        node.next = succ

    def __remove_node_links(self, node: DoublyLinkedNode) -> None:
        pred = node.prev
        succ = node.next
        succ.prev = pred
        pred.next = succ
        node.prev = None
        node.next = None

    def __remove_tail(self) -> int:
        to_delete = self.tail.prev
        k = to_delete.key
        pred = to_delete.prev
        self.tail.prev = pred
        pred.next = self.tail
        del to_delete
        return k

    def get(self, key: int) -> int:
        if key not in self.cache: return -1

        node = self.cache[key]

        # make frequently accessed keys to head
        self.__remove_node_links(node)
        self.__move_node_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and self.size == self.capacity:
            self.size -= 1
            tail_key = self.__remove_tail()
            del self.cache[tail_key]

        if key not in self.cache:
            self.size += 1
        else:
            old_node = self.cache[key]
            self.__remove_node_links(old_node)
            del self.cache[key]

        node = DoublyLinkedNode(key, value)
        self.cache[key] = node
        self.__move_node_to_head(node)



if __name__ == "__main__":

    lru = LRUCache(3)

    assert lru.get(1) == -1

    lru.put(1, "foo")
    lru.put(2, "bar")
    lru.put(3, "baz")

    assert lru.get(1) == "foo"

    lru.get(1)
    lru.get(1)
    lru.get(1)
    lru.get(3)

    lru.put(4, "qux")

    assert lru.get(4) == "qux"
    assert lru.get(2) == -1     # 2 is evicted as it was least accessed (fetched)

    lru.get(4)
    lru.get(4)

    lru.put(5, "quux")

    assert lru.get(5) == "quux"

