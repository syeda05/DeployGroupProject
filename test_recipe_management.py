import unittest
import main
import firebase_admin
from firebase_admin import credentials, firestore


class TestRecipeManagementSystem(unittest.TestCase):
    def test_addRecipe(self):
        management = main.RecipeManagmentSystem()
        recipe = main.Recipe('13','Smoothie','Avocado, banana, yogurt, tofu, nut butters and chia seeds','Put it all in the blender in the order above. Then blend until it’s as smooth as you like! Pour it in a cup — or a bowl, if you’re a smoothie bowl fan — and slurp it up.','Breakfast','3')
        recipe_dic ={"id":recipe.id,"name": recipe.recipeName, "ingredient": recipe.ingredients, "instruction": recipe.instructions, 'category': recipe.category, 'rating': recipe.rating}

        management.addRecipe(recipe)

        allrecipes = management.collection.get()
        final_data = [doc.to_dict() for doc in allrecipes]
        self.assertIn(recipe_dic, final_data)
    
    def test_duplicate_id(self):
        management = main.RecipeManagmentSystem() 
        recipe1 = main.Recipe('112','Salad','tomatoe, lettuce','Mix it all together','Lunch','1')
        recipe2 = main.Recipe('112','Sandwich','bread, tomatoe, lettuce','Put it all together','Breakfast','2')        
        management.addRecipe(recipe1)
        self.assertFalse(management.addRecipe(recipe2)
)
       
        

if __name__ =='__main__':
    unittest.main()