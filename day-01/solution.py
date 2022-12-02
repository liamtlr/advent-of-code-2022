
with open('input_data.txt', 'r') as infile:
    input_data: list = infile.read().splitlines()
    max_elf = 0
    current_elf = 0
    for datum in input_data:
        if not datum:
            if current_elf > max_elf:
                max_elf = current_elf
            current_elf = 0
            continue
        current = int(datum)
        current_elf += current

print(max_elf)