from unittest import TestCase
from unittest.mock import patch

import app
from blog import Blog


class TestApp(TestCase):

    def test_menu_print_prompt(self):
        with patch('builtins.input') as mocked_input:
            # The 'input' function is replaced by a mocked input
            app.menu()
            # To check if the 'input' function has been called with the right prompt
            # we check if the 'mocked_input' has been call with it
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blog(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        blog = Blog("Test", "Test Author")
        app.blogs = {'Test': blog}  # overload the 'blogs' dictionnary in 'app'

        with patch('builtins.print') as mocked_print:
            # The 'print' function is replaced by a mocked print
            app.print_blogs()
            # To check if the 'print' function has been called with the right text
            # we check if the 'mocked_print' has been call with it
            mocked_print.assert_called_with("- Blog Test by Test Author (0 post)")
            # No need to test the 'print' function itself, we know it works...