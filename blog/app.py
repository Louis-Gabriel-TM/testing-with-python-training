MENU_PROMPT = "Enter 'c' to create a blog, 'l' to list post, 'r' to read one, 'p' to create a post and 'q' to quit: "

blogs = dict()


def menu():
    # Show the user the available blogs
    print_blogs()

    # Let the user make a choice
    selection = input(MENU_PROMPT)

    # Do something with that choice

    # Eventually exit


def print_blogs():
    for key, blog in blogs.items():
        print(f"- {blog}")
