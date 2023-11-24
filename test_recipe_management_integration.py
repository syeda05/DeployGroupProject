import unittest
import firebase_admin
from firebase_admin import credentials, firestore
from unittest.mock import patch
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


if __name__ =='__main__':
    unittest.main()
