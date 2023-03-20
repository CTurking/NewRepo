"""
Your module description
"""
# define the input file name
input_file_name = 'input_file.txt'

# define the output file names
output_file_names = ['output_file1.txt', 'output_file2.txt', 'output_file3.txt', 'output_file4.txt']

# define the positions where the file should be split
positions = [100, 200, 300]

# open the input file and read its contents
with open(input_file_name, 'r') as input_file:
    input_contents = input_file.read()

# split the contents at the defined positions
split_contents = [input_contents[start:end] for start, end in zip([0] + positions, positions + [None])]

# write each split to its corresponding output file
for i, output_file_name in enumerate(output_file_names):
    with open(output_file_name, 'w') as output_file:
        output_file.write(split_contents[i])
