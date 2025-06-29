import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def visual(self):
        # Create a visual representation of the card
        suit_symbols = {'Hearts': '♥', 'Diamonds': '♦', 'Clubs': '♣', 'Spades': '♠'}
        rank = self.rank if self.rank != '10' else 'T'  # use 'T' for 10 to maintain consistent width
        suit = suit_symbols[self.suit]
        lines = [
            '┌─────┐',
            f'|{rank:<2}   |',
            '|     |',
            f'|  {suit}  |',
            '|     |',
            f'|   {rank:>2}|',
            '└─────┘'
        ]
        return '\n'.join(lines)

class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def add_card(self, card):
        self.hand.append(card)

    def calculate_score(self):
        self.score = 0
        ace_count = 0
        for card in self.hand:
            if card.rank in ['Jack', 'Queen', 'King']:
                self.score += 10
            elif card.rank == 'Ace':
                ace_count += 1
                self.score += 11
            else:
                self.score += int(card.rank)

        while self.score > 21 and ace_count:
            self.score -= 10
            ace_count -= 1

        return self.score

    def show_hand(self):
        cards_visual = [card.visual() for card in self.hand]
        # Join visual representations side by side
        card_lines = [card.split('\n') for card in cards_visual]
        return '\n'.join([' '.join(line) for line in zip(*card_lines)])

class Dealer(Player):
    def __init__(self):
        super().__init__('Dealer')
        self.show_one_card = True

    def show_hand(self):
        if self.show_one_card:
            card_visual = self.hand[0].visual().split('\n')
            hidden_card = ['┌─────┐', '|░░░░░|', '|░░░░░|', '|░░░░░|', '|░░░░░|', '|░░░░░|', '└─────┘']
            combined = [card_visual[i] + ' ' + hidden_card[i] for i in range(len(card_visual))]
            return '\n'.join(combined)
        else:
            return super().show_hand()

class BlackjackGame:
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
        self.dealer = Dealer()

    def deal_initial_cards(self):
        for player in self.players:
            for _ in range(2):
                player.add_card(self.deck.deal())
        for _ in range(2):
            self.dealer.add_card(self.deck.deal())

    def check_for_blackjack(self, player):
        if player.calculate_score() == 21:
            return f'{player.name} has Blackjack! {player.name} wins!'
        elif self.dealer.calculate_score() == 21:
            return 'Dealer has Blackjack! Dealer wins!'
        return None

    def player_turn(self, player):
        while True:
            print(f'{player.name} hand:\n{player.show_hand()} (Score: {player.calculate_score()})')
            if player.calculate_score() > 21:
                return f'{player.name} busts! Dealer wins!'
            move = input(f'{player.name}, do you want to [H]it or [S]tand? ').lower()
            if move == 'h':
                player.add_card(self.deck.deal())
            elif move == 's':
                break
        return None

    def dealer_turn(self):
        self.dealer.show_one_card = False
        while self.dealer.calculate_score() < 17:
            self.dealer.add_card(self.deck.deal())
        print(f'Dealer hand:\n{self.dealer.show_hand()} (Score: {self.dealer.calculate_score()})')
        if self.dealer.calculate_score() > 21:
            return 'Dealer busts! Players win!'
        return None

    def determine_winner(self, player):
        if player.score > self.dealer.score:
            return f'{player.name} wins!'
        elif player.score < self.dealer.score:
            return f'Dealer wins against {player.name}!'
        else:
            return f'{player.name} ties with the Dealer!'

    def play_game(self):
        self.deal_initial_cards()
        print(f'Dealer hand:\n{self.dealer.show_hand()}')

        for player in self.players:
            print(f'{player.name} hand:\n{player.show_hand()}')
            blackjack_result = self.check_for_blackjack(player)
            if blackjack_result:
                print(blackjack_result)
                return

        for player in self.players:
            player_result = self.player_turn(player)
            if player_result:
                print(player_result)
                return

        dealer_result = self.dealer_turn()
        if dealer_result:
            print(dealer_result)
            return

        for player in self.players:
            print(self.determine_winner(player))

if __name__ == "__main__":
    player_count = int(input('Enter the number of players: '))
    player_names = [input(f'Enter the name of player {i+1}: ') for i in range(player_count)]

    while True:
        game = BlackjackGame(player_names)
        game.play_game()
        play_again = input('Do you want to play again? [Y/N]: ').lower()
        if play_again != 'y':
            break

