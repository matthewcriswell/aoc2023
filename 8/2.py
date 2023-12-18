# import pysnooper
from math import lcm

filename = "input.txt"


def seq_iter(my_list):
    while True:
        for item in my_list:
            yield item


with open(filename, "r") as file:
    ops = file.readline().strip()
    ops_list = [char for char in ops]
    lines = file.readlines()
    lines = [line.strip().split() for line in lines if line != "\n"]

nodes = dict()
for line in lines:
    directions = dict()
    self_node = line[0]
    directions["self"] = self_node
    directions["L"] = line[2].strip("(),")
    directions["R"] = line[3].strip("(),")
    nodes[self_node] = directions


def resolve_steps(nodes, start_entry, ops_list):
    ops_gen = seq_iter(ops_list)
    counter = 1
    current = start_entry
    op = next(ops_gen)
    while nodes[current][op][2] != "Z":
        current = nodes[current][op]
        op = next(ops_gen)
        counter += 1
    return counter


# @pysnooper.snoop()
def main(nodes, ops_list):
    a_vals = dict()
    for a_val in [node for node in nodes if node[2] == "A"]:
        a_vals[a_val] = a_val

    z_scores = list()
    for a_val in a_vals:
        test_val = a_vals[a_val]
        z_scores.append(resolve_steps(nodes, test_val, ops_list))

    print(f"{lcm(*z_scores)}")


main(nodes, ops_list)
