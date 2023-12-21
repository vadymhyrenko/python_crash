#dimensions = (100, 50)
# print(dimensions)
# print(dimensions[0])
# print(dimensions[1])
#
# for dimension in dimensions:
#     print(dimension)
# dimensions[0] = 120 # an error is expected here

dishes = ("rise", "grechka", "proso", "pshono")
print("You can choose from the following menu items:")
for dish in dishes:
  print(f"- {dish}")

dishes = ("carrot", "tomato", "proso", "pshono")
print("Our meny has changed, now you can choose a dish from the following items:")
for dish in dishes:
    print(f"- {dish}")