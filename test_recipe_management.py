import unittest
import main
import firebase_admin
from firebase_admin import credentials, firestore
from unittest import mock
from main import RecipeManagmentSystem
from unittest.mock import MagicMock , patch,Mock
import sys
from io import StringIO


class TestRecipeManagementSystem(unittest.TestCase):
    def test_addRecipe(self):
        management = main.RecipeManagmentSystem()
        recipe = main.Recipe('13','Smoothie','Avocado, banana, yogurt, tofu, nut butters and chia seeds','Put it all in the blender in the order above. Then blend until it’s as smooth as you like! Pour it in a cup — or a bowl, if you’re a smoothie bowl fan — and slurp it up.','Breakfast','3')
        recipe_dic ={"id":recipe.id,"name": recipe.recipeName, "ingredient": recipe.ingredients, "instruction": recipe.instructions, 'category': recipe.category, 'rating': recipe.rating}

        management.addRecipe(recipe)

        allrecipes = management.collection.get()
        final_data = [doc.to_dict() for doc in allrecipes]
        self.assertIn(recipe_dic, final_data)
    
    def test_addRecipe_with_missing_field(self):
        management = main.RecipeManagmentSystem()
        recipe1 = main.Recipe('33','','espresso, milk, vanilla extract, caramal sauce',"Heat the milk using a milk frother or steam wand. Alternatively, warm on the hob until just steaming (don't boil) and use a hand frother – you want to aim for a temperature between 60C-70C.",'Breakfast','4')
        recipe2 = main.Recipe('33','Caramel macchiato','',"Heat the milk using a milk frother or steam wand. Alternatively, warm on the hob until just steaming (don't boil) and use a hand frother – you want to aim for a temperature between 60C-70C.",'Breakfast','4')
        recipe3 = main.Recipe('33','Caramel macchiato','espresso, milk, vanilla extract, caramal sauce',"",'Breakfast','4')
        recipe4 = main.Recipe('33','Caramel macchiato','espresso, milk, vanilla extract, caramal sauce',"Heat the milk using a milk frother or steam wand. Alternatively, warm on the hob until just steaming (don't boil) and use a hand frother – you want to aim for a temperature between 60C-70C.",'','4')

        recipe_dic1 ={"id":recipe1.id,"name": recipe1.recipeName, "ingredient": recipe1.ingredients, "instruction": recipe1.instructions, 'category': recipe1.category, 'rating': recipe1.rating}
        recipe_dic2 ={"id":recipe2.id,"name": recipe2.recipeName, "ingredient": recipe2.ingredients, "instruction": recipe2.instructions, 'category': recipe2.category, 'rating': recipe2.rating}
        recipe_dic3 ={"id":recipe3.id,"name": recipe3.recipeName, "ingredient": recipe3.ingredients, "instruction": recipe3.instructions, 'category': recipe3.category, 'rating': recipe3.rating}
        recipe_dic4 ={"id":recipe4.id,"name": recipe4.recipeName, "ingredient": recipe4.ingredients, "instruction": recipe4.instructions, 'category': recipe4.category, 'rating': recipe4.rating}

        with patch('builtins.print'):
            management.addRecipe(recipe1)
            management.addRecipe(recipe2)
            management.addRecipe(recipe3)
            management.addRecipe(recipe4)


        allrecipes = management.collection.get()
        final_data = [doc.to_dict() for doc in allrecipes]
        self.assertNotIn(recipe_dic1, final_data)
        self.assertNotIn(recipe_dic2, final_data)
        self.assertNotIn(recipe_dic3, final_data)
        self.assertNotIn(recipe_dic4, final_data)
    
    def test_addRecipe_rating(self):
        management = main.RecipeManagmentSystem()
        recipe1 = main.Recipe('44','Barbecue beef burger','Beef mince, vegetable oil, dried mixed herbs','Tip the beef mince, shallot, horseradish sauce, herbs and garlic into a bowl, and season well with salt and black pepper. Combine everything well using your hands, squeezing the mixture through your fingers repeatedly to help it bind together.','Dinner','a')
        recipe2 = main.Recipe('44','Barbecue beef burger','Beef mince, vegetable oil, dried mixed herbs','Tip the beef mince, shallot, horseradish sauce, herbs and garlic into a bowl, and season well with salt and black pepper. Combine everything well using your hands, squeezing the mixture through your fingers repeatedly to help it bind together.','Dinner','7')
        recipe_dic1 ={"id":recipe1.id,"name": recipe1.recipeName, "ingredient": recipe1.ingredients, "instruction": recipe1.instructions, 'category': recipe1.category, 'rating': recipe1.rating}
        recipe_dic2 ={"id":recipe2.id,"name": recipe2.recipeName, "ingredient": recipe2.ingredients, "instruction": recipe2.instructions, 'category': recipe2.category, 'rating': recipe2.rating}

        with patch('builtins.print'):
            management.addRecipe(recipe1)
            management.addRecipe(recipe2)

        allrecipes = management.collection.get()
        final_data = [doc.to_dict() for doc in allrecipes]

        self.assertNotIn(recipe_dic1, final_data)
        self.assertNotIn(recipe_dic2, final_data)
    
    def test_addRecipe_category(self):
        management = main.RecipeManagmentSystem()
        recipe1 = main.Recipe('55','Apple Pie','butter, sugar, apple','Mix all the ingredients and bake','Dessert','2')
        recipe2 = main.Recipe('55','Apple Pie','butter, sugar, apple','Mix all the ingredients and bake','12','2')
        recipe3 = main.Recipe('55','Apple Pie','butter, sugar, apple','Mix all the ingredients and bake','-1','2')

        recipe_dic1 ={"id":recipe1.id,"name": recipe1.recipeName, "ingredient": recipe1.ingredients, "instruction": recipe1.instructions, 'category': recipe1.category, 'rating': recipe1.rating}
        recipe_dic2 ={"id":recipe2.id,"name": recipe2.recipeName, "ingredient": recipe2.ingredients, "instruction": recipe2.instructions, 'category': recipe2.category, 'rating': recipe2.rating}
        recipe_dic3 ={"id":recipe3.id,"name": recipe3.recipeName, "ingredient": recipe3.ingredients, "instruction": recipe3.instructions, 'category': recipe3.category, 'rating': recipe3.rating}

        with patch('builtins.print'):
            management.addRecipe(recipe1)
            management.addRecipe(recipe2)
            management.addRecipe(recipe3)

        allrecipes = management.collection.get()
        final_data = [doc.to_dict() for doc in allrecipes]
        self.assertNotIn(recipe_dic1, final_data)
        self.assertNotIn(recipe_dic2, final_data)
        self.assertNotIn(recipe_dic3, final_data)
    
    def test_addRecipe_with_invalid_input(self):
        management = main.RecipeManagmentSystem()
        recipe = main.Recipe('66','-1','boneless chicken, vegetable oil, bell pepper, sour cream',"Combine orange juice, taco seasoning, and vegetable oil in a large resealable bag. Add chicken, coat with the marinade, squeeze out excess air, and seal the bag. Marinate in the refrigerator overnight.",'Dinner','4')
        recipe1 = main.Recipe('66','1','boneless chicken, vegetable oil, bell pepper, sour cream',"Combine orange juice, taco seasoning, and vegetable oil in a large resealable bag. Add chicken, coat with the marinade, squeeze out excess air, and seal the bag. Marinate in the refrigerator overnight.",'Dinner','4')
        recipe2 = main.Recipe('66','Chicken Fajita Tacos','1',"Combine orange juice, taco seasoning, and vegetable oil in a large resealable bag. Add chicken, coat with the marinade, squeeze out excess air, and seal the bag. Marinate in the refrigerator overnight.",'Dinner','4')
        recipe3 = main.Recipe('66','Chicken Fajita Tacos','-1',"Combine orange juice, taco seasoning, and vegetable oil in a large resealable bag. Add chicken, coat with the marinade, squeeze out excess air, and seal the bag. Marinate in the refrigerator overnight.",'Dinner','4')
        recipe4 = main.Recipe('66','Chicken Fajita Tacos','boneless chicken, vegetable oil, bell pepper, sour cream',"1",'Dinner','4')
        recipe5 = main.Recipe('66','Chicken Fajita Tacos','boneless chicken, vegetable oil, bell pepper, sour cream',"-1",'Dinner','4')


        recipe_dic ={"id":recipe1.id,"name": recipe1.recipeName, "ingredient": recipe1.ingredients, "instruction": recipe1.instructions, 'category': recipe1.category, 'rating': recipe1.rating}
        recipe_dic1 ={"id":recipe1.id,"name": recipe1.recipeName, "ingredient": recipe1.ingredients, "instruction": recipe1.instructions, 'category': recipe1.category, 'rating': recipe1.rating}
        recipe_dic2 ={"id":recipe2.id,"name": recipe2.recipeName, "ingredient": recipe2.ingredients, "instruction": recipe2.instructions, 'category': recipe2.category, 'rating': recipe2.rating}
        recipe_dic3 ={"id":recipe3.id,"name": recipe3.recipeName, "ingredient": recipe3.ingredients, "instruction": recipe3.instructions, 'category': recipe3.category, 'rating': recipe3.rating}
        recipe_dic4 ={"id":recipe4.id,"name": recipe4.recipeName, "ingredient": recipe4.ingredients, "instruction": recipe4.instructions, 'category': recipe4.category, 'rating': recipe4.rating}
        recipe_dic5 ={"id":recipe5.id,"name": recipe5.recipeName, "ingredient": recipe5.ingredients, "instruction": recipe5.instructions, 'category': recipe5.category, 'rating': recipe5.rating}


        with patch('builtins.print'):
            management.addRecipe(recipe)
            management.addRecipe(recipe1)
            management.addRecipe(recipe2)
            management.addRecipe(recipe3)
            management.addRecipe(recipe4)
            management.addRecipe(recipe5)

        allrecipes = management.collection.get()
        final_data = [doc.to_dict() for doc in allrecipes]
        self.assertNotIn(recipe_dic, final_data)
        self.assertNotIn(recipe_dic1, final_data)
        self.assertNotIn(recipe_dic2, final_data)
        self.assertNotIn(recipe_dic3, final_data)
        self.assertNotIn(recipe_dic4, final_data)
        self.assertNotIn(recipe_dic5, final_data)
    
    def test_view_breakfast_recipes(self):
        management = main.RecipeManagmentSystem()
        
        with patch('builtins.input', side_effect=['2', 'sys.exit']):
            with patch('sys.exit'):
                buffer = StringIO()
                sys.stdout = buffer
                management.view_recipe()
                output = buffer.getvalue() #rescipes displayed to user on choosing 2-Breakfast (should be breakfast only)
                sys.stdout = sys.__stdout__
        
        
        #print("=======",print_output)
        test_input1="category: Lunch"
        self.assertNotIn(test_input1,output,"present")
        test_input2="category: Dinner"
        self.assertNotIn(test_input2,output,"present")
        test_input3 = 'category: Breakfast'
        self.assertIn(test_input3,output,"not present")

    def test_view_lunch_recipes(self):
        management = main.RecipeManagmentSystem()
        
        with patch('builtins.input', side_effect=['3', 'sys.exit']):
            with patch('sys.exit'):
                buffer = StringIO()
                sys.stdout = buffer
                management.view_recipe()
                output = buffer.getvalue() #rescipes displayed to user on choosing 2-Breakfast (should be breakfast only)
                sys.stdout = sys.__stdout__
        
        
        #print("=======",print_output)
        test_input1="category: Lunch"
        self.assertIn(test_input1,output,"present")
        test_input2="category: Dinner"
        self.assertNotIn(test_input2,output,"present")
        test_input3 = 'category: Breakfast'
        self.assertNotIn(test_input3,output,"not present")

    def test_view_dinner_recipes(self):
        management = main.RecipeManagmentSystem()
        
        with patch('builtins.input', side_effect=['4', 'sys.exit']):
            with patch('sys.exit'):
                buffer = StringIO()
                sys.stdout = buffer
                management.view_recipe()
                output = buffer.getvalue() #rescipes displayed to user on choosing 2-Breakfast (should be breakfast only)
                sys.stdout = sys.__stdout__
        
        
        #print("=======",print_output)
        test_input1="category: Dinner"
        self.assertIn(test_input1,output,"present")
        test_input2="category: Lunch"
        self.assertNotIn(test_input2,output,"present")
        test_input3 = 'category: Breakfast'
        self.assertNotIn(test_input3,output,"not present")

    
    def test_delete_recipeID_not_present(self):
        management = main.RecipeManagmentSystem()
        r = main.Recipe("240", "Shawarma", 'chilli, salt, pepper', 'gather, cut, cook', 'Dinner', '3')
        # The ID 240 doesn't exist
        with patch('builtins.print'):
            self.assertFalse(management.deleteRecipe(r.id))

    def test_duplicate_id(self):
        management = main.RecipeManagmentSystem() 
        recipe1 = main.Recipe('112','Salad','tomatoe, lettuce','Mix it all together','Lunch','1')
        recipe2 = main.Recipe('112','Sandwich','bread, tomatoe, lettuce','Put it all together','Breakfast','2')        
        with patch('builtins.print'):
            management.addRecipe(recipe1)
        self.assertFalse(management.addRecipe(recipe2))

if __name__ =='__main__':
    unittest.main()