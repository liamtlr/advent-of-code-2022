import re

with open('input_data.txt', 'r') as infile:
    input_data: list = infile.read().splitlines()

CHANGE_DIRECTORY = '$ cd'
GO_UP = '..'
MAX_FOLDER_SIZE = 100000
REQUIRED_SPACE = 30000000
TOTAL_SPACE = 70000000
folders = {}
breadcrumb = []

current_directory = None
current_directory_size = 0
for command in input_data:
    if command.startswith(CHANGE_DIRECTORY):
        destination_directory = command[len(CHANGE_DIRECTORY) + 1:]
        if destination_directory != GO_UP:
            if current_directory is not None:
                breadcrumb.append(current_directory)
            try:
                destination_path = f'{breadcrumb[-1]}{destination_directory}/'
            except IndexError:
                destination_path = destination_directory
            for parent in breadcrumb:
                folders[parent] += current_directory_size
            current_directory = destination_path
            current_directory_size = 0
            folders[destination_path] = current_directory_size
        else:
            folders[current_directory] += current_directory_size
            for parent in breadcrumb:
                folders[parent] += current_directory_size
            current_directory = breadcrumb.pop()
            current_directory_size = 0
    elif re.match(r'\d+', command):
        size = int(re.match(r'\d+', command).group(0))
        current_directory_size += size
else:
    folders[current_directory] += current_directory_size
    for parent in breadcrumb:
        folders[parent] += current_directory_size

total_size = folders['/']
available_space = 70000000 - total_size
space_to_free = REQUIRED_SPACE - available_space
folder_gen = (total for total in folders.values() if total >= space_to_free)

print(min(folder_gen))
