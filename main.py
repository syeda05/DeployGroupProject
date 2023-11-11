import firebase_admin
from firebase_admin import credentials, firestore

class Recipe:
    def __init__(self, recipeName, ingredients, instructions, category, rating  ):
         self.recipeName = recipeName
         self.ingredients = ingredients
         self.instruction = instructions
         self.category =category
         self.rating = rating

class RecipeManagmentSystem:
    def _init_(self, db_name = 'recipes'):
        cred = credentials.Certificate("key.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.collection = self.db.collection(db_name)

r = RecipeManagmentSystem()