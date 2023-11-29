import unittest
from unittest.mock import MagicMock, patch
import firebase_admin
from firebase_admin import credentials, firestore
from unittest import mock
from unittest.mock import MagicMock, patch
import sys
from io import StringIO
# from main import RecipeManagementSystem  # Assuming RecipeManagementSystem is in main.py
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


    
    def test_view_recipe(self):
        management = main.RecipeManagmentSystem()
        recipe1 = main.Recipe("23", "Juices kiwi", "apple,orange,kiwi", "mix apple and orange, kiwi together", "Dinner", "5")
        management.addRecipe(recipe1)

        with patch('builtins.input', side_effect=['4', 'sys.exit']):
            with patch('sys.exit'):  # to avoid unwanted prints during the test
                buffer = StringIO()
                sys.stdout = buffer
                management.view_recipe()
                output = buffer.getvalue()
                sys.stdout = sys.__stdout__

        
       
       
    
    
       
        expected_recipe = {"id":"23", "name ": "Juices kiwi", "ingredint": "apple,orange,kiwi", "instruction":"mix apple and orange, kiwi together",  "category":"Dinner","rating" :"5"}
        for keys, values in expected_recipe.items():
            print(values)
        
    
       
        self.assertIn(values, output)

    
    @patch('builtins.input', side_effect=['61','1', '6','62','1','','81','1','-1'])  
    def test_editRecipe_name(self, mock_editRecipe):
        management = main.RecipeManagmentSystem()
        r1=main.Recipe("61", "Ice Cream", 'milk, sugar', 'blend together','Lunch', '4')
        r2=main.Recipe("62", "Ice Cream", 'milk, sugar', 'blend together','Lunch', '4')
        r3=main.Recipe("81", "Ice Cream", 'milk, sugar', 'blend together','Lunch', '4')

        with patch('builtins.print'):  # to avoid unwanted prints during the test
            management.addRecipe(r1)
            management.addRecipe(r2)
            management.addRecipe(r3)


        with patch('builtins.print'):  # to avoid unwanted prints during the test
            management.editRecipe('61')
            management.editRecipe('62') 
            management.editRecipe('81') 
 

        allrecipes = management.collection.get()
        final_data = [doc.to_dict() for doc in allrecipes]

        recipe_dic1 ={"id":'61',"name": "6", "ingredient": 'milk, sugar', "instruction": 'blend together', 'category': 'Lunch', 'rating': '4'}
        recipe_dic2 ={"id":'62',"name": "", "ingredient": 'milk, sugar', "instruction": 'blend together', 'category': 'Lunch', 'rating': '4'}
        recipe_dic3 ={"id":'81',"name": "-1", "ingredient": 'milk, sugar', "instruction": 'blend together', 'category': 'Lunch', 'rating': '4'}

        self.assertNotIn(recipe_dic1, final_data)
        self.assertNotIn(recipe_dic2, final_data)
        self.assertNotIn(recipe_dic3, final_data)

    @patch('builtins.input', side_effect=['63', '5', '','64', '5', '0','65', '5', 'a'])
    def test_editRecipe_ratings(self, mock_editRecipe):
        management = main.RecipeManagmentSystem()
        r1 = main.Recipe("63", "Ice Cream", 'milk, sugar', 'blend together', 'Lunch', '2')
        r2 = main.Recipe("64", "Ice Cream", 'milk, sugar', 'blend together', 'Lunch', '2')
        r3 = main.Recipe("65", "Ice Cream", 'milk, sugar', 'blend together', 'Lunch', '2')

        with patch('builtins.print'):  # to avoid unwanted prints during the test
            management.addRecipe(r1)
            management.addRecipe(r2)
            management.addRecipe(r3)

        with patch('builtins.print'):  # to avoid unwanted prints during the test
            management.editRecipe('63')
            management.editRecipe('64')
            management.editRecipe('65')

        allrecipes = management.collection.get()
        final_data = [doc.to_dict() for doc in allrecipes]

        recipe_dic1 ={"id":'63',"name": "cake", "ingredient": 'milk, sugar', "instruction": 'blend together', 'category': 'Lunch', 'rating': ''}
        recipe_dic2 ={"id":'64',"name": "cake", "ingredient": 'milk, sugar', "instruction": 'blend together', 'category': 'Lunch', 'rating': '0'}
        recipe_dic3 ={"id":'64',"name": "cake", "ingredient": 'milk, sugar', "instruction": 'blend together', 'category': 'Lunch', 'rating': 'a'}

        self.assertNotIn(recipe_dic1, final_data)
        self.assertNotIn(recipe_dic2, final_data)
        self.assertNotIn(recipe_dic3, final_data) 


if __name__ =='__main__':
    unittest.main()
