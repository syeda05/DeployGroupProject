import sys
import firebase_admin
from firebase_admin import credentials, firestore
import random
from collections import OrderedDict

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
class Recipe:
    def __init__(self, id, recipeName, ingredients, instructions, category, rating):
         self.id = id
         self.recipeName = recipeName
         self.ingredients = ingredients
         self.instructions = instructions  # Fixed typo: instruction -> instructions
         self.category = category
         self.rating = rating

class RecipeManagmentSystem:
    def __init__(self, db_name = 'recipes'):
        
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
                self.view_recipe()
            elif userInput == '2':
                num = random.randint(0,200)   #generate random number for id
                while self.collection.document(str(num)).get().exists:
                    num = random.randint(0,200)
                id = str(num)

                name = input('Enter recipe name: ')
                while name == '' or name.isdigit():
                    print("Invalid input. Please enter a recipe name.")
                    name = input('Enter recipe name: ')
         
                ing = input('Enter recipe ingredients (Separate values by ,): ')
                while ing == '' or ing.isdigit():
                    print("Invalid input. Please enter ingredients.")
                    ing = input('Enter recipe ingredients (Separate values by ,): ')
                ing = ing.split(',')
                
                
                ins = input('Enter recipe instructions: ')
                while ins == '' or ins.isdigit():
                    print("Invalid input. Please enter recipe instructions.")
                    ins = input('Enter recipe instructions: ')

                category = input('Enter recipe category (Breakfast, Lunch, or Dinner): ')
                while category == '' or category.isdigit() or category.lower() not in ['breakfast','lunch','dinner']:
                    print("Invalid input. Please enter recipe category.")
                    category = input('Enter recipe category (Breakfast, Lunch, or Dinner): ')

                rating = input('Enter recipe rating: ')

                while not rating.isdigit() or (int(rating)<1 or int(rating)>5) :
                    print("Invalid input. Please enter recipe rating.")
                    rating = input('Enter recipe rating: ')

                recipe = Recipe(id, name, ing, ins, category, rating)

                self.addRecipe(recipe)
                self.selectOptions()


            elif userInput == '3':
                #display all the recipes with the viewRecipes function
                id=input("Enter the ID number of the recipe you want to edit :")
                self.editRecipe(id)
                
            elif userInput == '4':
                userInput=input("Enter the ID number of the record you want to delete :")
                self.deleteRecipe(userInput)
            elif userInput == '5':
                print("Function for Exiting Recipe will be called")
                
        else:
            print("-----------------------------------------------")
            print("Error: The number should be between 1 to 5 inclusively")

            self.selectOptions()
  


        



        




       

    def view_recipe(self):
        print("1-View all")
        print("2-Breakfast")
        print("3-Lunch")
        print("4-Dinner")
        user_Input = (input("Please select from the above option:"))
        while user_Input.isdigit() == False:
            print("please select from the above option.")
        if user_Input == '1':
            print("All recipes will be displayed.")
            docs = self.collection.get()
            lists = []
            for view_recipe in docs:
                
                data_view = view_recipe
                result_view = {
                    'id':data_view.get('id'),
                    'name':data_view.get('name'),
                    'category':data_view.get('category'),
                    'rating':data_view.get('rating'),
                    'ingredient':data_view.get('ingredient'),
                    'instruction':data_view.get('instruction'),

                }

                lists.append(result_view)
            for result_view in lists:
                for key, value in result_view.items():
                    print(f'{key}: {value}')
                print("\n")


            yes_input = (input("say yes if you want to go to main option or not exit: "))
            if yes_input.lower() == 'yes':
                self.selectOptions()
            else:
                self.exit_recipe()
           
        elif user_Input == '2':
            print("Breakfast menu will be shown.")
            break_docs = self.collection.where("category", "==", "Breakfast").get()
            list =[]
            for recipe_break in break_docs:
                data_all = recipe_break

                total = {
                    'id': data_all.get('id'),
                    'name': data_all.get('name'),
                    'category': data_all.get('category'),
                    'rating': data_all.get('rating'),
                    'ingredient': data_all.get('ingredient'),
                    'instruction': data_all.get('instruction')

                }
                list.append(total)
            for total in list:
                for key, value in total.items():
                    print(f'{key}: {value}')
                print("\n")
            yes_input = (input("say yes if you want to go to main option or else exit: "))
            if yes_input.lower() == 'yes':
                self.selectOptions()
            else:
                self.exit_recipe()
            
            
        elif user_Input == '3':
            lunchList=[]
            print("Lunch menu will be displayed.")
            lunch_docs = self.collection.where("category", "==", "Lunch").get()
            for lunches in lunch_docs:
                
                datas = lunches
                

                result = {
                    'id':datas.get('id'),
                    'name':datas.get('name'),
                    'category':datas.get('category'),
                    'rating':datas.get('rating'),
                    'ingredient':datas.get('ingredient'),
                    'instruction':datas.get('instruction')

                }

                lunchList.append(result)
            for result in lunchList:
                for key, value in result.items():
                    print(f'{key}: {value}')
                print("\n")
            yes_input = (input("say yes if you want to go to main option or else exit: "))
            if yes_input.lower() == 'yes':
                self.selectOptions()
            else:
                self.exit_recipe()
            
        elif user_Input == '4':
            print("Dinner menu will be displayed.")
            dinner_docs = self.collection.where("category", "==", "Dinner").get()
            list_d = []
            for dinner in dinner_docs:
                data_d = dinner
               

                results_t = {
                    'id':data_d.get('id'),
                    'name':data_d.get('name'),
                    'category':data_d.get('category'),
                    'rating':data_d.get('rating'),
                    'ingredient':data_d.get('ingredient'),
                    'instruction':data_d.get('instruction'),

                }
                list_d.append(results_t)
            for result_t in list_d:
                for key, value in result_t.items():
                    print(f'{key}: {value}')
                print("\n")
          

            yes_input = (input("say yes if you want to go to main option or else exit: "))
            if yes_input.lower() == 'yes':
                self.selectOptions()
            else:
                self.exit_recipe()  

    def delete2(self,input):

        if self.collection.document(input).get().exists:
            return False

        else:
            return True


    def deleteRecipe(self, userInput):
        
        while not self.delete2:
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
             confirmation=input("Do you want to select another recipe option?")
             
             if confirmation.lower()=='yes':
                 self.selectOptions()                
             else:
                 self.exit_recipe()         
        else:
             confirmation2=input("Do you want to select another option?")
             
             if confirmation2.lower()=='yes':
                 self.selectOptions()
                
             else:
                 self.exit_recipe()   
                    

    def addRecipe(self,recipe):

        recipe_dic ={"id":recipe.id,"name": recipe.recipeName, "ingredient": recipe.ingredients, "instruction": recipe.instructions, 'category': recipe.category, 'rating': recipe.rating}

        self.collection.document(recipe.id).set(recipe_dic)
        print('Recipe added successfully!')


    def editRecipe(self, id):
        while id.isdigit()==False:
            id=input("Enter the ID number of the recipe you want to edit :")

        print('Recipe Fields:')
        print("1- Name")
        print("2- Ingredients")
        print("3- Instructions")
        print("4- Category")
        print("5- Rating")
        print("6- Exit")

        option=(input("Select the recipe field you want to edit (Enter a number between 1 and 6): "))
        
        while not option.isdigit() or (int(option)<1 or int(option)>6) :
            print("Invalid input. Please select a valid recipe field.")
            option = input('Select the recipe field you want to edit (Enter a number between 1 and 6): ')
    
        if option == '1':
            name= input("Enter recipe name: ")
            while name == '' or name.isdigit():
                print("Invalid input. Please enter a recipe name.")
                name = input('Enter recipe name: ')
            verification= input("Are you sure you want to update the record (Type yes or no)?")
            if verification.lower()=='yes':
                self.collection.document(id).update({'name':name})
                print("Recipe name updated successfully!")
            else:
                self.selectOptions()

        elif option == '2':
            ing = input('Enter recipe ingredients (Separate values by ,): ')
            while ing == '' or ing.isdigit():
                print("Invalid input. Please enter ingredients.")
                ing = input('Enter recipe ingredients (Separate values by ,): ')
            ing = ing.split(',')
            verification= input("Are you sure you want to update the record (Type yes or no)?")
            if verification.lower()=='yes':
                self.collection.document(id).update({'ingredient':ing})
                print("Recipe ingredients updated successfully!")
            else:
                self.selectOptions()
        
        elif option == '3':
            ins = input('Enter recipe instructions: ')
            while ins == '' or ins.isdigit():
                print("Invalid input. Please enter recipe instructions.")
                ins = input('Enter recipe instructions: ')
            verification= input("Are you sure you want to update the record (Type yes or no)?")
            if verification.lower()=='yes':
                self.collection.document(id).update({'instruction':ins})
                print("Recipe instructions updated successfully!")
            else:
                self.selectOptions()

        elif option == '4':
            category = input('Enter recipe category (Breakfast, Lunch, or Dinner): ')
            while category == '' or category.isdigit() or category.lower() not in ['breakfast','lunch','dinner']:
                print("Invalid input. Please enter recipe category.")
                category = input('Enter recipe category (Breakfast, Lunch, or Dinner): ')
            verification= input("Are you sure you want to update the record (Type yes or no)?")
            if verification.lower()=='yes':
                self.collection.document(id).update({'category':category})
                print("Recipe category updated successfully!")
            else:
                self.selectOptions()


        
        elif option == '5':
            rating = input('Enter recipe rating: ')
            while not rating.isdigit() or (int(rating)<1 or int(rating)>5) :
                print("Invalid input. Please enter recipe rating.")
                rating = input('Enter recipe rating: ')
            verification= input("Are you sure you want to update the record (Type yes or no)?")
            if verification.lower()=='yes':
                self.collection.document(id).update({'rating':rating})
                print("Recipe rating updated successfully!")
            else:
                self.selectOptions()
            
        elif option == '6':
            self.selectOptions()
        
        confirmation = input("Do you want to select another recipe option (Type yes or no)? ")
        if confirmation.lower() == 'yes':
            self.selectOptions()
        else:
            self.exit_recipe()

    def exit_recipe(self):
        return sys.exit()
    
def main():
    r = RecipeManagmentSystem()
    r.selectOptions()


if __name__ == "__main__":
    main()
   


