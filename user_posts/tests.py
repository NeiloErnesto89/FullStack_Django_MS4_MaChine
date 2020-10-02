from django.test import TestCase
from .models import User_Posts

# ensure to turn off PostGreSQL as it doesn't function for tests, need Sqlite3 
# (DEVELOPMENT MODE)

class PostsTests(TestCase):
    
    def test_str(self):
        test_name = User_Posts(name='user post')
        self.assertEqual(str(test_name), 'user profile')

