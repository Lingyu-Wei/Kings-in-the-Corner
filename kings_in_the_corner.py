# Lingyu Wei & Brian Rivera
# CS 111 - Final Project
# 11/19

import random
class Card():

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        if 1 < self.value <= 10:
            if self.suit in "♦♥":
                return "\u001b[31m" + str(self.value) + self.suit + "\u001b[0m"
            return str(self.value) + self.suit
        if self.value == 1:
            face = "Ace"
            self.face = face
        else:
            face = ["Jack", "Queen", "King"][self.value - 11]
            self.face = face
        if self.suit in "♦♥":
            return "\u001b[31m" + face + self.suit + "\u001b[0m"
        return face + self.suit

# class KingsInCornersState():
#     def __init__(self, turn):
#         self.turn = turn
#         self.winner = self.c_winner()
#
#     def get_next_moves(self):
#         moves = []
#         if self.winner == "":
#             for i in

def check_winner(player_hand, cpu_hand):
    winner = ""
    if player_hand == []:
        print("♥ ♣ Player1 wins! ♦ ♠")
        winner = 1
        return winner
    elif cpu_hand == []:
        print("♥ ♣ Player2 wins! ♦ ♠")
        winner = 1
        return winner
    else:
        return winner

def deal(deck, player_hand, cpu_hand, normal_piles):
# randomizing deck
    for value in range(1, 14):
        for suit in ["♣" , "♦", "♠", "♥"]:
            deck.append(Card(value, suit))
    random.shuffle(deck)
# dealing 7 cards to each player
    while len(player_hand) < 7:
            if len(deck) % 2 == 0:
                cpu_hand.append(deck.pop(0))
            else:
                player_hand.append(deck.pop(0))
    normal_piles[0].append(deck.pop(0))
    normal_piles[1].append(deck.pop(0))
    normal_piles[2].append(deck.pop(0))
    normal_piles[3].append(deck.pop(0))

def take_turn(hand, normal_piles, corner_piles, pile_names, suit_colors, all_piles, normal_pile_names):
    # taking turn and checking if valid input
    move_card_or_pile = input("enter the <play> to move card from hand, <pile> to move pile on board, or <pass> to complete move:").lower()
    while move_card_or_pile != "play" and move_card_or_pile != "pile" and move_card_or_pile != "pass":
        move_card_or_pile = input("enter a valid move option:").lower()
    if move_card_or_pile == "play":
        card_move = input("choose card index 1 - " + str(len(hand)) + ":")
        if card_move == "nvm":
            take_turn(hand, normal_piles, corner_piles, pile_names, suit_colors, all_piles, normal_pile_names)
            return
        while card_move.isalpha() or int(card_move) > len(hand) or int(card_move) < 1:
            card_move = input("enter a valid card option:")
        card1 = hand[int(card_move) - 1]
        card_move2pile = input("to which pile:").upper()
        while card_move2pile not in pile_names:
            card_move2pile = input("enter a valid pile:").upper()
        if card_move2pile in normal_pile_names:
            if all_piles[0][int(card_move2pile)] == []:
                all_piles[0][int(card_move2pile)].append(hand.pop(int(card_move) - 1))
                return
            card2 = all_piles[0][int(card_move2pile)][-1]
        if card_move2pile.startswith("K"):
            if card_move2pile == "K0":
                king_pile = all_piles[1][0]
            if card_move2pile == "K1":
                king_pile = all_piles[1][1]
            if card_move2pile == "K2":
                king_pile = all_piles[1][2]
            if card_move2pile == "K3":
                king_pile = all_piles[1][3]
            if king_pile == [] and card1.face != "King":
                print("Not a valid move")
                take_turn(hand, normal_piles, corner_piles, pile_names, suit_colors, all_piles, normal_pile_names)
                return
            if king_pile == [] and card1.face == "King":
                king_pile.append(hand.pop(int(card_move) - 1))
                return
            elif king_pile != []:
                card2 = king_pile[-1]

        while not check(card1, card2, suit_colors):
            print("Not a valid move")
            take_turn(hand, normal_piles, corner_piles, pile_names, suit_colors, all_piles, normal_pile_names)
            return
        if check(card1, card2, suit_colors) and card_move2pile in normal_pile_names:
            all_piles[0][int(card_move2pile)].append(hand.pop(int(card_move) - 1))
            return
        if check(card1, card2, suit_colors) and card_move2pile.startswith("K"):
            king_pile.append(hand.pop(int(card_move) - 1))
            return


    elif move_card_or_pile == "pile":
        pile_move = input("choose pile number 0-3:")
        if pile_move == "nvm":
            take_turn(hand, normal_piles, corner_piles, pile_names, suit_colors, all_piles, normal_pile_names)
            return
        while pile_move not in normal_pile_names or normal_piles[int(pile_move)] == []:
            pile_move = input("enter a valid pile option (cannot move King Piles or empty piles):")
        card1 = normal_piles[int(pile_move)][0]

        pile_move2pile = input("to which pile:").upper()
        while pile_move2pile not in pile_names:
            pile_move2pile = input("enter a valid pile (cannot move into empty normal pile):").upper()
        if pile_move2pile in normal_pile_names:
            if normal_piles[int(pile_move2pile)] == [] and card1.face != "King":
                # inserting pile into pile
                normal_piles[int(pile_move2pile)].extend(normal_piles[int(pile_move)])
                normal_piles[int(pile_move)].clear()
                return
            card2 = normal_piles[int(pile_move2pile)][-1]

        if pile_move2pile.startswith("K"):
            if pile_move2pile == "K0":
                king_pile = all_piles[1][0]
            if pile_move2pile == "K1":
                king_pile = all_piles[1][1]
            if pile_move2pile == "K2":
                king_pile = all_piles[1][2]
            if pile_move2pile == "K3":
                king_pile = all_piles[1][3]
            if king_pile == [] and card1.face != "King":
                print("Not a valid move")
                take_turn(hand, normal_piles, corner_piles, pile_names, suit_colors, all_piles, normal_pile_names)
                return
            if king_pile == [] and card1.face == "King":
                # inserting pile into pile
                king_pile.extend(normal_piles[int(pile_move)])
                normal_piles[int(pile_move)].clear()
                return
            elif king_pile != [] and card1.face != "King":
                card2 = king_pile[-1]

        while not check(card1, card2, suit_colors):
            print("Not a valid move")
            take_turn(hand, normal_piles, corner_piles, pile_names, suit_colors, all_piles, normal_pile_names)
            return
        if check(card1, card2, suit_colors) and pile_move2pile in normal_pile_names:
            # inserting pile into pile
            normal_piles[int(pile_move2pile)].extend(normal_piles[int(pile_move)])
            normal_piles[int(pile_move)].clear()
            return
        if check(card1, card2, suit_colors) and pile_move2pile.startswith("K"):
            # inserting pile into pile
            king_pile.extend(normal_piles[int(pile_move)])
            normal_piles[int(pile_move)].clear()
            return


    elif move_card_or_pile == "pass":
        return "pass"

def draw(deck, hand):
    hand.append(deck.pop(0))
    return

def check(card1, card2, suit_colors):
    if suit_colors[card2.suit] != suit_colors[card1.suit]:
        if card2.value - card1.value == 1:
            return True
    return False

def who_starts(cpu_hand, player_hand):
    start = random.choice([1, 2])
    #CHANGE BACK, DELETE \/
    #start = 1
    if start == 1:
        hand = player_hand
    if start == 2:
        hand = cpu_hand
    return hand

def print_state(deck, normal_piles, corner_piles, player_hand, cpu_hand):
    print(len(deck), "cards in deck")
    print("")
    print("0:", normal_piles[0])
    print("1:", normal_piles[1])
    print("2:", normal_piles[2])
    print("3:", normal_piles[3])
    print("")
    print("K0:", corner_piles[0])
    print("K1:", corner_piles[1])
    print("K2:", corner_piles[2])
    print("K3:", corner_piles[3])
    print("")
    print("Player1:", player_hand)
    print("")
    #print("Player2 has " + str(len(cpu_hand)) + " cards")
    print("Player2:", cpu_hand)
    # TAKE ^ OUT IN POST
    print("")

def play():
    deck = []
    normal_piles = [[], [], [], []]
    normal_pile_names = ["0", "1", "2", "3"]
    corner_piles = [[], [], [], []]

    all_piles = [normal_piles, corner_piles]
    pile_names = ["0", "1", "2", "3", "K0", "K1", "K2", "K3"]
    player_hand = []
    cpu_hand = []

    deal(deck, player_hand, cpu_hand, normal_piles)
    suit_colors = {"♣": "black", "♦": "red", "♠": "black", "♥": "red"}

    print_state(deck, normal_piles, corner_piles, player_hand, cpu_hand)
    start_command = input("enter <start> to start the game!").lower()
    while start_command != "start":
        start_command = input("enter <start>:").lower()

    hand = who_starts(cpu_hand, player_hand)
    count = 0

    while check_winner(player_hand, cpu_hand) == "":

        while hand == player_hand:
            while count == 0:
                if deck != []:
                    draw(deck, hand)
                print_state(deck, normal_piles, corner_piles, player_hand, cpu_hand)
                plop = take_turn(hand, normal_piles, corner_piles, pile_names, suit_colors, all_piles, normal_pile_names)
                if plop == "pass":
                    hand = cpu_hand
                    count = 0
                    break
                else:
                    count += 1
            check_winner(player_hand, cpu_hand)

            while count >= 1:
                # dont draw more than you have to
                print_state(deck, normal_piles, corner_piles, player_hand, cpu_hand)
                plop = take_turn(hand, normal_piles, corner_piles, pile_names, suit_colors, all_piles, normal_pile_names)
                if plop == "pass":
                    hand = cpu_hand
                    count = 0
                    break
                else:
                    count += 1
            check_winner(player_hand, cpu_hand)

        while hand == cpu_hand:
            while count == 0:
                if deck != []:
                    draw(deck, hand)
                print_state(deck, normal_piles, corner_piles, player_hand, cpu_hand)
                plop = take_turn(hand, normal_piles, corner_piles, pile_names, suit_colors, all_piles, normal_pile_names)
                if plop == "pass":
                    hand = player_hand
                    count = 0
                    break
                else:
                    count += 1
            check_winner(player_hand, cpu_hand)

            while count >= 1:
                # dont draw more than you have to
                print_state(deck, normal_piles, corner_piles, player_hand, cpu_hand)
                plop = take_turn(hand, normal_piles, corner_piles, pile_names, suit_colors, all_piles, normal_pile_names)
                if plop == "pass":
                    hand = player_hand
                    count = 0
                    break
                else:
                    count += 1
            check_winner(player_hand, cpu_hand)

    return
play()
