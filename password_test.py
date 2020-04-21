import unittest #Importing the unittest module
import pyperclip
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

        User.credential_list = []        

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.account_name,"Instagram")
        self.assertEqual(self.new_credential.account_password,"12345")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saced into the credentials list
        '''

        self.new_credential.save_credential() #saving the new credential
        self.assertEqual(len(User.credential_list),1)

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if I can save multiple credential
        objects to the credential_list
        '''

        self.new_credential.save_credential()
        test_credential = User("Test","2345") #new credential
        test_credential.save_credential()
        self.assertEqual(len(User.credential_list),2)

    def test_delete_credential(self):
        '''
        test_delete to test if I can remove a credential from the credential_list
        '''
        # self.new_credential.save_credential()
        # new_credential = User("Linkedin", "3333")
        # new_credential.save_credential()
        # User.delete_credential("Linkedin")
        # self.assertEqual(len(User.credential_list),1)

        self.new_credential.save_credential()
        test_credential = User("Test","3456") #new credential
        test_credential.save_credential()

        self.new_credential.delete_credential() #Deleting a credential object
        self.assertEqual(len(User.credential_list),1)

    def test_credential_exists(self):
        '''
        test to check if we can return a boolean if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = User("LinkedIn", "0987") #new credential
        test_credential.save_credential()

        credential_exists = User.credential_exist("LinkedIn")
        
        self.assertTrue(credential_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(User.display_credentials(),User.credential_list)

    def test_find_credential_by_account_name(self):
        '''
        Test to check if we can find a credential by the account_name and display information
        '''

        self.new_credential.save_credential()
        test_credential = User("Facebook", "4567") #new credential
        test_credential.save_credential()

        found_credential = User.find_by_account_name("Facebook")

        self.assertEqual(found_credential.account_name,test_credential.account_name)

    # def test_copy_password(self):
    #     '''
    #     Test to confirm that we are copying the password from a credential
    #     '''

    #     self.new_credential.save_credential()
    #     User.copy_password("4567")

    #     self.assertEqual(self.new_credential.account_password,pyperclip.paste())

if __name__ == "__main__":
    unittest.main()