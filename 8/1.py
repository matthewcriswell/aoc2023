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

ops_gen = seq_iter(ops_list)
counter = 1
current = "AAA"
op = next(ops_gen)
while nodes[current][op] != "ZZZ":
    if nodes[current][op] == "ZZZ":
        break
    current = nodes[current][op]
    op = next(ops_gen)
    counter += 1

print(f"{counter}")
