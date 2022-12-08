

with open('input_data.txt', 'r') as infile:
    input_data = [
        [int(char) for char in row.strip()]
        for row in infile.readlines()
    ]

start_column = 1
end_column = len(input_data[0]) - 1
start_row = 1
end_row = len(input_data) - 1

def _visible_up(row_index: int, column_index: int, height: int):
    index = row_index - 1
    while index >= 0:
        current_tree = input_data[index][column_index]
        if current_tree >= height:
            return False
        index -= 1
    return True

def _visible_right(row_index: int, column_index: int, height: int):
    index = column_index + 1
    while index:
        try:
            current_tree = input_data[row_index][index]
            if current_tree >= height:
                return False
            index += 1
        except IndexError:
            return True

def _visible_left(row_index: int, column_index: int, height: int):
    index = column_index - 1
    while index >=0:
        current_tree = input_data[row_index][index]
        if current_tree >= height:
            return False
        index -= 1
    return True


def _visible_down(row_index: int, column_index: int, height: int):
    index = row_index + 1
    while index:
        try:
            current_tree = input_data[index][column_index]
            if current_tree >= height:
                return False
            index += 1
        except IndexError:
            return True

def _visible_around(row_index: int, column_index: int):
    height = input_data[row_index][column_index]
    return any([
        _visible_left(row_index, column_index, height),
        _visible_up(row_index, column_index, height),
        _visible_right(row_index, column_index, height),
        _visible_down(row_index, column_index, height),
    ])
internal_visible_trees = 0
for row in range(start_row, end_row):
    for column in range(start_column, end_column):
        tree = input_data[row][column]
        if _visible_around(row, column):
            internal_visible_trees += 1
_visible_around(3, 2)
externals = (len(input_data) * 2) + ((len(input_data[0]) - 2) * 2 )

print(externals + internal_visible_trees)
