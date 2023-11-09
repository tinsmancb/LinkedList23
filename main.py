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
        if self.value is not None:
            out = str(self.value)
            if self.next.value is not None:
                out += ','
                out += str(self.next)
            return out
        else:
            return ''


def main():
    mylist = Node()
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
    print(mylist)


if __name__ == '__main__':
    main()
