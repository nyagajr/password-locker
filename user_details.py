#USER CLASS
class User:
    """
    generates new user details
    """
    user_details = []

    def save_user(self):

        '''
        save_user method saves user objects into user_details
        '''

        User.user_details.append(self)

    # def delete_user(self):
    #
    #     '''
    #     delete_credentials method deletes a saved credentials from the credentials_list
    #     '''
    #
    #     User.user_details.remove(self)

    @classmethod
    def display_user(cls):
        '''
        class method that returns the user details
        '''
        return cls.user_details

    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password
