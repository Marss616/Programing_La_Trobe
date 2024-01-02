# part of AT week 6 codeing exercise
# 26 DEC 2023 - Jack Bell

class binary:
    def __init__(self, binary):
        self.binary = binary
    
    def print_8_bit_table(binary):
        for i in range(256):
            binary = "{0:b}".format(i)
            padded_binary = binary.zfill(8)
            print(padded_binary)

    def print_range_binary():
       for i in range(256):
            binary = "{0:b}".format(i)
            padded_binary = binary.zfill(8)
            binary_value = int(padded_binary, 2)
            print(binary_value)

    def print_binary_range(self, start, finish):
        for i in range(start, finish + 1):
            binary = "{0:b}".format(i)
            padded_binary = binary.zfill(8)
            print(f"{padded_binary} - {i}")

# Example usage:
start = int(input("first number: "))
finsih = int(input("second number: "))

binary.print_binary_range(self=int, start=start, finish=finsih)

