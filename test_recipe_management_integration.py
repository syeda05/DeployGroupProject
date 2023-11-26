import unittest
import firebase_admin
from firebase_admin import credentials, firestore
from unittest import mock
from unittest.mock import MagicMock, patch
# from main import RecipeManagementSystem  # Assuming RecipeManagementSystem is in main.py
import main 
class TestRecipeManagementSystem(unittest.TestCase):

    def test_delete_recipe(self):
        management = main.RecipeManagmentSystem()
        r=main.Recipe("12", "Brownie", 'potato, salt, pepper', 'gather, cut, cook', 'Lunch', '5')


        management.addRecipe(r)

        recipe_added = {"id": '12', "name": "Brownie", "ingredient": 'potato, salt, pepper',
                        "instructions": 'gather, cut, cook', 'category': 'Lunch', 'rating': '5'}

        management.delete2('12')
      
        # Updated doc to compare
        ref = management.collection.get()
        updated = [doc.to_dict() for doc in ref]

        self.assertNotIn(recipe_added, updated, msg="Recipe should not be in the list")
        
   

   

    def test_add_view_recipe(self):
        management = main.RecipeManagmentSystem()
        recipe1 = main.Recipe("25", "smoothie", "strawberry, banana, ice cream", "mix starwberry and banana together and ice cream", "Lunch", "3")
        management.addRecipe(recipe1)
    
        with patch('builtins.input',side_effect=['3', 'sys.exit']):
            with patch('sys.exit'):
            
                output = management.view_recipe()
                recipe_add = None
                for recipe in output:
                    if recipe.id == recipe1.id:
                        break  
        self.assertIsNotNone(recipe_add, "The added recipe was not found") 
    
    
        expected_output = f"id: {recipe1.id}, name: {recipe1.recipeName}, ingredient: {recipe1.ingredients}, instruction: {recipe1.instructions}, category: {recipe1.category}, rating: {recipe1.rating}"
        actual_output = f"id: {recipe_add.id}, name: {recipe_add.recipeName}, ingredient: {recipe_add.ingredients}, instruction: {recipe_add.instructions}, category: {recipe_add.category}, rating: {recipe_add.rating}"
    
    
        self.assertEqual(expected_output, actual_output) 


if __name__ =='__main__':
    unittest.main()
