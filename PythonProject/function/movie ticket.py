movie_name = "Kantara"
total_seats = 100
ticket_price = 200


                                                       # Function to check available seats
def check_seat_count():
    print("Available Seats:", total_seats)


                                                    # Function to book tickets
def book_ticket():
    global total_seats

    seats=45
    if seats <= 0:
        print("Please enter a valid number of tickets.")
        return 0

    elif seats > total_seats:
        print("Sorry! Only", total_seats, "seats are available.")
        return 0

    else:
        total_seats = total_seats - seats
        print("Booking Successful!")
        return seats


                                                    # Function to calculate total price
def calculate_total_price(no_of_tickets):
    return no_of_tickets * ticket_price


                                                       # Function to print final ticket
def print_ticket(no_of_tickets, total_amount):

    print("Movie Name      :", movie_name)
    print("Tickets Booked  :", no_of_tickets)
    print("Price per Ticket: ₹", ticket_price)
    print("Total Amount    : ₹", total_amount)
    print("Remaining Seats :", total_seats)


check_seat_count()

tickets = book_ticket()

if tickets > 0:
    amount = calculate_total_price(tickets)
    print_ticket(tickets, amount)
