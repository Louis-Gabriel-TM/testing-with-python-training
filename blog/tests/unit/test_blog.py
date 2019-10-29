from unittest import TestCase

from blog import Blog


class TestBlog(TestCase):

    def test_create_blog(self):
        b = Blog("Test", "Test Author")

        self.assertEqual(b.title, "Test")
        self.assertEqual(b.author, "Test Author")
        self.assertListEqual(b.posts, [])
        self.assertEqual(len(b.posts), 0)  # similar to previous assert

    def test__repr__(self):
        b1 = Blog("Test", "Test Author")
        b2 = Blog("My Day", "Rolf")

        self.assertEqual(
            b1.__repr__(), 
            "Blog Test by Test Author (0 post)"
        )
        self.assertEqual(
            b2.__repr__(), 
            "Blog My Day by Rolf (0 post)"
        )

    def test__repr__with_multiple_posts(self):
        b = Blog("Test", "Test Author")
        b.posts = ["Test post"]

        self.assertEqual(
            b.__repr__(), 
            "Blog Test by Test Author (1 post)"
        )

        b.posts.append("Another test post")

        self.assertEqual(
            b.__repr__(),
            "Blog Test by Test Author (2 posts)"
        )
