SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

def calculate_price(total_tickets):
    return (total_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name?  ")
    try:
        total_tickets = int(input(
            "Hello {}, how many tickets would you like?  ".format(name)))
        if total_tickets > tickets_remaining:
            raise ValueError("Not enough tickets available. There are only {} tickets available".format(tickets_remaining))
    except ValueError as err:
        print("Error occurred! {}.".format(err))
    else:
        total_price = calculate_price(total_tickets)
        print("Your total is ${}.".format(total_price))
        proceed = input("Confirm purchase (Y/N). ")
        proceed = proceed.upper()
        if proceed == "Y":
            tickets_remaining -= total_tickets
            print("SOLD! {} tickets remaining.".format(tickets_remaining))
        else:
            print("Thank you {}.".format(name))
print("Sorry, we're all sold out!")
