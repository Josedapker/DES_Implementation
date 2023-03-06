import math
## Array to hold the 16 keys
round_keys = [''] * 16

## String to hold the plain text
pt = ""

## Function to convert a number in decimal to binary
def convertDecimalToBinary(decimal):
    binary = ""
    while decimal != 0:
        binary = ("1" if decimal % 2 != 0 else "0") + binary
        decimal //= 2
    while len(binary) < 4:
        binary = "0" + binary
    return binary

## Function to convert a number in binary to decimal
def convertBinaryToDecimal(binary):
    decimal = 0
    counter = 0
    size = len(binary)
    for i in range(size-1, -1, -1):
        if binary[i] == "1":
            decimal += int(math.pow(2, counter))
        counter += 1
    return decimal

## Function to compute xor between two strings
def Xor(a, b):
    result = ""
    size = len(b)
    for i in range(size):
        if a[i] != b[i]:
            result += "1"
        else:
            result += "0"
    return result

## Function to do a circular left shift by 1
def shift_left_once(key_chunk):
    shifted = key_chunk[1:] + key_chunk[0]
    return shifted

# Function to do a circular left shift by 2
def shift_left_twice(key_chunk):
    shifted = key_chunk
    for i in range(2):
        shifted = shifted[1:] + shifted[0]
    return shifted

## Function to generate the 16 keys
def generate_keys(key):
    ## PC-1 permutation
    pc1 = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4,
    ]
    ## PC-2 permutation
    pc2 = [
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32,
    ]
    ## Compressing the key using the PC1 table
    perm_key = ''
    for i in range(56):
        perm_key += key[pc1[i]-1]

    ## Dividing the result into two equal halves
    left = perm_key[:28]
    right = perm_key[28:]

    ## Generating 16 keys
    for i in range(16):
        ## For rounds 1, 2, 9, 16 the key_chunks are shifted by one.
        if i == 0 or i == 1 or i == 8 or i == 15:
            left = shift_left_once(left)
            right = shift_left_once(right)
        ## For other rounds, the key_chunks are shifted by two.
        else:
            left = shift_left_twice(left)
            right = shift_left_twice(right)

        ## The chunks are combined
        combined_key = left + right
        round_key = ''
        ## Finally, the PC2 table is used to transpose the key bits
        for j in range(48):
            round_key += combined_key[pc2[j]-1]
        round_keys[i] = round_key


def encrypt(pt, round_keys):

    def DES():
        ## IP Table
        initial_permutation = [
            58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7,
        ]
        ## IP-1 Table
        inverse_permutation = [
            40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25,
        ]
        ## Expansion Function Table
        expansion_table = [
            32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1,
        ]
        ## Permutation Table
        permutation_tab = [
            16, 7, 20, 21, 29, 12, 28, 17,
            1, 15, 23, 26, 5, 18, 31, 10,
            2, 8, 24, 14, 32, 27, 3, 9,
            19, 13, 30, 6, 22, 11, 4, 25,
        ]
        ## Substitution Boxes
        substitution_boxes = [
            ## S1
            [
                [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
            ],
            ## S2
            [
                [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
            ],
            ## S3
            [
                [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
            ],
            ## S4
            [
                [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
            ],
            ## S5
            [
                [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
            ],
            ## S6
            [
                [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
            ],
            ## S7
            [
                [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
            ],
            ## S8
            [
                [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
            ]]

        ## Applying the initial permutation
        perm = ""
        for i in range(64):
            perm += pt[initial_permutation[i]-1]
        # print("Initial Permutation: ", perm)

        ## Dividing the result into two equal halves
        left = perm[:32]
        right = perm[32:]
        #print("left:",left)
        #print("right:",right)

        ## The plain text is encrypted 16 times
        for i in range(16):

            ## The right half of the plain text is expanded
            right_expanded = ""
            for j in range(48):
                right_expanded += right[expansion_table[j]-1]
            # print("Right expanded:", right_expanded)

            ## The result is xored with a key
            xored = Xor(round_keys[i], right_expanded)
            #print("xored",xored)

            ## The result is divided into 8 equal parts and passed
            ## through 8 substitution boxes. After passing through a
            ## substituion box, each box is reduces from 6 to 4 bits.
            res = ""
            for j in range(8):
                # Finding row and column indices to lookup the
                # substituition box
                row1 = xored[j*6] + xored[j*6 + 5]
                row = convertBinaryToDecimal(row1)
                col1 = xored[j*6 + 1] + xored[j*6 + 2] + \
                xored[j*6 + 3] + xored[j*6 + 4]
                col = convertBinaryToDecimal(col1)
                # print("row1",row1)
                # print("row",row)
                # print("col1: ", col1)
                # print("col",col)
                val = substitution_boxes[j][row][col]
                res += convertDecimalToBinary(val)
                # print("Val: ", val)
                # print("res: ", res)

            # 3.5. Another permutation is applied
            perm2 = ""
            for j in range(32):
                perm2 += res[permutation_tab[j]-1]

            # 3.6. The result is xored with the left half
            xored = Xor(perm2, left)

            # 3.7. The left and the right parts of the plain text are swapped
            left = xored
            if i < 15:
                temp = right
                right = xored
                left = temp
        # print("right_expanded ",right_expanded)

    # 4. The halves of the plain text are applied
        combined_text = left + right
        ciphertext = ""

    # The inverse of the initial permuttaion is applied
        for i in range(64):
            ciphertext += combined_text[inverse_permutation[i]-1]
            # And we finally get the cipher text
        # print("ciphertext:",ciphertext)
        return ciphertext

    return DES()


def pad_plaintext(plaintext):
    padding = "!@#$%^&*"
    # Check if plaintext is already a multiple of 8 bytes
    if len(plaintext) % 8 == 0:
        return plaintext

    # Calculate the number of padding bytes required
    padding_bytes = 8 - len(plaintext) % 8
    #print("padding bytes: ", padding_bytes)

    # If plaintext is already a multiple of 8 bytes, pad with 8 bytes
    if padding_bytes == 0:
        padding_bytes = 8
    # Create padding bytes filled with the value of the number of padding bytes

    # padding = bytes([padding_bytes] * padding_bytes)
    padding_text = padding[0:padding_bytes]
    #print("padding_text:", padding_text)

    # Concatenate plaintext and padding
    padded_plaintext = plaintext + padding_text
    return padded_plaintext


def pad_key(key):
    padding = "!@#$%^&*"
    # Check if key is already a multiple of 8 bytes
    if len(key) % 8 == 0:
        return key

    # Calculate the number of padding bytes required
    padding_bytes = 8 - len(key) % 8

    # If key is already a multiple of 8 bytes, pad with 8 bytes
    if padding_bytes == 0:
        padding_bytes = 8

    # Create padding bytes filled with the value of the number of padding bytes
    padding_key = padding[0:padding_bytes]

    # Concatenate key and padding
    padded_key = key + padding_key
    return padded_key


def encrypt_text(pt, round_keys):
    
    ## loop 8 characters at a time
    start = 0
    finish = 64
    chunk_size = 64
    num_chunks = len(pt) // chunk_size 
    encrypted_text = ""
    for i in range(num_chunks):
        #Chunk the plaintext
        pt_chunk = pt[start:finish]
        #print("pt_chunks: ", pt_chunk)
        encrypted_text = encrypted_text + encrypt(pt_chunk, round_keys)
        start=finish
        finish=finish+chunk_size
    return encrypted_text


## main function
def main():

    print("DES Implementation App\n\nBy: Jose Jaramillo & Marco Rojas\n\n")
    while True:
        ## Prompt user to enter yes or no answer
        choice = input("Would you like to encrypt or decrypt?\n")

        ## Check if answer is encrpyt or decrypt
        if choice.lower() == "encrypt":
            plaintext = input("Please enter the plaintext you would like to encrypt: \n")
            key = input("Please enter the secret key: \n")

            padded_plaintext = pad_plaintext(plaintext)
            padded_key = pad_key(key)
            
            # Convert plaintext to ASCII
            ascii_plaintext = [ord(c) for c in padded_plaintext]
            # Convert key to ASCII
            ascii_key = [ord(c) for c in padded_key]

            # Convert each ASCII code to binary
            binary_plaintext = [bin(c)[2:].zfill(8) for c in ascii_plaintext]
            binary_key = [bin(c)[2:].zfill(8) for c in ascii_key]

            ## Join the binary codes together into a single string
            binary_plaintext_string = "".join(binary_plaintext)
            #print("Binary Plaintext:", binary_plaintext_string)
            binary_key_string = "".join(binary_key)

            #print("Padded Plaintext:", padded_plaintext)
            #print("Padded Key:",padded_key)
        
            ## Calling the function to generate 16 keys
            generate_keys(binary_key_string)

            ## Applying the algorithm
            ciphertext = encrypt_text(binary_plaintext_string, round_keys)
            print("Cipher text:", ciphertext)
        
        elif choice.lower() == "decrypt":

                ciphertext = input("Please enter the ciphertext you would like to decrypt: \n")
                binary_key_string = input("Please enter the secret key: \n")
                generate_keys(binary_key_string)

                ## Reversing the round_keys array for decryption
                i = 15
                j = 0
                while i > j:
                    temp = round_keys[i]
                    round_keys[i] = round_keys[j]
                    round_keys[j] = temp
                    i -= 1
                    j += 1

                decrypted = encrypt_text(ciphertext, round_keys)
                print("Decrypted text:", decrypted)
                print("Binary Plaintext:", binary_plaintext_string)

                ## Comparing the initial plain text with the decrypted text
                if decrypted == binary_plaintext_string:
                    print("Plain text encrypted and decrypted successfully. :-)")
                    print("Plaintext:", plaintext)
                else:
                    print("Plain text encrypted and decrypted unsuccessfully :-(")
                break
                
        else:
                print("Invalid input. Please enter 'encrypt' or 'decrypt'.")
        
        
        ## Ask user if they want to decrypt ciphertext
        while True:
            ## Prompt user to enter yes or no answer
            answer = input("Do you want to decrypt your ciphertext? (yes or no): ")

            ## Check if answer is yes or no
            if answer.lower() == "yes":
            
                ## Reversing the round_keys array for decryption
                i = 15
                j = 0
                while i > j:
                    temp = round_keys[i]
                    round_keys[i] = round_keys[j]
                    round_keys[j] = temp
                    i -= 1
                    j += 1

                plaintext = ciphertext
                decrypted = encrypt_text(plaintext, round_keys)
                print("Decrypted text:", decrypted)
                print("Binary Plaintext:", binary_plaintext_string)

                ## Comparing the initial plain text with the decrypted text
                if decrypted == binary_plaintext_string:
                    print("Plain text encrypted and decrypted successfully. :-)")
                else:
                    print("Plain text encrypted and decrypted unsuccessfully :-(")
                break

            elif answer.lower() == "no":
                print("Exiting program...")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        break
main()
