import unittest
from user_details import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.user_details = User("jimmy","jim123")


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''


        self.assertEqual(self.user_details.user_name,"jimmy")
        self.assertEqual(self.user_details.password,"jim123")

    def test_save_user(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credentials list
        '''
        self.user_details.save_user() # saving the new credentials
        self.assertEqual(len(User.user_details),1)

    
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_details = []

# saving multiple users
    def test_save_multiple_user(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our user_details
            '''
            self.user_details.save_user()
            test_user = User("jimmy","jim123") # new credentials
            test_user.save_user()
            self.assertEqual(len(User.user_details),2)



    def test_display_user(self):
        '''
        method that returns a list of all user saved
        '''

        self.assertEqual(User.display_user(),User.user_details)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()

if __name__ ==  '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
