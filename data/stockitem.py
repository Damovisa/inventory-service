from dataclasses import dataclass

@dataclass
class StockItem:
    id: int
    name: str
    remaining_stock: int

    def __init__(self, id, name, remaining_stock):
        self.id = id
        self.name = name
        self.remaining_stock = remaining_stock

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'remaining_stock': self.remaining_stock
        }