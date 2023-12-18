with open("input.txt", "r") as file:
    lines = [line.strip().split() for line in file]


def get_diff(line):
    return [int(j) - int(i) for i, j in zip(line[:-1], line[1:])]


results = list()
for line in lines:
    diff_line = get_diff(line)
    result = diff_line[-1]
    while len([entry for entry in diff_line if entry != 0]) != 0:
        if len(diff_line) > 0:
            diff_line = get_diff(diff_line)
            result += diff_line[-1]
        else:
            result += diff_line[0]
    results.append(result + int(line[-1]))

print(f"{sum(results)}")
