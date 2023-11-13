import firebase_admin
from firebase_admin import credentials, firestore

class Recipe:
    def __init__(self, id, recipeName, ingredients, instructions, category, rating  ):
         self.id = id
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
            elif userInput == '3':
                print("Function for Editing Recipe will be called")
            elif userInput == '4':
                userInput=input("Enter the ID number of the record you want to delete :")
                self.deleteRecipe(userInput)
            elif userInput == '5':
                print("Function for Exiting Recipe will be called")
                
        else:
            print("-----------------------------------------------")
            print("Error: The number should be between 1 to 5 inclusively")
            self.selectOptions()
    def deleteRecipe(self, userInput):
        
        while not self.collection.document(userInput).get().exists:
             print("The record with that ID doesn't exist")
             check=input("Do you want to select another record ID for deleteing (Type yes or no)?")
             if check.lower()=='yes':
                userInput=input("Enter the ID number of the record you want to delete :")
             else:
                self.selectOptions()
               
        verification= input("Are you sure you want to delete the record (Type yes or no)?")
        if verification.lower()=='yes':
             self.collection.document(userInput).delete()
             print('The record has been deleted sucessfully')
             self.selectOptions()
             
        else:
            self.selectOptions()

r = RecipeManagmentSystem()
r.selectOptions()