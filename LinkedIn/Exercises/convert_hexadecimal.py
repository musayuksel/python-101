# Converting Hexadecimal to Decimal
# Hexadecimal or "base 16" uses all of the numbers 0 - 9, plus a few others to signify higher numbers:

# A = 10

# B = 11

# C = 12

# D = 13

# E = 14

# F = 15

# Therefore, the number 'D' in hexadecimal would be 13 in decimal.

# The number '1A' in hexadecimal would be 26 in decimal. Just like we have the "tens" place in base 10, hexadecimal has the "sixteens" place. So 1A would be 16 + 10 or 26.

# And just like decimal has the "hundreds" place (because 10 * 10 is 100), hexadecimal has the "256's" place (because 16 * 16 is 256) So 'ABC' in hexadecimal is (256 * 10) + (16 * 11) + (1 * 12) or 2,748


# # Converts a string hexadecimal number into an integer decimal
# # If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    hexNumbers = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    hex_num_upper_case = hexNum.upper()
    dec_num = 0
    for i in range(len(hex_num_upper_case)):
        if hex_num_upper_case[i] in hexNumbers:
            dec_num = dec_num * 16 + hexNumbers[hex_num_upper_case[i]]
        else:
            return None
    return dec_num


print(hexToDec('1A'))  # 26
print(hexToDec('3C0'))  # 960
print(hexToDec('AA'))  # 170
print(hexToDec('ZZ'))  # None
