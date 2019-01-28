#USER CLASS
class User:
    """
   generates new user details
    """

   user_details = []

    def __init__(self,user_name,password):

        self.user_name = user_name
        self.password = password
