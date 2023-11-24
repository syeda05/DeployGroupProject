import unittest
import main
import firebase_admin
from firebase_admin import credentials, firestore
from unittest import mock 
from unittest.mock import MagicMock , patch


class TestRecipeManagementSystem(unittest.TestCase):
    # def test_addRecipe(self):
    #     management = main.RecipeManagmentSystem()
    #     recipe = main.Recipe('13','Smoothie','Avocado, banana, yogurt, tofu, nut butters and chia seeds','Put it all in the blender in the order above. Then blend until it’s as smooth as you like! Pour it in a cup — or a bowl, if you’re a smoothie bowl fan — and slurp it up.','Breakfast','3')
    #     recipe_dic ={"id":recipe.id,"name": recipe.recipeName, "ingredient": recipe.ingredients, "instruction": recipe.instructions, 'category': recipe.category, 'rating': recipe.rating}

    #     management.addRecipe(recipe)

    #     allrecipes = management.collection.get()
    #     final_data = [doc.to_dict() for doc in allrecipes]
    #     self.assertIn(recipe_dic, final_data)


    
    
    @mock.patch('builtins.input', side_effect=['2']) 
    @mock.patch('builtins.print')
    def test_view_recipe(self):
        management = main.RecipeManagmentSystem()
        management.view_recipe()
        #expected_output = self.collection.where("category","==","Breakfast")
      
        output =  self.collection.where("category","==","Breakfast")
     
        message = "First value and second value are not equal !"
        self.assertEqual(expected_output,output,message) 



        print(output)
        
        


if __name__ =='__main__':
    unittest.main()