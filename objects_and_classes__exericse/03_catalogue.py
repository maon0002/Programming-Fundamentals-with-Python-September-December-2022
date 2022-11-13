class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        # return [x for x in self.products if x.startswith(first_letter)]
        return [item for item in self.products if item.startswith(first_letter)]

    def __repr__(self):
        first_line = f"Items in the {self.name} catalogue:\n"
        first_line += '\n'.join(sorted(self.products))
        return first_line
