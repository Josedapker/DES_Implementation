# Implementation of DES by Jose Jaramillo & Marco Rojas

### Assignment 2: Modern Aspects of Cryptography (FAU)
This is a Python implementation of the Data Encryption Standard (DES) algorithm, which is a symmetric-key block cipher used to encrypt and decrypt data. 


## How to set up and run
1. Clone this project
2. Open this project in desired IDE
3. Make sure you have Python and appropriated packages installed
4. Run "Assignment2.py"

# Example
Example.jpg in the images repo
![Alt text](/images/Example.jpg "Example encryption and decryption")


# Functions
The generate_keys() function is used to generate 16 round keys used in the DES algorithm. The input to this function is the original encryption key, which is a 64-bit string, and the output is a list of 16 48-bit round keys. The key generation process involves permuting the original key using the PC-1 and PC-2 tables, dividing the permuted key into two halves, and then rotating and permuting the halves to generate the 16 round keys.

The encrypt() function takes the plain text to be encrypted and the round keys as inputs and outputs the encrypted text. The encryption process involves permuting the plain text using the initial permutation table (IP table), dividing the permuted text into two halves, and then performing 16 rounds of substitution and permutation using the round keys generated by the generate_keys() function. Finally, the encrypted text is permuted using the inverse of the IP table to generate the final cipher text.

The pad_plaintext() takes the plaintext and pads it with a specified padding character until its length is a multiple of 8 bytes (64 bits). If the plaintext is already a multiple of 8 bytes, it returns the plaintext as is.

The pad_key() function takes the key and pads it with the same padding character until its length is a multiple of 8 bytes. If the key is already a multiple of 8 bytes, it returns the key as is.

The encrypt_text() function takes the padded plaintext and the round keys, and encrypts the plaintext using DES. It does this by chunking the plaintext into 64-bit blocks and encrypting each block using the encrypt() function, which is not included in this code snippet. The encrypted blocks are concatenated together to form the final encrypted text. The encrypted blocks are concatenated together to form the final encrypted text.

The convertDecimalToBinary(decimal) function takes in a decimal number and converts it into a 4-bit binary string. It does this by repeatedly dividing the decimal number by 2, and appending a "1" to the binary string if the remainder is 1, and a "0" otherwise. The resulting binary string is then left-padded with zeros until it is 4 bits long.

The convertBinaryToDecimal(binary) function takes in a binary string and converts it into a decimal number. It does this by iterating over each bit of the binary string, starting from the rightmost bit. If the bit is "1", it adds 2 to the power of the current bit position to the decimal number. The resulting decimal number is returned.

The Xor(a, b) function takes in two binary strings of equal length and performs an XOR operation between them. It does this by iterating over each bit of the strings and appending a "1" to the result string if the bits at that position are different, and a "0" otherwise.

The shift_left_once(key_chunk) function takes in a binary string of length 28 and performs a circular left shift by 1. It does this by taking the first bit of the string and moving it to the end, while shifting all other bits one position to the left.

The shift_left_twice(key_chunk) function takes in a binary string of length 28 and performs a circular left shift by 2. It does this by performing the shift_left_once function twice.

