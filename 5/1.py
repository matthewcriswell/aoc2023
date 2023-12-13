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
                    map_list = list()
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
def make_hash(input_tuples, input_list):
    output_list = list()
    for input_value in input_list:
        found = False
        for dest_start_range, source_start_range, range_length in input_tuples:
            # if input in range
            if (
                input_value >= source_start_range
                and input_value <= source_start_range + range_length
            ):
                # number in range
                output_value = abs(input_value - source_start_range) + dest_start_range
                found = True
        if not found:
            output_value = input_value
        output_list.append(output_value)
    return output_list


infile = "input.txt"
output = read_seeds(infile)
hash_test_input = read_file(infile)
for map_header in hash_test_input.keys():
    output_list = make_hash(hash_test_input[map_header], output)
    output = [entry for entry in output_list]


print(f"{min(output)}")
