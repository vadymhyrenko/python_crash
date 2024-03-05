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


class Admin(User):
    """A class representing Admin user"""

    def __init__(self, first_name, last_name, age, address):
        """Initialize an Admin"""
        super().__init__(first_name, last_name, age, address)
        self.privileges = []

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("The admin has the following privileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")


matt = Admin("Matt", "Cluster", 33, "Queen Vitoria")
matt.privileges = ["GetObject", "DeleteObject", "PutObject"]
matt.describe_user()
matt.show_privileges()
