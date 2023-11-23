import unittest
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

if __name__ =='__main__':
    unittest.main()
