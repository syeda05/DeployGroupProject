import unittest
from unittest.mock import MagicMock, patch
import firebase_admin
from firebase_admin import credentials, firestore
from unittest import mock
from unittest.mock import MagicMock, patch
import sys
from io import StringIO
import main 

class TestRecipeManagementSystem(unittest.TestCase):
    @patch('builtins.input', side_effect=['Yes', 'No'])
    def test_delete_recipe(self, mock_input):
        management = main.RecipeManagmentSystem()
        r = main.Recipe("12", "Soup", 'potato, salt, pepper', 'gather, cut, cook', 'Lunch', '5')
        
        with patch('builtins.print'):
            management.addRecipe(r)
        recipe_added = {
            "id": '12',
            "name": "Soup",
            "ingredient": 'potato, salt, pepper',
            "instructions":'gather, cut, cook',
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
        
        with patch('builtins.print'):
            management.addRecipe(r)

        with patch('builtins.print'):  
            management.editRecipe('111') 

        allrecipes = management.collection.get()
        final_data = [doc.to_dict() for doc in allrecipes]

        recipe_dic ={"id":'111',"name": "Gelato", "ingredient": 'milk, sugar', "instruction": 'blend together', 'category': 'Lunch', 'rating': '4'}
        
        self.assertIn(recipe_dic, final_data)
    
    def test_view_recipe(self):
        management = main.RecipeManagmentSystem()
        recipe1 = main.Recipe("23", "Juices kiwi", "apple,orange,kiwi", "mix apple and orange, kiwi together", "Dinner", "5")
        
        with patch('builtins.print'):
            management.addRecipe(recipe1)

        with patch('builtins.input', side_effect=['4', 'sys.exit']):
            with patch('sys.exit'): 
                buffer = StringIO()
                sys.stdout = buffer
                management.view_recipe()
                output = buffer.getvalue()
                sys.stdout = sys.__stdout__
      
        expected_recipe = {"id":"23", "name ": "Juices kiwi", "ingredient": "apple,orange,kiwi", "instruction":"mix apple and orange, kiwi together",  "category":"Dinner","rating" :"5"}
        for keys, value in expected_recipe.items():
            self.assertIn(value, output)
    
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
        
    @patch('builtins.input', side_effect=['66', '2', '','67', '2', '4','88', '2', '-3'])
    def test_editRecipe_ingredients(self, mock_editRecipe):
        management = main.RecipeManagmentSystem()
        r1 = main.Recipe("66", "Ice Cream", 'milk, sugar', 'blend together', 'Lunch', '2')
        r2 = main.Recipe("67", "Ice Cream", 'milk, ,honey,sugar', 'blend together', 'Lunch', '2')
        r3 = main.Recipe("88", "Ice Cream", 'milk, ,honey,sugar', 'blend together', 'Lunch', '2')

        with patch('builtins.print'):  # to avoid unwanted prints during the test
            management.addRecipe(r1)
            management.addRecipe(r2)
            management.addRecipe(r3)

        with patch('builtins.print'):  # to avoid unwanted prints during the test
            management.editRecipe('66')
            management.editRecipe('67')
            management.editRecipe('88')

        allrecipes = management.collection.get()
        final_data = [doc.to_dict() for doc in allrecipes]

        recipe_dic1 ={"id":'66',"name": "cake", "ingredient": '', "instruction": 'blend together', 'category': 'Lunch', 'rating': '4'}
        recipe_dic2 ={"id":'67',"name": "cake", "ingredient": '4', "instruction": 'blend together', 'category': 'Lunch', 'rating': '4'}
        recipe_dic3 ={"id":'88',"name": "cake", "ingredient": '-3', "instruction": 'blend together', 'category': 'Lunch', 'rating': '4'}

        self.assertNotIn(recipe_dic1, final_data)
        self.assertNotIn(recipe_dic2, final_data)
        self.assertNotIn(recipe_dic3, final_data)

    @patch('builtins.input', side_effect=['68', '3', '','69', '3', '3','99', '3', '-4'])
    def test_editRecipe_instructions(self, mock_editRecipe):
        management = main.RecipeManagmentSystem()
        r1 = main.Recipe("68", "Ice Cream", 'milk, sugar', 'blend together', 'Lunch', '2')
        r2 = main.Recipe("69", "Ice Cream", 'milk, ,honey,sugar', 'blend together', 'Lunch', '2')
        r3 = main.Recipe("99", "Ice Cream", 'milk, ,honey,sugar', 'blend together', 'Lunch', '2')

        with patch('builtins.print'):  # to avoid unwanted prints during the test
            management.addRecipe(r1)
            management.addRecipe(r2)
            management.addRecipe(r3)

        with patch('builtins.print'):  # to avoid unwanted prints during the test
            management.editRecipe('68')
            management.editRecipe('69')
            management.editRecipe('99')

        allrecipes = management.collection.get()
        final_data = [doc.to_dict() for doc in allrecipes]

        recipe_dic1 ={"id":'68',"name": "cake", "ingredient": 'honey,milk', "instruction": '', 'category': 'Lunch', 'rating': '4'}
        recipe_dic2 ={"id":'69',"name": "cake", "ingredient": '4', "instruction": '3', 'category': 'Lunch', 'rating': '4'}
        recipe_dic3 ={"id":'99',"name": "cake", "ingredient": '4', "instruction": '-4', 'category': 'Lunch', 'rating': '4'}

        self.assertNotIn(recipe_dic1, final_data)
        self.assertNotIn(recipe_dic2, final_data)
        self.assertNotIn(recipe_dic3, final_data)
    @patch('builtins.input', side_effect=['70', '4', '','71', '4', '3','72', '4', 'dessert','33', '4', '-5'])
    def test_editRecipe_category(self, mock_editRecipe):
        management = main.RecipeManagmentSystem()
        r1 = main.Recipe("70", "Ice Cream", 'milk, sugar', 'blend together', 'Lunch', '2')
        r2 = main.Recipe("71", "Ice Cream", 'milk,honey,sugar', 'blend together', 'Lunch', '2')
        r3 = main.Recipe("72", "Ice Cream", 'milk,honey,sugar', 'blend together', 'Lunch', '2')
        r4 = main.Recipe("33", "Ice Cream", 'milk,honey,sugar', 'blend together', 'Lunch', '2')

        with patch('builtins.print'):  # to avoid unwanted prints during the test
            management.addRecipe(r1)
            management.addRecipe(r2)
            management.addRecipe(r3)
            management.addRecipe(r4)

        with patch('builtins.print'):  # to avoid unwanted prints during the test
            management.editRecipe('70')
            management.editRecipe('71')
            management.editRecipe('72')
            management.editRecipe('33')

        allrecipes = management.collection.get()
        final_data = [doc.to_dict() for doc in allrecipes]

        recipe_dic1 ={"id":'70',"name": "cake", "ingredient": 'honey,milk', "instruction": '', 'category': '', 'rating': '4'}
        recipe_dic2 ={"id":'71',"name": "cake", "ingredient": '4', "instruction": '3', 'category': '3', 'rating': '4'}
        recipe_dic3 ={"id":'72',"name": "cake", "ingredient": '4', "instruction": '3', 'category': 'dessert', 'rating': '4'}
        recipe_dic4 ={"id":'33',"name": "cake", "ingredient": '4', "instruction": '3', 'category': '-5', 'rating': '4'}

        self.assertNotIn(recipe_dic1, final_data)
        self.assertNotIn(recipe_dic2, final_data)
        self.assertNotIn(recipe_dic3, final_data)
        self.assertNotIn(recipe_dic4, final_data)

if __name__ =='__main__':
    unittest.main()
