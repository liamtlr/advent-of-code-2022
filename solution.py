import string


with open('input_data.txt', 'r') as infile:
    input_data: list = infile.read().splitlines()

score = 0
for rucksack in input_data:
    compartment_size = int(len(rucksack) / 2)

    compartment_1, compartment_2 = rucksack[:compartment_size], rucksack[compartment_size:]
    common = list(set(compartment_1).intersection(compartment_2))[0]
    letter_index = string.ascii_lowercase.index(common.lower()) + 1
    if common.isupper():
        letter_index = letter_index + len(string.ascii_lowercase)
    score += letter_index

print(score)

