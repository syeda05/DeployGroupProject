import unittest
from unittest.mock import MagicMock, patch
import firebase_admin
from firebase_admin import credentials, firestore

import main 

class TestRecipeManagementSystem(unittest.TestCase):
    @patch('builtins.input', side_effect=['Yes', 'No'])
    def test_delete_recipe(self, mock_input):
        management = main.RecipeManagmentSystem()
        r = main.Recipe("12", "Soup", 'potato, salt, pepper', 'gather, cut, cook', 'Lunch', '5')
        management.addRecipe(r)
        recipe_added = {
            "id": '12',
            "name": "Soup",
            "ingredient": 'potato, salt, pepper',
            "instructions": 'gather, cut, cook',
            'category': 'Lunch',
            'rating': '5'
        }
        with patch('builtins.print'):
            management.deleteRecipe('12')

        # Updated doc to compare
        reference = management.collection.get()
        updated_list = [doc.to_dict() for doc in reference]
        self.assertNotIn(recipe_added, updated_list)


    
    @patch('builtins.input', side_effect=['111','1', 'Gelato', 'yes'])  
    def test_editRecipe(self, mock_editRecipe):
        management = main.RecipeManagmentSystem()
        r=main.Recipe("111", "Ice Cream", 'milk, sugar', 'blend together','Lunch', '4')
        management.addRecipe(r)

        with patch('builtins.print'):  # to avoid unwanted prints during the test
            management.editRecipe('111') 

        allrecipes = management.collection.get()
        final_data = [doc.to_dict() for doc in allrecipes]

        recipe_dic ={"id":'111',"name": "Gelato", "ingredient": 'milk, sugar', "instruction": 'blend together', 'category': 'Lunch', 'rating': '4'}
        
        self.assertIn(recipe_dic, final_data)


if __name__ =='__main__':
    unittest.main()
