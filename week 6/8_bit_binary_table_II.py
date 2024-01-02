# part of AT week 6 codeing exercise
# 27 DEC 2023 - Jack Bell

start = int(input('Start: '))
stop = int(input('Stop: '))

# Create the binary conversion table, saving it to table.txt.


output = ""

for i in range(start, stop):
    binary = "{0:b}".format(i)
    output += f"{binary.zfill(8)} is {i}\n"

with open('table.txt', 'w') as file:
    file.write(output)



# Read and display the contents of the file.
table_file_readonly = open('table.txt', 'r')
print(table_file_readonly.read(), end='')