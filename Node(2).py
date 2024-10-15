class Element:
    def __init__(self, value):
        self.value = value
        self.subsequent = None

class Chain:
    def __init__(self):
        self.start = None

    def prepend(self, value):
        new_element = Element(value)
        new_element.subsequent = self.start
        self.start = new_element

    def show_contents(self):
        current_element = self.start
        while current_element:
            print(current_element.value)
            current_element = current_element.subsequent

# Example usage
chain = Chain()
chain.prepend(1)
chain.prepend(2)
chain.show_contents()