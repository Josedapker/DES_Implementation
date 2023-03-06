# Implementation of DES by Jose Jaramillo & Marco Rojas

### Assignment 2: Modern Aspects of Cryptography (FAU)

This is a Python app that implements the Data Encryption Standard (DES) algorithm, which is a symmetric-key block cipher used to encrypt and decrypt data. 

#Example

![Alt text](/Users/jose/CryptographyAssignment2/Example.jpg "Example")




# Functions

The generate_keys() function is used to generate 16 round keys used in the DES algorithm. The input to this function is the original encryption key, which is a 64-bit string, and the output is a list of 16 48-bit round keys. The key generation process involves permuting the original key using the PC-1 and PC-2 tables, dividing the permuted key into two halves, and then rotating and permuting the halves to generate the 16 round keys.

The encrypt() function takes the plain text to be encrypted and the round keys as inputs and outputs the encrypted text. The encryption process involves permuting the plain text using the initial permutation table (IP table), dividing the permuted text into two halves, and then performing 16 rounds of substitution and permutation using the round keys generated by the generate_keys() function. Finally, the encrypted text is permuted using the inverse of the IP table to generate the final cipher text.

The pad_plaintext() takes the plaintext and pads it with a specified padding character until its length is a multiple of 8 bytes (64 bits). If the plaintext is already a multiple of 8 bytes, it returns the plaintext as is.

The pad_key() function takes the key and pads it with the same padding character until its length is a multiple of 8 bytes. If the key is already a multiple of 8 bytes, it returns the key as is.

The encrypt_text() function takes the padded plaintext and the round keys, and encrypts the plaintext using DES. It does this by chunking the plaintext into 64-bit blocks and encrypting each block using the encrypt() function, which is not included in this code snippet. The encrypted blocks are concatenated together to form the final encrypted text. The encrypted blocks are concatenated together to form the final encrypted text.

