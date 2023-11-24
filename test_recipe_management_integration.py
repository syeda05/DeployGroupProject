import unittest
from unittest.mock import MagicMock, patch
import firebase_admin
from firebase_admin import credentials, firestore
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
    
    @patch('builtins.input', side_effect=['111','1', 'Gelato', 'yes'])   #creates a MagicMock() object
    def test_editRecipe(self, mock_editRecipe):
        management = main.RecipeManagmentSystem()
        r=main.Recipe("111", "Ice Cream", 'milk, sugar', 'blend together','Lunch', '4')
        management.addRecipe(r)

        # mock_editRecipe.side_effect = [1,'Fries','yes']   

        with patch('builtins.print'):  # to avoid unwanted prints during the test
            management.editRecipe('111') 

        # mock_editRecipe.assert_called_once_with('12', option=1, name='Fries', verification='yes')
        allrecipes = management.collection.get()
        final_data = [doc.to_dict() for doc in allrecipes]

        recipe_dic ={"id":'111',"name": "Gelato", "ingredient": 'milk, sugar', "instruction": 'blend together', 'category': 'Lunch', 'rating': '4'}
        
        self.assertIn(recipe_dic, final_data)


if __name__ =='__main__':
    unittest.main()
