"""
Your module description
"""
import re

# define regular expression pattern to match ORIGIN and its numbers
pattern = r'ORIGIN\s+\d+\s*//\s*'

# open input file and read contents
with open('preproinsulin-seq.txt', 'r') as input_file:
    file_contents = input_file.read()

# remove ORIGIN, its numbers, slashes, spaces, and line breaks using regex
clean_contents = re.sub(pattern, '', file_contents)
clean_contents = re.sub(r'\s+', '', clean_contents)

# check if the resulting file has 110 characters
if len(clean_contents) == 110:
    print('File has 110 characters.')
else:
    print('File does not have 110 characters.')

# open output file and write clean contents
with open('output_file.txt', 'w') as output_file:
    output_file.write(clean_contents)
