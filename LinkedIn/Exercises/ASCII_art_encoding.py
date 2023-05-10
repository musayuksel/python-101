# Write a function "encodeString" that will encode a string like 'AAAAABBBBAAA' as a list of tuples: [('A', 5), ('B', 4), ('A', 3)] meaning that the string has "5 A's, followed by 4 B's, followed by 3 A's"

# Then use that function to compress a string containing "ASCII Art" (https://en.wikipedia.org/wiki/ASCII_art)

# Write a corresponding function "decodeString" that will take in a list of tuples and print the original string.

def encodeString(stringVal):
    encoded_list = []
    prev_char = stringVal[0]
    char_count = 0
    for char in stringVal:
        if char == prev_char:
            char_count += 1
        else:
            # print(prev_char, char_count)
            encoded_list.append((prev_char, char_count))
            prev_char = char
            char_count = 1
    # print(prev_char, char_count)
    encoded_list.append((prev_char, char_count))
    return encoded_list


encoded_list = encodeString("AAAAABBBBAAA")
print(encoded_list)


def decodeString(encodedList):
    decoded_string = ""
    for letter,letter_count in encodedList:
        decoded_string += letter * letter_count
    return decoded_string

print(decodeString(encoded_list))