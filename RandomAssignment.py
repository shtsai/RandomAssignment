import random

filename = input('Please enter the file name: ')
newfilename = filename + "-assigned"

# need configuration here
names = ['A', 'B', 'C']   # names are the names of team member
length = len(names)
random.shuffle(names)

fd = open(filename, 'r')
newfd = open(newfilename, 'w')

count = 0   # used for count the number of lines and indexing

for line in fd:
    # skip the empty line
    if line.strip() == '':
        continue

    # find first empty space, assuming all the line starts with a number (or index)
    i = 0
    while (line[i] != ' '):  # i is the index of the first space
        i += 1

    # assign the task to the member and write into the new file
    newStr = line[:i] + ' ' + names[count % length] + ' ' + line[i+1:]
    newfd.write(newStr)

    count += 1

fd.close()
newfd.close()

print("Congratulation! The random assignment has completed!")
print("There are " + str(count) + " tasks in this file.")


