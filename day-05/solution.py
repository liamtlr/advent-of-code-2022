from collections import deque
import re

with open('input_data.txt', 'r') as infile:
    input_data: list = infile.read().splitlines()
    splitter = input_data.index('')
    crates, commands = input_data[:splitter], input_data[splitter + 1:]

    num_stacks = int(crates.pop()[-1])
    CHARS_BETWEEN_CRATE = 4
    column_indexes = list(range(1, num_stacks * CHARS_BETWEEN_CRATE, CHARS_BETWEEN_CRATE))
    crates_by_stack = []
    for index in column_indexes:
        stack = []
        for row in crates:
            try:
                crate = row[index]
                if crate != ' ':
                    stack.append(crate)
            except IndexError:
                pass
        crates_by_stack.append(deque(stack))

    commands = [
        re.findall(r'\d+', command)
        for command in commands
    ]
    for command in commands:
        num_crates, source, destination = command
        num_crates, source, destination = int(num_crates), int(source) - 1, int(destination) - 1
        for _ in range(num_crates):
            crate = crates_by_stack[source].popleft()
            crates_by_stack[destination].appendleft(crate)
    tops = [stack[0] for stack in crates_by_stack]

    print(''.join(tops))
