places = ["Saint Helena iceland", "New Zealand", "Easter island", "Machu picchu"]
print("\nOriginal list:")
print(places)

print("\nTemporary sorted list:")
print(sorted(places))

print("\nTemporary reversed sorted list:")
print(sorted(places, reverse=True))

print("\nOriginal list again:")
print(places)

print("\nusing reversed method:")
places.reverse()
print(places)

print("\nusing reversed method again:")
places.reverse()
print(places)

print("\nusing sort method back again:")
places.sort()
print(places)

print("\nusing reversed sort method back again:")
places.sort(reverse=True)
print(places)