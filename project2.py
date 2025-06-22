# Simple Bus Ticket Booking

bus_fare = 100  # Fixed fare for any route
total_seats = 20
booked_seats = 0

print("Welcome to Simple Bus Ticket System!\n")

while booked_seats < total_seats:
    name = input("Enter your name: ")
    seats = int(input("How many seats do you want to book? "))

    if booked_seats + seats <= total_seats:
        cost = seats * bus_fare
        print(f"Booking successful for {name}!")
        print(f"Total cost: ₹{cost}")
        print("Payment received. Enjoy your trip!\n")
        booked_seats += seats
    else:
        print("Sorry, not enough seats available.\n")

    cont = input("Book another ticket? (yes/no): ")
    if cont.lower() != "yes":
        break

print("Thank you for using our system!")
