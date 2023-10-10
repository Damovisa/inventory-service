from flask import Flask, request, jsonify
import json
import os
from data import inventorydata
from utils import appsetup

app = Flask(__name__)
app_port = os.getenv('APP_PORT', '5000')
appsetup.dosetup()

@app.route('/api/inventory/all', methods=['GET'])
def get_inventory():
    data = inventorydata.get_inventory_data()
    return jsonify(data)

@app.route('/api/inventory/<int:item_id>', methods=['GET'])
def get_inventory_item(item_id):
    item = inventorydata.get_inventory_item(item_id)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item)


app.run(port=app_port)