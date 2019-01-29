#CLASS CREDENTIALS
class Credentials:
    """
    Class that generates new instances of contacts.
    """

    credentials_list = [] # Empty contact list

    def save_credential(self):

        '''
        save_contact method saves contact objects into credentials_list
        '''

        Credentials.credentials_list.append(self)

    def delete_credential(self):

        '''
        delete_contact method deletes a saved contact from the credentials_list
        '''

        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    def __init__(self,first_name,last_name,user_name,number,email,password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.phone_number = number
        self.email = email
        self.password = password
