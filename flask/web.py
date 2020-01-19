from flask import Flask, Blueprint, request, Response, jsonify
from flask_api import status
from keeper import Keeper

app = Flask(__name__)
keep = Keeper()

@app.route('/<list_id>', methods=['GET'])
def listItems(list_id):
    return jsonify(
        uncheckedItems = keep.getUncheckedItems(list_id),
        checkedItems = keep.getCheckedItems(list_id)
    ), status.HTTP_200_OK

@app.route('/<list_id>', methods=['POST'])
def addListItem(list_id):
    content = request.json
    item = content['item']
    keep.addItem(list_id, item)

    return jsonify(
        addedItem = item,
    ), status.HTTP_200_OK

@app.route('/<list_id>', methods=['PUT'])
def checkUncheck(list_id):
    content = request.json
    item = content['item']

    keep.modifyCheckState(list_id, item)

    return jsonify(
        uncheckedItems = keep.getUncheckedItems(list_id),
        checkedItems = keep.getCheckedItems(list_id)
    ), status.HTTP_200_OK


@app.route('/login', methods=['POST'])
def login():
    content = request.json
    email = content['email']
    password = content['password']

    token = keep.login(email, password)

    return jsonify(
        token = token
    ), status.HTTP_200_OK
