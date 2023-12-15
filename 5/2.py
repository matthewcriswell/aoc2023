import pysnooper


# @pysnooper.snoop()
def read_file(filename):
    with open(filename, "r") as file:
        maps_hash = dict()
        in_map = False
        for line in file:
            for words in line.split():
                # if not in_map:
                if "map" in words:
                    in_map = True
                    # map_list = list()
                    map_header = line.split()[0].strip()
                    if map_header in maps_hash.keys():
                        pass
                    else:
                        maps_hash[map_header] = list()
                    break
                else:
                    if len(line) == 0:
                        in_map = False
                        break

            if in_map == True:
                line_entry = [
                    int(entry) for entry in line.strip().strip("\n").split(" ") if entry.isdigit()
                ]
                if len(line_entry) >= 3:
                    maps_hash[map_header].append(tuple(line_entry))
    return maps_hash


def read_seeds(filename):
    with open(filename, "r") as file:
        seeds = list()
        raw_input = file.readline()
        raw_seeds = raw_input.strip().split(":")[1]
        seeds = [int(seed) for seed in raw_seeds.strip().split()]
        return seeds


# @pysnooper.snoop()
def make_hash(input_tuples, input_value, forward=True):
    if forward is True:
        for dest_start_range, source_start_range, range_length in input_tuples:
            if (
                input_value >= source_start_range
                and input_value <= source_start_range + range_length
            ):
                return abs(input_value - source_start_range) + dest_start_range
    else:
        for dest_start_range, source_start_range, range_length in input_tuples:
            if input_value >= dest_start_range and input_value <= dest_start_range + range_length:
                return abs(input_value - dest_start_range) + source_start_range
    return input_value


def prep_seed_list(seeds):
    i = 0
    output = list()
    while i < len(seeds) - 1:
        output.append(tuple([seeds[i], seeds[i + 1]]))
        i += 2
    return output


def valid_seed(seed_list, i):
    # print(f'seed tuples: {seed_list}')
    for start_val, range_val in seed_list:
        if i >= start_val and i < start_val + range_val:
            return True
    return False


infile = "input.txt"
seeds = read_seeds(infile)
seed_list = prep_seed_list(seeds)
hash_test_input = read_file(infile)
output_list = list()
for i in range(100000, 9999999999):
    output = i
    for map_header in reversed(hash_test_input.keys()):
        output = make_hash(hash_test_input[map_header], output, forward=False)
    if valid_seed(seed_list, output):
        # print(f'{output} is a seed with location {i}')
        output_list.append(i)
        break

print(f"{min(output_list)}")
