#!/usr/bin/env python3.6
from password import User

def create_credential(acc_name,acc_password):
    '''
    Function to create a new credential
    '''

    new_credential = User(acc_name,acc_password)
    return new_credential