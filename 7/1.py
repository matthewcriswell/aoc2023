from dataclasses import dataclass, field
from operator import itemgetter, attrgetter
from collections import Counter
import pysnooper


@dataclass
class Card:
    rank: str

    @property
    def value(self):
        return {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
            "T": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2,
        }[self.rank]


@dataclass
class Hand:
    cards: list[Card] = field(default_factory=list)
    bid: int = field(default_factory=int)

    @property
    def strength_index(self):
        return {
            "five_of_a_kind": 6000,
            "four_of_a_kind": 5000,
            "full_house": 4000,
            "three_of_a_kind": 3000,
            "two_pair": 2000,
            "one_pair": 1000,
            "high_card": 0,
        }[self.strength]

    @property
    def strength(self):
        sorted_cards = sorted(self.cards, key=lambda card: card.value, reverse=True)
        rank_count = Counter(card.rank for card in sorted_cards)

        # five of a kind
        if 5 in rank_count.values():
            # return self.raw_score + base_scores['five_of_a_kind']
            return "five_of_a_kind"

        # four of a kind
        if 4 in rank_count.values():
            # return self.raw_score + base_scores['four_of_a_kind']
            return "four_of_a_kind"

        # full house
        if len(rank_count) == 2 and 3 in rank_count.values():
            # return self.raw_score + base_scores['full_house']
            return "full_house"

        # three of a kind
        if 3 in rank_count.values():
            # return self.raw_score + base_scores['three_of_a_kind']
            return "three_of_a_kind"

        # two pair
        if 2 in rank_count.values():
            if len([entry for entry in rank_count.values() if entry == 2]) == 2:
                # return self.raw_score + base_scores['two_pair']
                return "two_pair"

        # pair
        if 2 in rank_count.values():
            # return self.raw_score + base_scores['one_pair       ']
            return "one_pair"
        return "high_card"

    def add_card(self, card):
        self.cards.append(card)

    # @pysnooper.snoop()
    def __lt__(self, other):
        if self.strength_index < other.strength_index:
            return True
        elif self.strength_index > other.strength_index:
            return False
        for i in range(len(self.cards)):
            if self.cards[i].value < other.cards[i].value:
                return True
            if self.cards[i].value > other.cards[i].value:
                return False
        return False

    def sort_cards(self):
        self.cards = sorted(self.cards, key=lambda card: card.value, reverse=True)


filename = "input.txt"
with open(filename, "r") as file:
    lines = [line.strip().split() for line in file]


hands = {}
hands = list()
for line in lines:
    hand = Hand()
    for cards in line[0]:
        for card in cards:
            hand.add_card(Card(card))
    hand.bid = int(line[1])
    hands.append(hand)

output = 0
for x, i in enumerate([entry.bid for entry in sorted(hands)], 1):
    output += x * i

print(f"{output}")
