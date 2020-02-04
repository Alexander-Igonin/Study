from random import shuffle
import random


class Card:
    suites = ['червей', 'пики', 'треф', 'бубей']
    values = [None, None, None, None, None, None, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def suites_check(self, c2):
        if self.suit == c2.suit:
            return True
        else:
            return False

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        return False

    def __repr__(self):
        card = str(self.values[self.value]) + ' ' + self.suites[self.suit]
        return card

class Deck:
    def __init__(self):
        self.deck = []
        for i in range(6, 15):
            for j in range(4):
                self.deck.append(Card(i, j))
        shuffle(self.deck)

    def take_card(self):
        if len(self.deck) == 0:
            return
        return self.deck.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.card = []
        self.move_point = 0


class Game:
    def __init__(self):
        self.player1 = Player('Crusher.bot')
        self.player2 = Player('Space_AI')
        self.deck = Deck()
        self.suits = Card.suites
        self.power_suit = random.choice(self.suits)
        self.cards = self.deck.deck

    def first_move(self):
        p1_card = self.min_cards_value(self.power_suits_deck(self.player1))
        p2_card = self.min_cards_value(self.power_suits_deck(self.player2))
        if self.player1.card[p1_card] < self.player2.card[p2_card]:
            self.player2.move_point += 1
        else:
            self.player1.move_point += 1

    def power_suits_deck(self, player):
        lst = []
        for i in range(len(player.card)):
            if player.card[i][1] == self.power_suit:
                lst.append(player.card[i])
        return lst

    def move(self, player, player_card):
        print(f'{player.name} ходит {player.card[player_card]}')
    

    def card_on_deck(self, player,  player_card):
        return player.card.pop(player_card)

    def take(self, player):
        print(f'{player} берет карту')
        player.card.append(self.deck.take_card())

    def give_cards(self, deck):
        while len(self.player1.card) < 6:
            self.player1.card.append(deck.pop())
        while len(self.player2.card) < 6:
            self.player2.card.append(deck.pop())

    def min_cards_value(self, player_deck):
        while True:
            lst = []
            for i in range(len(player_deck)):
                lst.append(player_deck[i][0])
            x = lst.index(min(lst))
            if player_deck[x][1] == self.power_suit:
                continue
            return x

    def move_turn(self):
        if self.player1.move_point > self.player2.move_point:
            return self.player2
        return self.player1

    def move_counter_turn(self):
        if self.player1.move_point < self.player2.move_point:
            return self.player2
        return self.player1


    def play_game(self):
        self.give_cards(self.cards)
        while len(self.player1.card) > 0 and len(self.player2.card) > 0 and len(self.cards) > 0:
            self.first_move()
            self.move(self.move_turn(), self.min_cards_value(self.move_turn().card))
            cart_on_deck = self.card_on_deck(self.move_turn(), self.min_cards_value(self.move_turn().card))



