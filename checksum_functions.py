# CS 1 Lab Assignment 5
# create functions to find the checksum of a plaintext file, encrypt it with checksum, and decrypt it with a checksum
# author Ian Marx, date 5 March 2016

# import the encryption and decryption functions
from encryption_functions import *
from decryption_functions import *


def skip_line(in_file):
    while True:
        c = in_file.read(1)    # read over the first line (the pad)
        if c == "\n":
            break


def find_checksum(plaintext_file_name, block_size):

    block = plaintext_file_name.read(block_size)      # assign a block of text of size block_size
    checksum = 0

    while len(block) > 0:
        checksum_block = 0

        for i in range(len(block)):                   # for each block of text, we find the checksum of each character,
            checksum_part = ord(block[i]) * i         # multiply the ASCII character value of each char by its index
            checksum_block += checksum_part           # add the character's value to a block's checksum value
        checksum += checksum_block                    # add the block's value to the total checksum
        block = plaintext_file_name.read(block_size)  # increment the block you're reading

    return checksum


def decrypt_checksum(checksum_file, d, n):

    checksum = ""                    # create an empty string
    while True:
        c = checksum_file.read(1)
        if c == "\n":                # if we find a new line character,
            break                    # break out of the function and avoid appending it
        else:
            checksum += c            # not a newline, so append
    decrypted_checksum = modular_exponentiation(int(checksum), d, n)    # decrypt the checksum with mod_exp
    return decrypted_checksum


def checksum_encryption(plaintext_file_name, ciphertext_file_name, e, n, block_size):

    in_file = open(plaintext_file_name, "r")                # open plaintext for reading
    out_file = open(ciphertext_file_name, "wb")             # open a new file for writing cipher-text

    pad = generate_pad(block_size)                          # generate a random pad
    pad_long = string_to_long(pad)                          # turn it into a long int
    encrypted_pad = modular_exponentiation(pad_long, e, n)  # encrypt it with modular exponentiation

    checksum = find_checksum(in_file, block_size)                   # find the checksum
    encrypted_checksum = modular_exponentiation(checksum, e, n)     # encrypt the checksum

    # write the pad and a newline character into the new file
    out_file.write(str(encrypted_pad) + "\n")
    out_file.write(str(encrypted_checksum) + "\n")

    in_file.close()
    in_file = open(plaintext_file_name, "r")

    block = in_file.read(block_size)                        # assign a block of text of size block_size
    while len(block) > 0:
        encrypted_line = xor_block(pad, block)              # xor each block w/ the pad to encrypt
        out_file.write(encrypted_line)
        block = in_file.read(block_size)                    # increment the block of text

    # close both files
    in_file.close()
    out_file.close()


def checksum_decryption(ciphertext_file_name, decrypted_file_name, checksum_file, d, n, block_size, pad=None, checksum=None):

    in_file = open(ciphertext_file_name, "rb")  # open the cipher-text file for decryption
    out_file = open(decrypted_file_name, "wb")  # open a new file to write plaintext

    if not pad:  # if no pad is provided, decrypt the pad in the file
        pad = decrypt_pad(in_file, d, n, block_size)

    if not checksum:
        checksum = decrypt_checksum(in_file, d, n)

    out_file.write("The checksum should be: " + str(checksum) + ". Look at other file to check." + "\n" + "\n")

    block = in_file.read(block_size)            # read through the cipher-text block_size bytes at a time
    while len(block) > 0:                       # while there is text to decrypt,
        decrypted_line = xor_block(pad, block)  # xor the block with the decrypted pad
        out_file.write(decrypted_line)
        block = in_file.read(block_size)        # increment the block of text

    # close both files
    in_file.close()
    out_file.close()

    out_file = open(decrypted_file_name, "rb")  # reopen the plaintext file we just closed

    skip_line(out_file)
    skip_line(out_file)

    end_checksum = find_checksum(out_file, block_size)       # calculate the checksum of the just-decrypted plaintext
    checksum_out_file = open(checksum_file, "wb")
    checksum_out_file.write("The checksum is: " + str(end_checksum) + ".")   # write the checksum into a new file

    # close both files
    out_file.close()
    checksum_out_file.close()
