#!/usr/bin/env python3.6
from password import User

def create_credential(acc_name,acc_password):
    '''
    Function to create a new credential
    '''

    new_credential = User(acc_name,acc_password)
    return new_credential

def save_credentials(credential):
    '''
    Function to save a credential
    '''
    credential.save_credential()

def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credetial()

def find_credential(account_name):
    '''
    Function that finds a credential by account name and returns the credential
    '''
    return User.find_by_account_name(account_name)

