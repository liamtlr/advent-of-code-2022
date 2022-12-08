from math import prod

with open('input_data.txt', 'r') as infile:
    input_data = [
        [int(char) for char in row.strip()]
        for row in infile.readlines()
    ]

start_column = 0
end_column = len(input_data[0])
start_row = 0
end_row = len(input_data)

def _visible_up(row_index: int, column_index: int, height: int):
    index = row_index - 1
    count = 0
    while index >= 0:
        current_tree = input_data[index][column_index]
        count += 1
        if current_tree >= height:
            return count
        index -= 1
    return count

def _visible_right(row_index: int, column_index: int, height: int):
    index = column_index + 1
    count = 0
    while index:
        try:
            current_tree = input_data[row_index][index]
            count += 1
            if current_tree >= height:
                return count
            index += 1
        except IndexError:
            return count

def _visible_left(row_index: int, column_index: int, height: int):
    index = column_index - 1
    count = 0
    while index >=0:
        current_tree = input_data[row_index][index]
        count += 1
        if current_tree >= height:
            return count
        index -= 1
    return count

def _visible_down(row_index: int, column_index: int, height: int):
    index = row_index + 1
    count = 0
    while index:
        try:
            current_tree = input_data[index][column_index]
            count += 1
            if current_tree >= height:
                return count
            index += 1

        except IndexError:
            return count

def _visible_around(row_index: int, column_index: int):
    height = input_data[row_index][column_index]
    return prod([
        _visible_up(row_index, column_index, height),
        _visible_left(row_index, column_index, height),
        _visible_right(row_index, column_index, height),
        _visible_down(row_index, column_index, height),
    ])

internal_visible_trees = 0
max_vista = 0
for row in range(start_row, end_row):
    for column in range(start_column, end_column):
        tree = input_data[row][column]
        vista_score = _visible_around(row, column)
        if vista_score > max_vista:
            max_vista = vista_score

print(max_vista)
