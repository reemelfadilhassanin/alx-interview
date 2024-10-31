#!/usr/bin/python3
"""UTF-8 Validation
"""


def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes.

    Returns:
        bool: True if data is valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for num in data:
        # Get the last 8 bits (i.e., the byte)
        byte = num & 0xFF

        if num_bytes == 0:  # New character
            if (byte >> 7) == 0b0:
                continue  # 1-byte character
            elif (byte >> 5) == 0b110:
                num_bytes = 1  # Expecting a 2-byte character
            elif (byte >> 4) == 0b1110:
                num_bytes = 2  # Expecting a 3-byte character
            elif (byte >> 3) == 0b11110:
                num_bytes = 3  # Expecting a 4-byte character
            else:
                return False  # Invalid starting byte
        else:  # Continuing a multi-byte character
            if (byte >> 6) != 0b10:
                return False  # Invalid continuation byte
            num_bytes -= 1  # Expecting more continuation bytes

    return num_bytes == 0
