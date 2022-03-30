from Node import Node

class LinkedLIst:

    def __init__(self):
        self.head = self.last = None
        self.size = 0

    def empty(self):
        return self.size == 0

    def len(self):
        return self.size

    def firstElement(self):
        if not self.empty():
            return self.head.dado

    def lastElement(self):
        if not self.empty():
            return self.last.dado

    def appendIndex(self, index, dado):
        if not self.empty():
            pointer = previous = self.head
            for i in range(2, index+1):
                if index == i:
                    previous.next = Node(dado, pointer)
                    self.size += 1
                    if pointer.next is None:
                        self.last = pointer
                    break
                previous = pointer
                pointer = pointer.next
            return pointer

    def removeIndex(self, index):
        if not self.empty():
            pointer = previous = self.head
            for i in range(2, index+1):
                if index == i:
                    previous.next = pointer.next
                    self.size -= 1
                    break
                previous = pointer
                pointer = pointer.next
            previous = self.head = pointer.next

    def removeValues(self, value):
        if not self.empty():
            pointer = previous = self.head
            for i in range(2, self.len()+1):
                if pointer.dado == value:
                    previous.next = pointer.next
                    self.size -= 1
                previous = pointer
                pointer = pointer.next
            if pointer.dado == value:
                previous = self.head = None

    def appendValue(self, value, value1):
        if not self.empty():
            pointer = previous = self.head
            for i in range(2, self.len()+1):
                if pointer.dado == value:
                    aux = pointer.next
                    pointer.next = Node(value1, aux)
                    self.size += 1
                previous = pointer
                pointer = pointer.next
            if pointer.dado == value:
                pointer.next = Node(value1, None)

    def sumValues(self):
        if not self.empty():
            pointer = self.head
            sumValue = pointer.dado
            for i in range(2, self.len()+1):
                if pointer.next == None:
                    return sumValue
                sumValue += pointer.dado
                pointer = pointer.next
            return sumValue

    def modifierIndex(self, index, value):
        if not self.empty():
            pointer = self.head
            for i in range(2, index+1):
                if i == index:
                    pointer.dado = value
            pointer.dado = value

    def consultValue(self, value):
        if not self.empty():
            pointer = previous = self.head
            for i in range(2, self.len()+1):
                if pointer.dado == value:
                    return previous.dado
                previous = pointer
                pointer = pointer.next
            return None

    def pairsValues(self):
        if not self.empty():
            pointer = previous = self.head
            count = 0
            if pointer % 2 == 0:
                count = 1
            for i in range(2, self.len()+1):
                if pointer % 2 == 0:
                    count += 1
            return count
