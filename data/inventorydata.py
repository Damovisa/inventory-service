import json
from .stockitem import StockItem
from .cosmos import cosmos

def get_inventory_data() -> list[StockItem]:
    data = cosmos.getall('inventory')
    stock_items = [StockItem(**item) for item in data]
    return stock_items

def get_inventory_item(item_id) -> StockItem:
    data = get_inventory_data()
    for item in data:
        if item.id == item_id:
            return item
    return None