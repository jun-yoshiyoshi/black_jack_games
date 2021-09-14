# (class Card)トランプ（suit, number）
# (class Deck)(deal=カードを配る、shuffle)
# (class Hand)手札
# * __init__
# ?player,dealer
# ?cards
# ?value
# *hit(add_card)
# *total(calc_value)
# *is_blackjack()
# *show()
# (class Game)ゲーム

from random import shuffle
from time import sleep


class Card():

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __repr__(self):
        return f'{self.suit} {self.number}'


class Deck():

    def __init__(self):
        suits = ['♠', '♡', '♦', '♧']
        numbers = [
            {"key": "A", "value": 11},
            {"key": "2", "value": 2},
            {"key": "3", "value": 3},
            {"key": "4", "value": 4},
            {"key": "5", "value": 5},
            {"key": "6", "value": 6},
            {"key": "7", "value": 7},
            {"key": "8", "value": 8},
            {"key": "9", "value": 9},
            {"key": "10", "value": 10},
            {"key": "J", "value": 10},
            {"key": "Q", "value": 10},
            {"key": "K", "value": 10},
        ]

        self.cards = []

        for suit in suits:
            for number in numbers:
                self.cards.append(Card(suit, number))

    def deal(self):
        return self.cards.pop(0)

    def shuffle(self):
        shuffle(self.cards)


class Hand():
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.total = 0

    def add_card(self, card):
        self.cards.append(card)

    def calc_value(self):
        self.value = 0
        ace = False
        for card in self.cards:
            self.value += int(card.number["value"])
            if card.number["key"] == "A":
                ace = True

        if ace and self.value > 21:
            self.value -= 10
        return self.value

    def is_blackjack(self):
        return self.calc_value() == 21

    def show(self, show_two_cards=False):
        # if self.dealer:
        #  print("Dealer hand:")
        # else:
        #  print("Your hand:")

        print(f"{'Dealer' if self.dealer else 'Your'} hand:")
        # "Dealer"はエラー。

        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_two_cards and not self.is_blackjack():
                pass
            else:
                print(f"{card.suit}{card.number['key']}")
                # ”key”ではエラー。
        # ディーラーのカードを１枚伏せる。最初のカードで、ディーラーの場合で　show_two_cardsがTrueでブラックジャックが完成していない場合。何もしない。

        if not self.dealer:
            print("Total:", self.calc_value())


class Game():
    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.calc_value() > 21:
                print("BARST.YOU LOSE.")
                return True
            elif dealer_hand.calc_value() > 21:
                print("DEALER is BARST.YOU WIN.")
                return True
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print("DRAW.")
                return True
            elif player_hand.is_blackjack():
                print("Conglatulation,Black Jack.")
                return True
            elif dealer_hand.is_blackjack():
                print(f'(ディーラーのカードは{dealer_hand.show(show_two_cards=False)}です。)')
                print("Dealer's Black Jack. YOU LOSE.")
                return True
        else:
            if player_hand.calc_value() > dealer_hand.calc_value():
                print("YOU WIN.")
            elif dealer_hand.calc_value() == player_hand.calc_value():
                print("DRAW")
            else:
                print("YOU LOSE.")
            return True
        return False

    def play(self):
        game_to_play = 0
        game_number = 0

        while game_to_play <= 0:
            try:
                game_to_play = int(input("何回プレーしますか？："))
            except ValueError:
                print("数字を入力してください。")

        while game_number < game_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal())
                dealer_hand.add_card(deck.deal())
            print('カードをディールします。')
            sleep(2)
            print(f'(ゲームの回数{game_number}/{game_to_play})')
            # /の前後にスペースを入れるとエラー
            sleep(2)
            print()

            player_hand.show()
            dealer_hand.show()

            if self.check_winner(player_hand, dealer_hand):
                continue
            else:
                pass
            print("①ヒットかスタンドの選択")

            choice = ""
            while choice not in ["s", "stand", "n", "no"] and player_hand.calc_value() < 21:
                choice = input("Hitしますか(Y/N):").lower()
                print()
                while choice not in ["y", "yes", "h", "hit", "n", "no", "s", "stand"]:
                    choice = input("Hitしますか(Y/N):").lower()
                    print()

                if choice in ["h", "hit", "y", "yes"]:
                    player_hand.add_card(deck.deal())
                    player_hand.show()

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("②ディーラーが１７までヒットする")

            while dealer_hand.calc_value() < 17:
                dealer_hand.add_card(deck.deal())
                dealer_hand.calc_value()
                dealer_hand.show(show_two_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue
            print("結果を表示する")
            print("Your Hand:", player_hand.calc_value())
            print("Dealer Hand:", dealer_hand.calc_value())

            self.check_winner(player_hand, dealer_hand, game_over=True)


game = Game()
game.play()
