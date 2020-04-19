class User:
    '''
    A class that generates new instaces of passwords
    '''
    
    credentials_list = [] #Empty credentials list

    def __init__(self,account_name,account_password):
        
        #docstring removed for simplicity
        
        self.account_name = account_name
        self.password = account_password

    def save_credential(self):
        '''
        save_credential method saves credential objects into credentials list
        '''

        User.credentials_list.append(self)

    def delete_credential(self):
        '''
        delete_credential method deletes credentials from the crdentials_list
        '''

        User.credentials_list.remove(self)