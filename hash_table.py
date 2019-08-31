class HashMap:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__buckets = [None] * capacity

    def put(self, key, val):
        bucket = hash(key) % self.__capacity
        if self.__buckets[bucket] is None:
            ll = LinkList()
            ll.add((key, val))
            self.__buckets[bucket] = ll
        else:
            self.__buckets[bucket].add((key, val))

    def get(self, key):
        bucket = hash(key) % self.__capacity
        if self.__buckets[bucket] is None:
            return None
        else:
            return self.__buckets[bucket].find(key)


class LinkList:
    class Node:
        def __init__(self, v):
            self.value = v
            self.next = None

    def __init__(self):
        self.__head = None

    def add(self, v):
        if self.__head is None:
            self.__head = LinkList.Node(v)
        else:
            p = self.__head
            while p.next is not None and p.value[0] != v[0]:
                p = p.next
            if p.value[0] == v[0]:
                p.value = v
            else:
                p.next = LinkList.Node(v)

    def find(self, key):
        p = self.__head
        while p is not None:
            if p.value[0] == key:
                return p.value[1]
            p = p.next
        return None


h = HashMap(10)
h.put(r'swapnil', 1)
h.put(r'himan', 2)
h.put(r'abhi', 3)

assert(h.get(r'swapnil') == 1)
assert(h.get(r'himan') == 2)
assert(h.get(r'abhi') == 3)
assert(h.get(r'aaa') is None)
assert(h.get(r'bbb') is None)

h.put(r'swapnil', 11)
assert(h.get(r'swapnil') == 11)
h.put(r'abhi', 12)
assert(h.get(r'abhi') == 12)