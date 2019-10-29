from unittest import TestCase
from unittest.mock import patch

import app
from blog import Blog


class TestApp(TestCase):

    def test_print_blogs(self):
        blog = Blog("Test", "Test Author")
        app.blogs = {'Test': blog}  # overload the 'blogs' dictionnary in 'app'

        with patch('builtins.print') as mocked_print:
            # The 'print' function is replaced by a mocked print
            app.print_blogs()
            # To check if the 'print' function has been called with the right input
            # we check if the 'mocked_print' has been call with it
            mocked_print.assert_called_with("- Blog Test by Test Author (0 post)")
            # No need to test the 'print' function itself, we know it works...
