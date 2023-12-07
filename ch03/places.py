places = ["Machu Pikchu", "Village", "Saint Helen Island", "Alabama"]
print("Original list")
print(places)
print("\nSorted list:")
print(sorted(places))
print("\nSorted in reverse order:")
print(sorted(places, reverse=True))
print("\nOriginal list:")
print(places)

places.reverse()
print("\nReverted list:")
print(places)

places.reverse()
print("\n Again reverted list:")
print(places)

places.sort()
print("\n Sorted list:")
print(places)

places.sort(reverse=True)
print("\n Sorted backward list:")
print(places)

places_number = len(places)
print(f"\nSo, the total number of places to be visited is: {places_number}")