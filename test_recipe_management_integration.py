import unittest
import firebase_admin
from firebase_admin import credentials, firestore
from unittest.mock import patch
# from main import RecipeManagementSystem  # Assuming RecipeManagementSystem is in main.py
import main 
class TestRecipeManagementSystem(unittest.TestCase):
    @patch('builtins.input', side_effect=['Yes', 'No'])
    def test_delete_recipe(self, mock_input):
        # Your test logic here
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

    # def test_delete_recipeID_not_present(self):
    #     management = main.RecipeManagmentSystem()
    #     r = main.Recipe("14", "Shawarma", 'chilli, salt, pepper', 'gather, cut, cook', 'Dinner', '3')
    #     management.addRecipe(r)
    #     #This ID doesn't exist
    #     management.delete2('15')  
    #     # The list should still have shawarma because the deletion was unsuccessful
    #     reference = management.collection.get()
    #     UpdatedList = [doc.to_dict() for doc in reference]
    #     # Check if the 'Shwarma' recipe is not in the Updated list after deletion attempt
    #     # It is still going to be present because the id for delete doesnt exist
    #     self.assertNotIn( {
    #         "id": '14',
    #         "name": "Shawarma",
    #         "ingredient": 'chilli, salt, pepper',
    #         "instructions": 'gather, cut, cook',
    #         'category': 'Dinner',
    #         'rating': '3'
    #     }, UpdatedList)

    # def test_delete_with_invalid_id(self):
    #     management = main.RecipeManagmentSystem()
    #     # The range for ID says the ID shouldn't be less than 0 
    #     management.delete2('-15')  
    #     reference = management.collection.get()
    #     updatedList = [doc.to_dict() for doc in reference]

    #     reference_length=len(reference) #length of reference list
    #     updatedList_length = len(updatedList) #length of updated list 

    #     #the test will be successful because ID is invalid so length will not increase
    #     self.assertEqual(reference_length, updatedList_length)

if __name__ =='__main__':
    unittest.main()
