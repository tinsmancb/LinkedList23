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
        self.len = 0
        try:
            self.concat(values)
        except TypeError:
            self.append(values)

    def append(self, val):
        self.len += 1
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

    def __len__(self):
        return self.len

    def __getitem__(self, item):
        if item in range(-self.len, self.len):
            curr = self.head
            item %= self.len
            for _ in range(item):
                curr = curr.next
            return curr.value
        else:
            raise IndexError(f'Index {item} is out of range for list of length {self.len}.')

    def __setitem__(self, key, value):
        if key in range(-self.len, self.len):
            curr = self.head
            key %= self.len
            for _ in range(key):
                curr = curr.next
            curr.value = value
        else:
            raise IndexError(f'Index {key} is out of range for list of length {self.len}.')


def main():
    mylist1 = LinkedList([1, 2, 3])
    mylist2 = LinkedList([4, 5, 6])
    mylist = LinkedList(mylist1)
    mylist.concat(mylist2)
    print(mylist)
    print(mylist[5])
    #mylist[0] = 42
    #print(mylist)



if __name__ == '__main__':
    main()
