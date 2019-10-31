MENU_PROMPT = "Enter 'c' to create a blog, 'l' to list post, 'r' to read one, 'p' to create a post and 'q' to quit: "
POST_TEMPLATE = """
--- {} ---

{}
"""

blogs = dict()


def menu():
    # Show the user the available blogs
    print_blogs()

    # Let the user make a choice
    selection = input(MENU_PROMPT)

    # Do something with that choice
    while selection != 'q':
        if selection =='c':
            ask_creat_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()

        selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():
        print(f"- {blog}")

def ask_create_blog():
    title = input("Enter your blog title: ")
    author = input("Enter your name: ")

    blogs[title] = Blog(title, author)

def ask_read_blog():
    title = input("Enter the blog title you want to read: ")

    print(blogs[titles])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    pass
