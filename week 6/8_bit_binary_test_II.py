output = ""

start = 5
stop = 10

for i in range(start, stop + 1):
    binary_current = "{0:b}".format(i)
    binary_next = "{0:b}".format(i + 1)
    output += f"{binary_current.zfill(8)} is {i}, next is {binary_next.zfill(8)} is {i + 1}\n"

with open('table.txt', 'w') as file:
    file.write(output)
