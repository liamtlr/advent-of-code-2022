with open('input_data.txt', 'r') as infile:
    input_data: list = infile.read().splitlines()
    elves = []
    current_elf = 0
    for datum in input_data:
        if not datum:
            elves.append(current_elf)
            current_elf = 0
            continue
        current = int(datum)
        current_elf += current
    else:
        elves.append(current_elf)

print(sum(sorted(elves)[:-4:-1]))
