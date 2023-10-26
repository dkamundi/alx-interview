#!/usr/bin/python3


def validUTF8(data):
    # Initialize a variable to keep track of the number of expected following bytes
    following_bytes = 0


    # Iterate through the data list
    for byte in data:
        # Check if the current byte is a continuation byte
        if following_bytes > 0:
            # If it's not in the form "10xxxxxx," return False
            if (byte & 0b11000000) != 0b10000000:
                return False
            following_bytes -= 1
        else:
            # Determine the number of following bytes based on the leading bits
            if (byte & 0b10000000) == 0:
                following_bytes = 0
            elif (byte & 0b11100000) == 0b11000000:
                following_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:
                following_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:
                following_byte = 3
            else:
                # If it doesn't start with valid UTF-8 leading bits, return False
                return False
    # If there are remaining expected following bytes, return False
    if following_bytes > 0:
        return False

    return True
