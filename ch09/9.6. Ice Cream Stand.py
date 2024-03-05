class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f"The restaurant {self.restaurant_name} is open!")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type='ice_cream'):
        """Initialize an ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def describe_flavors(self):
        """Display the flavors available."""
        print(f"The following flavors are available: {self.flavors}")
        for flavor in self.flavors:
            print(f"- {flavor}")


restaurant = IceCreamStand("Ice World")
restaurant.flavors = ["peanuts", "strawberry", "mellon"]

restaurant.describe_restaurant()
restaurant.describe_flavors()
