import string


with open('input_data.txt', 'r') as infile:
    input_data: list = infile.read().splitlines()

score = 0
ELF_GROUP_SIZE = 3
for rucksack in range(0, len(input_data), 3):
    elf_1, elf_2, elf_3 = input_data[rucksack:rucksack + ELF_GROUP_SIZE]
    common = list(set(elf_1).intersection(set(elf_2)).intersection(elf_3))[0]
    letter_index = string.ascii_lowercase.index(common.lower()) + 1
    if common.isupper():
        letter_index = letter_index + len(string.ascii_lowercase)
    score += letter_index

print(score)
