def make_sandwich(*ingredients):
    """Returning the information about the sandwiches"""
    print(f"\nPlease, enjoy your sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"  -{ingredient}")
    print("Bon appetit!")


make_sandwich('cheese', 'tomato', 'papper')
make_sandwich('prosciutto', 'basilic', 'egg')
make_sandwich('sausage', 'olives')
