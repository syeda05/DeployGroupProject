import unittest
import main
import firebase_admin
from firebase_admin import credentials, firestore
from unittest import mock
from main import RecipeManagmentSystem
from unittest.mock import MagicMock , patch,Mock
import sys
from io import StringIO


class TestRecipeManagementSystem(unittest.TestCase):
    
    def test_view_breakfast_recipes(self):
        management = main.RecipeManagmentSystem()
        
        with patch('builtins.input', side_effect=['2', 'sys.exit']):
            with patch('sys.exit'):
                buffer = StringIO()
                sys.stdout = buffer
                management.view_recipe()
                output = buffer.getvalue() #rescipes displayed to user on choosing 2-Breakfast (should be breakfast only)
                sys.stdout = sys.__stdout__
        
        
        #print("=======",print_output)
        test_input1="category: Lunch"
        self.assertNotIn(test_input1,output,"present")
        test_input2="category: Dinner"
        self.assertNotIn(test_input2,output,"present")
        test_input3 = 'category: Breakfast'
        self.assertIn(test_input3,output,"not present")

    def test_view_lunch_recipes(self):
        management = main.RecipeManagmentSystem()
        
        with patch('builtins.input', side_effect=['3', 'sys.exit']):
            with patch('sys.exit'):
                buffer = StringIO()
                sys.stdout = buffer
                management.view_recipe()
                output = buffer.getvalue() #rescipes displayed to user on choosing 2-Breakfast (should be breakfast only)
                sys.stdout = sys.__stdout__
        
        
        #print("=======",print_output)
        test_input1="category: Lunch"
        self.assertIn(test_input1,output,"present")
        test_input2="category: Dinner"
        self.assertNotIn(test_input2,output,"present")
        test_input3 = 'category: Breakfast'
        self.assertNotIn(test_input3,output,"not present")

    def test_view_dinner_recipes(self):
        management = main.RecipeManagmentSystem()
        
        with patch('builtins.input', side_effect=['4', 'sys.exit']):
            with patch('sys.exit'):
                buffer = StringIO()
                sys.stdout = buffer
                management.view_recipe()
                output = buffer.getvalue() #rescipes displayed to user on choosing 2-Breakfast (should be breakfast only)
                sys.stdout = sys.__stdout__
        
        
        #print("=======",print_output)
        test_input1="category: Dinner"
        self.assertIn(test_input1,output,"present")
        test_input2="category: Lunch"
        self.assertNotIn(test_input2,output,"present")
        test_input3 = 'category: Breakfast'
        self.assertNotIn(test_input3,output,"not present")

    
    def test_delete_recipeID_not_present(self):
        management = main.RecipeManagmentSystem()
        r = main.Recipe("240", "Shawarma", 'chilli, salt, pepper', 'gather, cut, cook', 'Dinner', '3')
        # The ID 240 doesn't exist
        self.assertFalse(management.deleteRecipe(r.id))

    def test_duplicate_id(self):
        management = main.RecipeManagmentSystem() 
        recipe1 = main.Recipe('112','Salad','tomatoe, lettuce','Mix it all together','Lunch','1')
        recipe2 = main.Recipe('112','Sandwich','bread, tomatoe, lettuce','Put it all together','Breakfast','2')        
        management.addRecipe(recipe1)
        self.assertFalse(management.addRecipe(recipe2))

if __name__ =='__main__':
    unittest.main()