# - our parking garage class should have the following methods:
# - takeTicket FINISHED
# - This should decrease the amount of tickets available by 1 FINISHED
# - This should decrease the amount of parkingSpaces available by 1 FINISHED
# - payForParking 
# - Display an input that waits for an amount from the user and store it in a variable FINISHED
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave FINISHED
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# By the end of this project each student should be able to:
# - Explain and/or demonstrate creating classes
# - Explain and/or demonstrate creating class methods
# - Explain and/or demonstrate class instantiation

class parkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parking_spaces = list(range(1, total_parking_spaces +1))
        self.current_ticket = {}
    
    def takeTicket(self):
        ticket = self.tickets.pop(0)
        parking_space = self.parking_spaces.pop(0)
        self.current_ticket[ticket] = { 
            "paid" : False, 
            "parking_space" : parking_space
            }
        print(f"Ticket {ticket} issued. Your parking space is {parking_space}.")

    def payForParking(self):
        ticket_number = int(input("Please enter you ticket number: "))
        if ticket_number in self.current_ticket and not self.current_ticket[ticket_number]["paid"]:
            payment = input("Please enter payment amount: ")
            if payment:
                self.current_ticket[ticket_number]["paid"] = True
                print("Thank you, you have 15 minutes to leave.")
            else:
                print("Please Try again.")
    def leaveGarage(self):
        ticket_number = int(input("Please enter you ticket number: "))
        if ticket_number in self.current_ticket:
            if self.current_ticket[ticket_number]["paid"]:
                print("Thank you, Come again soon!")
                self.parking_spaces.append(self.current_ticket[ticket_number]["parking_space"])
                self.tickets.append(ticket_number)
                del self.current_ticket[ticket_number]
            else:
                print("Please pay before leaving.")
        else:
            print("Please Try again.")

open = True
garage = parkingGarage(total_tickets=100, total_parking_spaces=100)

while open:
    print("\nOptions:")
    print("If you need a ticket, please press '1'")
    print("If you would like to pay for parking, please press '2'")
    print("If you are trying to leave, please press '3'")
    print("If you are trying to quit, please press '4'")
    choice = input("Enter your choice: ")


    

    if choice == "1":
        garage.takeTicket()
    if choice == "2":
        garage.payForParking()
    if choice == "3":
        garage.leaveGarage()
    if choice == "4":
        break


