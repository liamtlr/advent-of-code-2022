
with open('input_data.txt', 'r') as infile:
    input_data: list = infile.read().splitlines()

contained_count = 0

for pair in input_data:
    elf_1, elf_2 = pair.split(',')
    elf_1_start, elf_1_end = elf_1.split('-')
    elf_2_start, elf_2_end = elf_2.split('-')
    elf_1_start = int(elf_1_start)
    elf_1_end = int(elf_1_end)
    elf_2_start = int(elf_2_start)
    elf_2_end = int(elf_2_end)

    if elf_1_start <= elf_2_start and elf_1_end >= elf_2_end:
        contained_count += 1
    elif elf_2_start <= elf_1_start and elf_2_end >= elf_1_end:
        contained_count += 1

print(contained_count)
