from flask_restful import Resource
from models.store import StoreModel
from flask_jwt import jwt_required


class Store(Resource):

	@jwt_required()
	def get(self, name):
		store = StoreModel.find_by_name(name)
		if store:
			return store.json()

		return {'message': 'Store not found'}, 404

	@jwt_required()
	def post(self, name):
		if StoreModel.find_by_name(name):
			return {'message': f'A store called {name} already exists.'}, 400
		store = StoreModel(name)
		try:
			store.save_to_db()
		except:
			# We are not sure what kind of error this might be, but it is not the user's fault. Internal server error.
			return {'message': 'An error occurred while creating the store.'}, 500

		return store.json(), 201

	@jwt_required()
	def delete(self, name):
		store = StoreModel.find_by_name(name)
		if store:
			store.delete_from_db()

		return {'message': 'Store deleted.'}


class StoreList(Resource):

	@jwt_required()
	def get(self):
		return {'stores': [store.json() for store in StoreModel.query.all()]}
