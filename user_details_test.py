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
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.user_details.save_user() # saving the new contact
        self.assertEqual(len(User.user_details),1)

    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_details = []

# other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our user_details
            '''
            self.user_details.save_user()
            test_user = User("jimmy","jim123") # new contact
            test_user.save_user()
            self.assertEqual(len(User.user_details),2)

    # More tests above
    # def test_delete_user(self):
    #         '''
    #         test_delete_contact to test if we can remove a contact from our contact list
    #         '''
    #         self.user_details.save_user()
    #         test_user = User("jimmy","jim123") # new contact
    #         test_user.save_user()
    #
    #         self.user_details.delete_user()# Deleting a contact object
    #         self.assertEqual(len(User.user_details),1)


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
