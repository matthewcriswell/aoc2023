import time
start_time = time.time()
with open('input.txt', 'r') as infile:
    lines = [line.strip() for line in infile]
print(lines)
result = 0
for line in lines:
    strnum = str([char for char in line if char.isnumeric()][0]) + str([char for char in line if char.isnumeric()][-1])
    result += int(strnum)

print(result)
end_time = time.time()
elapsed_time = (end_time - start_time) * 1000
print(f"Elapsed time: {elapsed_time} ms")
