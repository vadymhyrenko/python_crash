class User:
    """A class representing a user."""

    def __init__(self, first_name, last_name, age, address):
        """A method representing basic information about the user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} years old"
              f" and is living on {self.address}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"Welcome back, {self.first_name.title()}!")


user1 = User('Brandon', 'Smithers', 53, 'Victory avenue')
user1.describe_user()
user1.greet_user()


user2 = User('William', 'King', 28, 'High Road')
user2.describe_user()
user2.greet_user()
