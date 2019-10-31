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

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            # 'side_effect' allows to give 'mocked_input' a sequence of return values:
            mocked_input.side_effect = ("Test", "Test Author")
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get("Test"))

    def test_ask_read_blog(self):
        blog = Blog("Test", "Test Author")
        app.blogs = {'Test': blog}

        with patch('builtins.input', return_value="Test"):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.asser_called_with(blog)
    
    def test_print_posts(self):
        blog = Blog("Test", "Test Author")
        blog.create_post("Test Post", "Test Content")
        app.blogs = {'Test': blog}

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)

            mocked.print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post("Post title", "Post content")
        expected = POST_TEMPLATE.format("Post title", "Post content")

        with patch('builtins.print') as mocked_print:
            app.print_post()
            mocked_print.asser_called_with(expected)
