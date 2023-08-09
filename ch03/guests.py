guests = ['oksana', 'olena', 'olga']
print("Hi, " + guests[0].title() + "! Welcome!")
print("Greetings, " + guests[1].title() + "! Hope you're fine!")
print("Ahoy, " + guests[-1].title() + "! Haven't seen you a while.")

absent_person = guests.pop(-1)
print("\nHey! Listen up, " + guests[0].title() + " and " + guests[1].title() + "! " + absent_person.title() + " just called. She's won't arrive.")
guests.insert(2, 'helga')
print("So I decided to call " + guests[2].title() + " and invite her!")

guests.insert(1, 'veroniva')
print("Okay, the bigger table is now available, so I'll invite also " + guests[1].title() + "!")
guests.append('jessica')
print("Oh my! I'm inviting also " + guests[-1].title() + "!")
del guests[-1]
del guests[-2]
print("You know what " + str(guests) + "!")
