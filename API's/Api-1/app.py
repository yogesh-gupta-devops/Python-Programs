from flask import Flask, request
import uuid

app = Flask(__name__)

items = {
    'ba5f6ccb893f4f3f9ebcca35090e0d3a': {"Name": "Green Apple", "Price": 150},
    '85d744c7fdfc4fa2b40b8bcaf5c91ee8': {"Name": "Apple", "Price": 120},
    'a4986f47e6ac461f9e223cca0711b6fc': {"Name": "Orange", "Price": 100},
    '0ae62d1318f44221a1236214f7a99b07': {"Name": "Banana", "Price": 60}
}


@app.get('/items')
def get_items():
    return {"items": items}


@app.get('/item/<string:name>')
def get_item(name):
    for item in items:
        if name == item['Name']:
            return item
    return {"Message": "Recorde not found"}


@app.get('/item1')
def get_item1():
    name = request.args.get('name')
    for item in items:
        if name == item['Name']:
            return item
    return {"Message": "Recorde not found"}


@app.get('/item2')
def get_item2():
    id = request.args.get('id')
    try:
        return items[id]
    except KeyError:
        return {"Message": "Recorde Not Found"}, 404


@app.post('/items')
def add_items():
    items[uuid.uuid4().hex] = request.get_json()
    return {"Message": "Data Add Successfully"}, 201


@app.put('/items')
def update_item():
    id = request.args.get('id')
    if id in items.keys():
        items[id] = request.get_json()
        return {"Message": "Item Successfully Update"}, 200
    else:
        return {"Message": "ID Not Found"}, 404


@app.delete('/items')
def delete_items():
    id = request.args.get('id')
    if id in items.keys():
        del items[id]
        return {"Message": "Items delete successfully"}
    else:
        return {"Message": "Recorde not found"}
