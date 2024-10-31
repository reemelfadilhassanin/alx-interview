# UTF-8 Validation

This project implements a method to determine if a given dataset represents a valid UTF-8 encoding. It checks whether the byte sequences adhere to the UTF-8 encoding standards.

## Requirements

- Python 3.4.3 or later
- Ubuntu 20.04 LTS or similar

## Files

- `0-validate_utf8.py`: Contains the implementation of the `validUTF8(data)` function.
- `0-main.py`: A main file for testing the functionality of the `validUTF8` function.

## Functionality

### `validUTF8(data)`

- **Parameters**: 
  - `data` (list): A list of integers, where each integer represents a byte of data.
  
- **Returns**: 
  - `True` if the data is a valid UTF-8 encoding.
  - `False` otherwise.

### UTF-8 Encoding Rules

1. **Single-byte characters**: Represented by a byte in the range 0-127.
2. **Two-byte characters**: First byte starts with `110`, followed by a byte that starts with `10`.
3. **Three-byte characters**: First byte starts with `1110`, followed by two bytes that start with `10`.
4. **Four-byte characters**: First byte starts with `11110`, followed by three bytes that start with `10`.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository
