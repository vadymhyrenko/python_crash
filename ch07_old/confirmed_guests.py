unconfirmed_guests = ['viggo', 'silvio', 'tony', 'lucy', 'viggo', 'susan', 'viggo']
confirmed_guests = []

while unconfirmed_guests:
    while 'viggo' in unconfirmed_guests:
        unconfirmed_guests.remove('viggo')

    unconfirmed_guest = unconfirmed_guests.pop()
    confirmed_guests.append(unconfirmed_guest)

print("The following guests confirmed their arrival:")
for confirmed_guest in confirmed_guests:
    print(f" - {confirmed_guest.title()}")
