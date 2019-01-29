#!/usr/bin/env python3.6

from credentials import Credentials
from user_details import User

def create_credentials(fname,lname,uname,phone,email,password):
    '''
    Function to create a new credentials
    '''
    new_credentials = Credentials(fname,lname,uname,phone,email,password)
    return new_credentials

def save_credential(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credential()

def delete_credential(credentials):
    '''
    Function to delete a credential
    '''
    credentilas.delete_credential()

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def main():
    print("Hello Welcome to your credentials list. What is your name?")
    user_name = input()

    print(f"Welcome {user_name}. \n what would you like to do?")
    print('\n')

    while True:
            print("Use these short codes : cc - create a new credentials, dc - display credentials, ex -exit the credentials list ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("New Credential")
                    print("-"*10)

                    print ("First name ....")
                    f_name = input()

                    print("Last name ...")
                    l_name = input()

                    print("user name ...")
                    u_name = input()

                    print("Phone number ...")
                    p_number = input()

                    print("Email address ...")
                    e_address = input()

                    print("password ...")
                    password = input()


                    save_credential(create_credentials(f_name,l_name,u_name,p_number,e_address,password))
                    print ('\n')
                    print(f"New Credential {f_name} {l_name} created")
                    print ('\n')

            # elif short_code == 'dc':
            #
            #         if display_credentials():
            #                 print("Here is a list of all your credentials")
            #                 print('\n')
            #
            #                 for credentials in display_credentials():
            #                      print(f"first name: {credentials.first_name}\n\nlast name: {credentials.last_name}\n\nuser name: {credentials.user_name}\n\nphone number: {credentials.phone_number}\n\nemail: {credentials.email}\n\nyour password: {credentials.password}")
            #
            #                 print('\n')
            #         else:
            #                 print('\n')
            #                 print("You dont seem to have any credentials saved yet")
            #                 print('\n')
            #
            #
            #
            # elif short_code == "ex":
            #                 print("Thank you for using password locker")
            #                 break
            #
            # else:
            #                 print("INVALID!! Please use the short codes provided")

if __name__ == '__main__':
    main()
