import pysnooper
from math import prod

# filename = 'test.txt'
filename = "input.txt"
with open(filename, "r") as file:
    lines = file.readlines()

races = dict()
times = list()
distanes = list()
lines = [line.strip().split() for line in lines]

# for entry in lines[0]:
#     times = [int(time) for time in entry[1:]]
times = [int(time) for time in lines[0][1:]]

# for entry in lines[1]:
#     distances = [int(distance) for distance in entry[:1]]
distances = [int(distance) for distance in lines[1][1:]]

for x in range(len(times)):
    races[x] = {"time": times[x], "distance": distances[x]}


def calculate_distances(max_time):
    output = list()
    for i in range(max_time):
        accel_time = i
        travel_time = max_time - accel_time
        travel_distance = travel_time * accel_time
        output.append(travel_distance)
    return output


def check_ways_to_win(races):
    output = list()
    for race in races:
        possible_outcomes = calculate_distances(races[race]["time"])
        output.append(
            len([outcome for outcome in possible_outcomes if outcome > races[race]["distance"]])
        )
    return output


print(f"{prod(check_ways_to_win(races))}")
