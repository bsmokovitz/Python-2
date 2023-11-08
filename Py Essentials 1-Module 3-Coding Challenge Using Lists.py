import random as r

player1 = []
player2 = []

for i in range(20):
    player1.append(r.randint(1,13))
    player2.append(r.randint(1,13))

print("Player 1's hand: ", player1)
print("Player 2's hand: ", player2)

rounds = 0
while rounds < 20 and len(player1) > 0 and len(player2) > 0:
    rounds += 1
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    print("Player 1's card: ", card1)
    print("Player 2's card: ", card2)
    if card1 > card2:
        player1.append(card1)
        player1.append(card2)
        print("Player 1 wins round ", rounds)
    elif card2 > card1:
        player2.append(card1)
        player2.append(card2)
        print("Player 2 wins round ", rounds)
    else:
        player1.insert(10, card1)
        player2.insert(10, card2)
        print("Round ", rounds, " is a tie")

print("Player 1's hand: ", player1)
print("Player 2's hand: ", player2)

if len(player1) > len(player2):
    print("Player 1 wins with ", len(player1), " cards!")
elif len(player2) > len(player1):
    print("Player 2 wins with ", len(player2), " cards!")
else:
    print("It's a tie!")