class BinaryPrinter:
    def print_range_binary(self):
        for i in range(256):
            binary = "{0:b}".format(i)
            padded_binary = binary.zfill(8)
            binary_value = int(padded_binary, 2)
            print(f"{i} in binary is {padded_binary}, which as a number is {binary_value}")

# Example usage:
bp = BinaryPrinter()
bp.print_range_binary()
