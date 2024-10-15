class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.elements = [None] * capacity
        self.current_index = -1

    def add_element(self, value):
        if self.current_index == self.capacity - 1:
            print("Stack is full")
        else:
            self.current_index += 1
            self.elements[self.current_index] = value

    def remove_element(self):
        if self.current_index == -1:
            print("Stack is empty")
        else:
            value = self.elements[self.current_index]
            self.current_index -= 1
            return value

# Example usage
capacity = int(input("Enter the capacity of the stack: "))
array_stack = ArrayStack(capacity)
array_stack.add_element(1)
array_stack.add_element(2)
print(array_stack.remove_element())