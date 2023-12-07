guests = ["John", "Vanessa","Silvio", "Walter"]

print(guests[0] + ", please, come at 7 pm, and you " + guests[1] + " please come at 7.30 pm. " + guests[2] +
      " please come earlier to help with the garden.")

print("I just found out that " + guests[3] + " won't come.")
guests[3] = "Sally"
print(guests[3] + ", would you be so kind to join to the dinner tomorrow?")
guests.insert(0, "Robert")
guests.insert(2, "Cris")
guests.append("Proctor")
print(guests)