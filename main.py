import firebase_admin
from firebase_admin import credentials, firestore
import random

class Recipe:
    def __init__(self, id, recipeName, ingredients, instructions, category, rating  ):
         self.id = id
         self.recipeName = recipeName
         self.ingredients = ingredients
         self.instruction = instructions
         self.category =category
         self.rating = rating

class RecipeManagmentSystem:
    def __init__(self, db_name = 'recipes'):
        cred = credentials.Certificate("key.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.collection = self.db.collection(db_name)

    def selectOptions(self):
        print('Recipe Management System')
        print("1- View Recipes")
        print("2- Add Recipes")
        print("3- Edit Recipes")
        print("4- Delete Recipes")
        print("5- Exit Recipes")

        userInput=(input("Please select from one of the options above: "))

        while userInput.isdigit()==False:
             userInput=(input("Please select from one of the options above: "))
        
        if int(userInput)>=1 and int(userInput)<=5:
            if userInput == '1':
                print("Function for Viewing Recipe will be called")
            elif userInput == '2':
                print("Function for Adding Recipe will be called")
                id = random.randint(0,200)
                name = input('Enter recipe name: ')
                ing = input('Enter recipe ingredients (Separate values by ,): ')
                ins = input('Enter recipe instructions: ')
                category = input('Enter recipe category: ')
                rating = input('Enter recipe rating: ')
                recipe = Recipe(str(id), name, ing, ins, category, rating)
                self.addRecipe(recipe)

            elif userInput == '3':
                print("Function for Editing Recipe will be called")
            elif userInput == '4':
                print("Function for Deleting Recipe will be called")
            elif userInput == '5':
                print("Function for Exiting Recipe will be called")
                
        else:
            print("-----------------------------------------------")
            print("Error: The number should be between 1 to 5 inclusively")
            self.selectOptions()

    def addRecipe(self,recipe):
        recipe_dic ={"id":recipe.id,"name": recipe.recipeName, "ingredient": recipe.ingredients, "instruction": recipe.instruction, 'category': recipe.category, 'rating': recipe.rating}

        self.collection.document(recipe.id).set(recipe_dic)
        print('Recipe added successfully!')

r = RecipeManagmentSystem()
r.selectOptions()