print("Hello! Welcome to new line remover :)\n")

filename = input('Please tell me the name of your assignment file: ')

# get new file name
dot = 0
while (filename[dot] != '.'):
    dot += 1
newfilename = filename[:dot] + "-1" + filename[dot:]

fd = open(filename, 'r')
newfd = open(newfilename, 'w')

count = 1   # used for count the number of lines and indexing
curIndex = 0

for line in fd:
    if count % 2 == 1: # odd number, which is an index number line
        curIndex = eval(line)
    else:              # even number, which is a title line
        newfd.write(str(curIndex) + ' ' + line)

    count += 1

fd.close()
newfd.close()

print("\nCongratulation! The new line removal has completed!")
print("Bye-bye~")


