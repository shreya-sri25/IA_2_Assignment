class Deque:
    def __init__(self):
        self.items = []

    def insert_front(self, item):
        self.items = [item] + self.items

    def insert_rear(self, item):
        self.items.append(item)

    def delete_front(self):
        if self.is_empty():
            return None
        item = self.items[0]
        self.items = self.items[1:]
        return item

    def delete_rear(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items


d = Deque()
d.insert_rear(10)
d.insert_rear(20)
d.insert_front(5)
d.insert_front(1)
print(d.display())
d.delete_front()
print(d.display())
d.delete_rear()
print(d.display())
