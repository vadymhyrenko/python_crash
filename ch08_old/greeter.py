def greet():
    """Display a simple greeting."""
    print("Hello, world!")


greet()


def greet_user(username):  # username is the parameter here
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


greet_user('jesus')  # Jesus is an argument here
