class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.elements = [None] * capacity
        self.head = 0
        self.tail = 0

    def add(self, item):
        if self.tail == self.capacity:
            print("Queue is at maximum capacity")
        else:
            self.elements[self.tail] = item
            self.tail += 1

    def remove(self):
        if self.head == self.tail:
            print("Queue is empty")
        else:
            item = self.elements[self.head]
            self.head += 1
            return item

# Example usage
capacity = int(input("Enter the size of the queue: "))
queue = Queue(capacity)
queue.add(1)
queue.add(2)
print(queue.remove())