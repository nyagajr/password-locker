import unittest # Importing the unittest module
from credentials import Credentials # Importing the credentials class

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
# Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("James","Muriuki","jimmy","0712345678","james@ms.com","jim123") # create credentials object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.first_name,"James")
        self.assertEqual(self.new_credential.last_name,"Muriuki")
        self.assertEqual(self.new_credential.user_name,"jimmy")
        self.assertEqual(self.new_credential.phone_number,"0712345678")
        self.assertEqual(self.new_credential.email,"james@ms.com")
        self.assertEqual(self.new_credential.password,"jim123")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_credential.save_credential() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)

    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []

# other test cases here
    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credential.save_credential()
            test_credentials = Credentials("James","Muriuki","jimmy","0712345678","james@ms.com","jim123") 
            test_credentials.save_credential()
            self.assertEqual(len(Credentials.credentials_list),2)


    def test_delete_credential(self):
            '''
            test_delete_credential to test if we can remove a credentials from our credentials list
            '''
            self.new_credential.save_credential()
            test_credentials = Credentials("James","Muriuki","jimmy","0712345678","james@ms.com","jim123") # new credentials
            test_credentials.save_credential()

            self.new_credential.delete_credential()# Deleting a credentials object
            self.assertEqual(len(Credentials.credentials_list),1)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()
