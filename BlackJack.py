import random

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
values = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

card_values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
               "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

def create_deck():
    deck = []
    for suit in suits:
        for value in values:
            deck.append(f"{value} of {suit}")
    random.shuffle(deck)
    return deck

def hand_value(hand):
    value = 0
    aces = 0

    for card in hand:
        rank = card.split()[0]
        value += card_values[rank]
        if rank == 'Ace':
            aces += 1
    while aces > 0 and value > 21:
        value -= 10
        aces -= 1
    
    return value

def display_hand(hand):
    for card in hand:
        print(card)

deck = create_deck()
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

player_value = hand_value(player_hand)

print(f"\nYour hand (Total Value: {player_value}):")
display_hand(player_hand)
print("\nDealer's hand:")
print(dealer_hand[0])
print("Hidden Card")

playing = True

while playing:
    player_value = hand_value(player_hand)
    if player_value == 21:
        print("Congratulation! You win!")
        break
    elif player_value > 21:
        print("You busted, better luck next time.")
        break
    
    action = input("Do you want to hit, stand or double down?  ").lower()

    if action == 'hit':
        new_card = deck.pop()
        player_hand.append(new_card)
        new_hand_value = hand_value(player_hand)
        print(f"\nYour hand (Total Value: {new_hand_value}):")
        display_hand(player_hand)

    elif action == "stand":
        break

    elif action == "double down":
        new_card = deck.pop()
        player_hand.append(new_card)
        new_hand_value = hand_value(player_hand)
        print(f"\nYour hand (Total Value: {new_hand_value}):")
        display_hand(player_hand)
        break

print("\nDealer's turn:")
print("\nDealer's hand:")
display_hand(dealer_hand)
while hand_value(dealer_hand) < 17:
    dealer_hand.append(deck.pop())
    new_hand_value = hand_value(dealer_hand)
    print(f"\nDealer's hand (Total Value: {new_hand_value}):")
    display_hand(dealer_hand)

dealer_value = hand_value(dealer_hand)

if dealer_value > 21:
    print("\nDealer busts! you win")
elif dealer_value > player_value:
    print("\nDealer wins! ")
elif dealer_value < player_value:
    print("\nYou win!")
elif dealer_value == player_value:
    print("\nPush! It's a tie!")