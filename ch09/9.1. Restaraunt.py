class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f"The restaurant {self.restaurant_name} is open!")


restaurant = Restaurant('Chifood', 'asian')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print("\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()
