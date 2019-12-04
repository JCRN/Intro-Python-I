"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""


# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE


def open_file(file, file_use):
    f = open(file, file_use)
    if file_use == 'r':
        for line in f:
            print(line, end='')
    else:
        t = input('\n\ninput some text: ')
        f.write(t)
        f.close()


open_file('foo.txt', 'r')

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

open_file('bar.txt', 'w')

open_file('bar.txt', 'r')
