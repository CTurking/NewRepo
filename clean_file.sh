#!/bin/bash
#
## define the input file name
input_file="preproinsulin-seq.txt"

 read the input file into a variable
 input_contents=$(< "$input_file")

 # define the regular expression pattern to match ORIGIN, its numbers, slashes, spaces, and line breaks
 pattern="ORIGIN[[:space:]]+[[:digit:]]+[[:space:]]*//"

 # remove the matched pattern from the input contents using sed
 clean_contents=$(echo "$input_contents" | sed -E "s/$pattern//g; s/[[:space:]]+//g")

 # check if the resulting file has 110 characters
 if [[ ${#clean_contents} -eq 110 ]]; then
     echo "File has 110 characters."
     else
         echo "File does not have 110 characters."
         fi

         # write the clean contents to an output file
         echo "$clean_contents" > "output_file_sh.txt"





