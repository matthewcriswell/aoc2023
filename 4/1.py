# with open('test.txt', 'r') as file:
with open("input.txt", "r") as file:
    lines = [line for line in file]

wip_lines = []
for line in lines:
    wip_lines.append(line.split(":")[1].strip())

cleaned_lines = []
for line in wip_lines:
    winning_nums = line.split("|")[0]
    my_nums = line.split("|")[1]
    winning_nums = winning_nums.split()
    my_nums = my_nums.split()
    cleaned_lines.append((winning_nums, my_nums))


def calc_points(winning_nums):
    result = 0
    if len(winning_nums) == 0:
        return 0
    if len(winning_nums) == 1:
        return 1

    result += 1
    double_points = len(winning_nums) - 1
    for _ in range(double_points):
        result = result * 2

    return result


# result = []
total = []
for card in cleaned_lines:
    winning_nums = set(card[0]) & set(card[1])
    points = calc_points(winning_nums)
    total.append(points)

print(f"{sum(total)}")
