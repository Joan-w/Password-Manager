import unittest #Importing the unittest module
from password import User #Importing the User class

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines the cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_credential = User("Instagram", "12345") #Create a new credential
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.account_name,"Instagram")
        self.assertEqual(self.new_credential.password,"12345")

if __name__ = "__main__"
unittest.main()