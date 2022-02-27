import config as cf
import random

from .deck import Deck


class Game(cf.WindowHandler):
    def __init__(self, w_destination, w_width, w_height, w_bg):
        super().__init__(w_destination, w_width, w_height, w_bg)
        self.turn_conter = 0
        self.cards_char = cf.CARDS_CHARACTERS
        self.cards_num = cf.CARDS_NUM
        self.deck_of_cards = []
        self.shuffled_cards = []
        # Deal cards
        self.deal_card_x = self.w_width - 250
        self.deal_card_y = (110, 550)
        # First turn
        self.first_turn_x = 100
        self.first_turn_y = self.w_height / 2
        # Second turn
        self.second_turn_x = 595
        self.second_turn_y = self.first_turn_y
        # Final turn
        self.final_turn_x = 770
        self.final_turn_y = self.first_turn_y
        # Showdown
        self.showdown_x = self.deal_card_x
        self.showdown_y = self.deal_card_y[0]

    def shuffle_deck(self):
        self.deck = Deck(self.canvas, cf.SAVE_FILE_PATH)
        for char in range(4):
            for num in range(13):
                self.deck_of_cards.append(
                    (self.cards_num[num], self.cards_char[char])
                )
        for _ in range(9):
            selected_card = random.choice(self.deck_of_cards)
            self.shuffled_cards.append(selected_card)
            self.deck_of_cards.remove(selected_card)

    def restart(self):
        self.turn_conter = 0
        self.deck_of_cards = []
        self.shuffled_cards = []
        self.shuffle_deck()

    def deal_cards(self):
        if self.turn_conter == 0:
            for i in range(2):
                self.deck.draw_cart_back(
                    self.deal_card_x + i * 160, self.deal_card_y[0]
                )
                self.deck.draw_cart_face(
                    self.deal_card_x + i * 160,
                    self.deal_card_y[1],
                    (self.shuffled_cards[i][0], self.shuffled_cards[i][1]),
                )

            for i in range(3):
                self.deck.draw_cart_back(
                    self.first_turn_x + i * 160, self.first_turn_y
                )
            self.deck.draw_cart_back(self.second_turn_x, self.second_turn_y)
            self.deck.draw_cart_back(self.final_turn_x, self.final_turn_y)
            self.turn_conter += 1

    def first_turn(self):
        if self.turn_conter == 1:
            for i in range(3):
                self.deck.draw_cart_face(
                    self.first_turn_x + i * 160,
                    self.first_turn_y,
                    (
                        self.shuffled_cards[i + 2][0],
                        self.shuffled_cards[i + 2][1],
                    ),
                )
            self.turn_conter += 1

    def second_turn(self):
        if self.turn_conter == 2:
            self.deck.draw_cart_face(
                self.second_turn_x,
                self.second_turn_y,
                (self.shuffled_cards[5][0], self.shuffled_cards[5][1]),
            )
            self.turn_conter += 1

    def final_turn(self):
        if self.turn_conter == 3:
            self.deck.draw_cart_face(
                self.final_turn_x,
                self.final_turn_y,
                (self.shuffled_cards[6][0], self.shuffled_cards[6][1]),
            )
            self.turn_conter += 1

    def showdown(self):
        if self.turn_conter == 4:
            for i in range(2):
                self.deck.draw_cart_face(
                    self.showdown_x + i * 160,
                    self.showdown_y,
                    (
                        self.shuffled_cards[i + 7][0],
                        self.shuffled_cards[i + 7][1],
                    ),
                )
            self.turn_conter += 1
