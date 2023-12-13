from dataclasses import dataclass, field

# import pysnooper


@dataclass
class Card:
    card: int
    matched: int


def read_file(file):
    with open(file, "r") as file:
        lines = [line for line in file]

    wip_lines = []
    for line in lines:
        wip_lines.append(line.split(":")[1].strip())
    result = []
    for x, line in enumerate(wip_lines, 1):
        winning_nums = line.split("|")[0]
        my_nums = line.split("|")[1]
        winning_nums = winning_nums.split()
        my_nums = my_nums.split()
        result.append((x, len(set(winning_nums) & set(my_nums))))
    return result


original_list = list()
# for line in read_file('test.txt'):
for line in read_file("input.txt"):
    original_list.append(Card(*line))

new_cards = []


# @pysnooper.snoop()
def calculate_total_cards(cards, index=0):
    card = cards[index]
    total = 1
    new_cards.append(card)

    if card.matched > 0:
        cid = index + 1 + card.matched
        for next_index in range(index + 1, cid):
            total += calculate_total_cards(cards, next_index)
    return total


for i in range(len(original_list)):
    calculate_total_cards(original_list, i)


print(f"{len(new_cards)}")
