# with open('test.txt', 'r') as infile:
with open("input.txt", "r") as infile:
    lines = [line.strip() for line in infile]


counters = list()
game_num = 1
for game in [line.split(";") for line in [line.split(":")[1].strip() for line in lines]]:
    play_dicts = list()
    for play in game:
        lst = play.strip().split()
        play_result_dict = {}
        for i in range(0, len(lst), 2):
            key = lst[i + 1].rstrip(",")  # Remove any trailing commas
            value = int(lst[i])  # Convert string to integer
            play_result_dict[key] = value
        play_dicts.append(play_result_dict)
        result_dict = dict()
        for play_dict in play_dicts:
            for item in play_dict:
                if item in result_dict:
                    if play_dict[item] >= result_dict[item]:
                        result_dict[item] = play_dict[item]
                else:
                    result_dict[item] = play_dict[item]
    counters.append([game_num, result_dict])
    game_num += 1

final_result = 0
for game in counters:
    if game[1]["red"] <= 12 and game[1]["green"] <= 13 and game[1]["blue"] <= 14:
        final_result += game[0]

print(final_result)
