class Node:
    def __init__(self, val=None):
        if val is not None:
            self.value = val
            self.next = Node()
        else:
            self.value = None
            self.next = None

    def append(self, val):
        if self.value is not None:
            self.next.append(val)
        else:
            self.value = val
            self.next = Node()

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, values):
        self.head = Node()
        try:
            self.concat(values)
        except TypeError:
            self.append(values)

    def append(self, val):
        self.head.append(val)

    def concat(self, values):
        for item in values:
            self.append(item)

    def iter(self):
        curr = self.head
        while curr.value is not None:
            yield curr.value
            curr = curr.next

    def __str__(self):
        out = '['
        for item in self.iter():
            out += str(item) + ', '
        return out[:-2] + ']'


def main():
    mylist = LinkedList([1, 2, 3])
    mylist.concat([4, 5, 6])
    print(mylist)


if __name__ == '__main__':
    main()
