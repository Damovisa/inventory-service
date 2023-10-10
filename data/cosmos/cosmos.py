import os
import json
from azure.cosmos import CosmosClient

url = os.getenv('COSMOS_DB_URL')
key = os.getenv('COSMOS_DB_KEY')

def getsingle(tablename, id):
    data = getall(tablename)
    for item in data:
        if item['id'] == id:
            return item
    return None

    # The below is ideal, but let's not worry about it for now
    client = CosmosClient(url, credential=key)
    database_name = 'inventory'
    database = client.get_database_client(database_name)
    container_name = tablename
    container = database.get_container_client(container_name)
    item = container.read_item(item=id, partition_key=id)
    return item

def getall(tablename):
    with open('./data/cosmos/inventory.json') as f:
        data = json.load(f)
    return data

    # probable implementation
    client = CosmosClient(url, credential=key)
    database_name = 'inventory'
    database = client.get_database_client(database_name)
    container_name = tablename
    container = database.get_container_client(container_name)
    items = container.read_all_items(max_item_count=50)
    return items
