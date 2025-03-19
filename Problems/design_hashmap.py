class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class DesignHashmap:
    def __init__(self):
        self.hash_map = [ListNode() for i in range(1000)]

    def hash(self, key):
        return key % len(self.hash_map)

    def put(self, key: int, value: int) -> None:
        cur = self.hash_map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.hash_map[self.hash(key)]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.hash_map[self.hash(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


class ListNodeForSet:
    def __init__(self, key=-1, next=None):
        self.key = key
        self.next = next

import random

class DesignHashSet:
    def __init__(self):
        self.hash_set = [ListNodeForSet() for i in range(10000)]
        self.size = 0

    def hash(self, key):
        return key % len(self.hash_set)

    def add(self, key: int) -> None:
        cur = self.hash_set[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNodeForSet(key)
        self.size += 1

    def remove(self, key: int) -> None:
        cur = self.hash_set[self.hash(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                self.size -= 1
                print(f"Removed {key} || size: {self.size}")
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.hash_set[self.hash(key)]
        while cur:
            if cur.key == key:
                return True
            cur = cur.next
        return False
    
    def getRandom(self):
        random_num = random.randint(0, self.size)
        print("random_num: ", random_num)
        cur = self.hash_set[self.hash(random_num)]
        while cur:
            if cur.key == random_num:
                print("Found")
                return cur.key
            cur = cur.next
        print("Not found")
        return -1
