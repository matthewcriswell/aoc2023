from dataclasses import dataclass


@dataclass
class Symbol:
    symbol: str
    row: int
    col: int

    @property
    def width(self):
        return 1

    @property
    def spots_on_grid(self):
        return (self.row, self.col)

    @property
    def surround_on_grid(self):
        return [
            (self.row + 1, self.col),
            (self.row + 1, self.col + 1),
            (self.row + 1, self.col - 1),
            (self.row - 1, self.col),
            (self.row - 1, self.col - 1),
            (self.row - 1, self.col + 1),
            (self.row, self.col - 1),
            (self.row, self.col + 1),
        ]


@dataclass
class Number:
    value: int
    row: int
    col: int

    @property
    def width(self):
        return len(str(self.value))

    @property
    def spots_on_grid(self):
        return [(self.row, self.col + i) for i in range(self.width)]


@dataclass
class Grid:
    rows: int
    cols: int
    grid: list = None
    numbers: list = None
    symbols: list = None

    def __post_init__(self):
        self.grid = [["." for _ in range(self.cols)] for _ in range(self.rows)]
        self.numbers = []
        self.symbols = []

    def add_symbol(self, symbol: Symbol):
        self.grid[symbol.row][symbol.col] = symbol.symbol
        self.symbols.append(symbol)

    def add_number(self, number: Number):
        num_str = str(number.value)
        for i in range(number.width):
            self.grid[number.row][i + number.col] = num_str[i]
        self.numbers.append(number)

    def remove_number(self, number: Number):
        for i in range(number.width):
            self.grid[number.row][number.col + i] = "."
        self.numbers.remove(number)

    def print_grid(self):
        for row in self.grid:
            print("".join(row))


with open("input.txt", "r") as infile:
    # with open("test.txt", "r") as infile:
    lines = [line.strip() for line in infile]

rows = len(lines)
cols = len(lines[0])

import parse_grid

grid = Grid(rows, cols)

nums_on_grid = parse_grid.parse_grid()
syms_on_grid = parse_grid.parse_grid(symbols=True)

for entry in nums_on_grid:
    grid.add_number(Number(*entry))

for entry in syms_on_grid:
    grid.add_symbol(Symbol(*entry))

grid.print_grid()

hot_numbers = []
gear_syms = []
for symbol in grid.symbols:
    close_nums = []
    if symbol.symbol == "*":
        for number in reversed(grid.numbers):
            if set(symbol.surround_on_grid) & set(number.spots_on_grid):
                close_nums.append(number)
                grid.remove_number(number)
                hot_numbers.append(number)

    if len(close_nums) == 2:
        gear_syms.append((symbol, close_nums))

grid.print_grid()


import operator

gear_sum = 0
for gear in gear_syms:
    gear_sum += operator.mul(*[num.value for num in gear[1]])

print(gear_sum)
