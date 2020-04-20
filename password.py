import pyperclip

class User:
    '''
    A class that generates new instaces of passwords
    '''
    
    credential_list = [] #Empty credentials list

    def __init__(self,account_name,account_password):
        
        #docstring removed for simplicity
        
        self.account_name = account_name
        self.account_password = account_password

    def save_credential(self):
        '''
        save_credential method saves credential objects into credentials list
        '''

        User.credential_list.append(self)

    def delete_credential(self):
        '''
        delete_credential method deletes credentials from the crdentials_list
        '''

        User.credential_list.remove(self)

    @classmethod
    def credential_exist(cls,account_name):
        '''
        Method that checks if a credential exixst from the credential_list
        Args:
            account_name: Account name to search if it exists
        Returns:
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return True
            
        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credential_list

    @classmethod
    def find_by_account_name(cls,account_name):
        '''
        Method that takes in an account name and returns a credential that matches that account name
        Args:
            account_name: Account name to search for
        Returns:
            A credential that matches the account name.
        '''

        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def copy_password(cls,account_name):
        password_found = User.find_by_account_name(account_name)
        pyperclip.copy(password_found.account_password)