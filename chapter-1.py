# Task 1 - Print a poem

print('''Jack and Jill went up the hill
To fetch a pail of water;
Jack fell down and broke his crown,
and Jill came tumbling after.

Up Jack got, and home did trot,
As fast as he could caper,
To old Dame Dob, who patched his nob
With vinegar and brown paper. ''')


# Task 2 - Use pip to install pyjokes module. 
# print A Joke

import pyjokes

joke = pyjokes.get_joke()
print(joke)


# Task 3 - Write a python program to print the contents 
# of a directory using os module

import os

# Specify the path 
directory_path = "./"

# List all the files in the path
contents = os.listdir(directory_path)

# Print the items/folder/files names in the path
for item in contents:
    print(item)