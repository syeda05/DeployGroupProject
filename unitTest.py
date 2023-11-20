import unittest
import main
import firebase_admin
from firebase_admin import credentials, firestore

class TestRecipeManagementSystem(unittest.TestCase):
    def test_addRecipe(self):
        management = main.RecipeManagmentSystem()
        recipe = management.Recipe('13','Smoothie','Avocado, banana, yogurt, tofu, nut butters and chia seeds','Put it all in the blender in the order above. Then blend until it’s as smooth as you like! Pour it in a cup — or a bowl, if you’re a smoothie bowl fan — and slurp it up.','Breakfast','3')
        management.add_student(recipe)

        allrecipes = management.collection()
        final_data = [doc.to_dict() for doc in allrecipes]
        self.assertIn(recipe, final_data)

if __name__ =='__main__':
    unittest.main()