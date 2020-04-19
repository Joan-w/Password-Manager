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

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        User.credentials_list = []        

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.account_name,"Instagram")
        self.assertEqual(self.new_credential.password,"12345")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saced into the credentials list
        '''

        self.new_credential.save_credential() #saving the new credential
        self.assertEqual(len(User.credentials_list),1)

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if I can save multiple credential
        objects to the credentials_list
        '''

        self.new_credential.save_credential()
        test_credential = User("Test","2345") #new credential
        test_credential.save_credential()
        self.assertEqual(len(User.credentials_list),2)

    def test_delete_credential(self):
        '''
        test_delet_credential to test if I can remove a credential from the credentials_list
        '''
        self.new_credential.save_credential()
        test_credential = User("Test","3456") #new credential
        test_credential.save_credential()

        self.new_credential.delete_credential() #Deleting a credential object
        self.assertEqual(len(User.credentials_list),1)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(User.display_credentials(),User.credentials_list)

if __name__ == "__main__":
    unittest.main()