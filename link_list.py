class LinkList:
    def __init__(self):
        self.__head = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def add(self, value):
        if self.__head is None:
            self.__head = LinkList.Node(value)
        else:
            p = self.__head
            while p.next is not None:
                p = p.next
            p.next = LinkList.Node(value)

    def __str__(self):
        out = ""
        if self.__head is None:
            return out
        else:
            p  = self.__head
            while p.next is not None:
                out = out + "%s -> " % p.value
                p = p.next
            out += str(p.value)
            return out

ll = LinkList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)

print(ll)