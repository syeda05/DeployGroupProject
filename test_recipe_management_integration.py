import unittest
from unittest.mock import MagicMock, patch
import firebase_admin
from firebase_admin import credentials, firestore
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
    
    @patch('main.RecipeManagmentSystem.editRecipe.input', create=True)   #creates a MagicMock() object
    def test_editRecipe(self, mock_editRecipe):
        management = main.RecipeManagmentSystem()
        r=main.Recipe("12", "Brownie", 'potato, salt, pepper', 'gather, cut, cook', 'Lunch', '5')
        management.addRecipe(r)

        mock_editRecipe.side_effects = [1,'Fries','yes']    

        management.editRecipe('62')
        # mock_editRecipe.assert_called_once_with('62', option=1, name='Fries', verification='yes')
        allrecipes = management.collection.get()
        final_data = [doc.to_dict() for doc in allrecipes]

        recipe_dic ={"id":62,"name": "Fries", "ingredient": "chicken, salt", "instruction": 'gsgssgsgs', 'category': 'Lunch', 'rating': '5'}
        
        self.assertIn(recipe_dic, final_data)


if __name__ =='__main__':
    unittest.main()
