# CS 1 Lab Assignment 5
# write functions to decrypt a one-time pad and to decrypt cipher-text files
# author Ian Marx, date 2 March 2016

from checkpoint import *
from mod_exp import modular_exponentiation
from nonRecModXP import modXP

# define my public and secret RSA keys including e, d, and n
e_key = 5
d_key = 423373754142276580220485879021423673212098671225290325821671703647655188149692674292370093017182893
n_key = 1058434385355691450551214697553559183030246678063330795205116915534886751904144766262010692314523041
BLOCK_SIZE = 16  # define the byte size of each block of text we will decrypt


def decrypt_pad(pad_file, d, n, block_size):

    pad = ""                    # create an empty string
    while True:
        c = pad_file.read(1)
        if c == "\n":           # if we find a new line character,
            break               # break out of the function and avoid appending it
        else:
            pad += c            # not a newline, so append
    long_pad = long(pad)        # the pad in the file = a string, so make it a long
    long_decrypt_pad = modXP(long_pad, d, n)  # decrypt the pad using modular exponentiation
    decrypted_pad = long_to_string(long_decrypt_pad, block_size)
    return decrypted_pad  # return the decrypted pad in string form


def decrypt_file(ciphertext_file_name, decrypted_file_name, d, n, block_size, pad=None):

    in_file = open(ciphertext_file_name, "rb")  # open the ciphertext file for decryption
    out_file = open(decrypted_file_name, "wb")  # open a new file to write plaintext

    if not pad:  # if no pad is provided, decrypt the pad in the file
        pad = decrypt_pad(in_file, d, n, block_size)

    block = in_file.read(block_size)            # read through the ciphertext block_size bytes at a time
    while len(block) > 0:                       # while there is text to decrypt,
        decrypted_line = xor_block(pad, block)  # xor the block with the decrypted pad
        out_file.write(decrypted_line)
        block = in_file.read(block_size)        # increment the block of text

    # close both files
    in_file.close()
    out_file.close()
