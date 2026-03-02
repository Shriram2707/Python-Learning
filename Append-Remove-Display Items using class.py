class ListManager:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f"Added: {item}")

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Deleted: {item}")
        else:
            print("Item not found!")

    def display(self):
        print("Current List:", self.items)

manager = ListManager()
manager.add("Apple")
manager.add("Banana")
manager.add("Orange")
manager.display()
manager.remove("Banana")
manager.display()