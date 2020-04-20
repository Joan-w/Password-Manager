#!/usr/bin/env python3.6
from password import User
import random

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

def check_existing_credentials(account_name):
    '''
    Function that checks if a credential exists with that account name and return a Boolean
    '''
    return User.credential_exist(account_name)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return User.display_credentials()

def copy_credential_password(account_name):
    '''
    Function that copies a credential's password to the clipboard
    '''
    return User.copy_password(account_name)


def main():
    print("Hello Welcome to your Password-Manager Application.")
    print("Time to create your account.")
    print("Enter your name....")
    user_name = input()
    print("Enter password:")
    user_password = input()
    print(f"Hello {user_name}. You've successfully logged in into your Password Manager Account. What would you like to do?")

    while True:
        print("Use these short codes: cc - create new credential, dc - display credential, fc - find credential, delc - to delete a credential, ex -exit the credential list")

        short_code = input().lower()

        if short_code == 'cc':
            print("New credential")
            print("-"*10)

            print("Account name ...")
            a_name = input()

            print("Enter password ...")
            print("Use these short password codes: gp - if you want your password to be generated for you, wp - if you want to write your own password")

            password_code = input().lower()

            if password_code == 'gp':
                print("Generating new password......")
                # new_password = random.randint(0,10)
                new_password = str()
                characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                for i in range(1,8):
                    new_password = new_password + random.choice(characters)
                    print(f"Your new password is {new_password}")
                    print(f"Your {a_name} account password is {new_password}")
            
            elif password_code == 'wp':
                print("New password:")
                new_password = input()
                print(f"Your {a_name} account password is {new_password}")

            else:
                print("I really didn't get that please use the short codes")

            # print(f"Hello {user_name}. What would you like to do?")

            save_credentials(create_credential(a_name,new_password)) #create and save a new credential
            print('\n')
            print(f"New credential {a_name} created.")
            print('\n')

        elif short_code == 'dc':

            if display_credentials():
                print("Here is a list of all your credentials")
                print('\n')

                for credential in display_credentials():
                    print(f"{credential.account_name} .......{credential.account_password}")
                    print('\n')

            else:
                print('\n')
                print("You don't seem to have any crdential saved yet")

        elif short_code == 'fc':
            print("Enter the account name you want to search for")

            search_account_name = input()
            if check_existing_credentials(search_credential):
                search_credential = find_credential(search_account_name)
                print(f"Account name - {search_credential.account_name}")
                print('-'*20)
                print(f"Account password - {search_credential.account_password}")

            else:
                print("That credential seems not to exist")

        elif short_code == 'delc':
            print("Enter the account name of the credential you wish to delete")

            credential_delete = input()
            if del_credential(credential):
                print(f"You have successfully deleted {credential.account_name} of password {credential.account_password}")
                print('\n')

            else:
                print('\n')
                print("You don't seem to have any credential with that account name")                

        elif short_code == 'ex':
            print("Byeee ........")
            break

        else:
            print("Sorry I didn't get that. Kindly use the short codes if you want to manage you passwords. Thank you")

if __name__ == '__main__':
    main()