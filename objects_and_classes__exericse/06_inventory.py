class Inventory:
    # __capacity
    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        self.items = []

    def add_item(self, item: str):
        if self.__capacity > len(self.items):
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):

        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity - len(self.items)}"
