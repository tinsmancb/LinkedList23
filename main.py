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
        self.curr = self.head
        try:
            self.concat(values)
        except TypeError:
            self.append(values)

    def append(self, val):
        self.head.append(val)

    def concat(self, values):
        for item in values:
            self.append(item)

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr.value is not None:
            out = self.curr.value
            self.curr = self.curr.next
            return out
        else:
            self.curr = self.head
            raise StopIteration

    def __str__(self):
        out = '['
        for item in self:
            out += str(item) + ', '
        return out[:-2] + ']'


def main():
    mylist1 = LinkedList([1, 2, 3])
    mylist2 = LinkedList([4, 5, 6])
    mylist = LinkedList(mylist1)
    mylist.concat(mylist2)
    print(mylist)


if __name__ == '__main__':
    main()
