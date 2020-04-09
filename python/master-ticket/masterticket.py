TICKET_PRICE = 10

tickets_remaining = 100


# Run this code continuously until we run out of tickets
while tickets_remaining >= 1:
    # TODO: Output how many tickets are remaining using the tickets_remaining
    # variable.
    print("There are {} tickets remaining.".format(tickets_remaining))

    # TODO: Gather user's name and assign it to new variable.
    name = input("What is your name?  ")

    # TODO: prompt user by name and ask how many tickets they would like
    total_tickets = int(input(
        "Hello {}, how many tickets would you like?  ".format(name)))

    # TODO: Calculate the price (# tickets * price) and assign it to variable
    total_price = total_tickets*TICKET_PRICE

    # TODO: Output price to screen
    print("Your total is ${}.".format(total_price))

    # TODO: prompt user if they want to proceed. Y/N?
    proceed = input("Confirm purchase (Y/N). ")
    proceed = proceed.upper()
    # TODO: If they want to proceed:
    #   print out to screen "SOLD!" to confirm purchase
    #   and then decrement the tickets remaining by the number of tickets
    #   purchased.
    if proceed == "Y":
        tickets_remaining -= total_tickets
        print("SOLD! {} tickets remaining.".format(tickets_remaining))
    else:
        # TODO: Else: thank them by name
        print("Thank you {}.".format(name))

# Notify user that the tickets are sold out
print("Sorry, we're all sold out!")
