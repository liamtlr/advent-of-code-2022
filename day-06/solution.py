with open('input_data.txt', 'r') as infile:
    input_data: list = infile.read().splitlines()[0]

    value = None

    PACKET_SIZE = 14

    for i in range(PACKET_SIZE, len(input_data)):
        checker = set(input_data[i-PACKET_SIZE:i])
        if len(checker) == PACKET_SIZE:
            value = i
            break

    print(value)
