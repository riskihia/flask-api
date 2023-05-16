import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores

blp = Blueprint("stores", __name__, description="Option in store")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "store deleted"}
        except KeyError:
            abort(404, message="store not found")


@blp.route("/store")
class StooreList(MethodView):
    def get(self):
        return {stores, list(stores.values())}

    def post(self):
        store_data = request.get_json()

        if "name" not in store_data:
            abort(400, message="Bad request, nama required")

        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message="sore already existx")

        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store
        return store, 201
