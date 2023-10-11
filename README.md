# Inventory Service

This is a simple inventory service that reports on stock levels for products.

## Usage

1. Install the dependencies using the following command:

```
pip install -r requirements.txt
```

2. Run the application using the following command:

```
python app.py
```

You may also want to use `venv` to isolate your python environment.

## Endpoints

All endpoints return JSON.

**GET /api/inventory/all**

Returns all stock items.

**GET /api/inventory/{id}**

Returns the stock item with the specified id.

### The Stock Item:

The stock item is a simple object with the following properties:
```
id: int
name: str
remaining_stock: int
```

## Power Platform Connector

The Power Platform connector is a simple wrapper around the API. It is a custom connector that can be imported into Power Apps, Power Automate, Power BI and Logic Apps.

The metadata and OpenAPI (Swagger) API definition can be found in the `powerplatform` directory.