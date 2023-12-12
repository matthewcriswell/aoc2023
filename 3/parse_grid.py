# with open("test.txt", "r") as file:
with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]


# def add_number(num_str, num_len, row, col):
#     """adds a number object to the matrix representation"""
#     print(f"last number was: {num_str:4} {num_len:3} long at row: {row} and col: {col - num_len}")


def parse_grid(symbols=False):
    """parses input looking for nums"""
    results = []
    symbol_results = []
    rows = len(lines)
    cols = len(lines[0])

    i = 0

    num_token = False
    num_len = 0
    num_row = 0
    num_col = 0
    num_str = ""
    line_nums = []
    while i < rows:
        for j in range(cols):
            if not lines[i][j].isdigit():
                if num_token:
                    # add number
                    # add_number(num_str, num_len, i, j)
                    results.append((int(num_str), i, j - num_len))
                    num_len = 0
                    num_str = ""
                    num_token = False
                if lines[i][j] != ".":
                    # symbol
                    # print(f"symbol: {lines[i][j]} at {i}, {j}")
                    symbol_results.append((lines[i][j], i, j))
            else:
                if lines[i][j].isdigit():
                    num_str = "".join([num_str, lines[i][j]])
                    if num_token:
                        num_len += 1
                    elif not num_token:
                        num_token = True
                        num_row = i
                        num_col = j
                        num_len += 1
            #  else:
            #      print(f"symbol: {lines[i][j]} at {i}, {j}")
            #      if lines[i][j] != '.':
            #          # symbol
            #          print(f"symbol: {lines[i][j]} at {i}, {j}")
        # number at the end of a row
        if num_token:
            # add number
            j += 1
            # add_number(num_str, num_len, i, j)
            results.append((int(num_str), i, j - num_len))
            num_str = ""
            num_len = 0
            num_token = False
        i += 1
    if symbols:
        return symbol_results
    return results


if __name__ == "__main__":
    with open("test.txt", "r") as file:
        lines = [line.strip() for line in file]
    nums = parse_grid()
    syms = parse_grid(symbols=True)
