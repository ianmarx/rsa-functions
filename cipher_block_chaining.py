# CS Lab Assignment 5
# functions to implement cipher block chaining for encryption and decryption, using a generated initialization vector
# author Ian Marx, date 5 March 2016

# import all necessary functions
from random import randint
from checkpoint import *
from encryption_functions import generate_pad
from mod_exp import modular_exponentiation
from decryption_functions import decrypt_pad

# define my public and private keys along with the block size
e_key = 5
d_key = 423373754142276580220485879021423673212098671225290325821671703647655188149692674292370093017182893
n_key = 1058434385355691450551214697553559183030246678063330795205116915534886751904144766262010692314523041
BLOCK_SIZE = 16


def generate_vector(block_size):
    vector_string = ""
    while len(vector_string) <= block_size:         # until the pad is as long as block_size,
        char = chr(randint(0, 255))                 # generate a random ASCII character in binary form
        vector_string += char                       # concatenate it to the pad
    vector_long = string_to_long(vector_string)
    vector_bin = bin(vector_long)
    return vector_bin                               # return the vector as a binary number


def encrypt_cipher_block(plaintext_file_name, ciphertext_file_name, e, n, block_size):

    # open the plaintext file to read and a new file to write cipher-text
    in_file = open(plaintext_file_name, "rb")
    out_file = open(ciphertext_file_name, "wb")

    pad = generate_pad(block_size)                              # generate a pad
    pad_long = string_to_long(pad)
    encrypted_pad = modular_exponentiation(pad_long, e, n)      # encrypt the pad

    out_file.write(str(encrypted_pad) + "\n")                   # write the pad into the cipher-text file

    i_vector = generate_vector(block_size)                      # generate a vector of block_size
    out_file.write(i_vector + "\n")                             # write the vector into the next line

    current_block = in_file.read(block_size)                    # read the plaintext in blocks
    prev_block = i_vector                                       # set the previous block to the initialization vector
    while len(current_block) > 0:

        xored_current_block = xor_block(prev_block, current_block)        # xor the plaintext w/ the previous block
        encrypted_current_block = xor_block(pad, xored_current_block)     # encrypt that result
        out_file.write(encrypted_current_block)

        prev_block = encrypted_current_block               # increment the prev_block to be the block we just encrypted
        current_block = in_file.read(block_size)           # increment the current block to be the next text block

    in_file.close()
    out_file.close()


def decrypt_cipher_block(ciphertext_file_name, decrypted_file_name, d, n, block_size, pad=None):

    # open the cipher-text file to read and a new file to write plaintext
    in_file = open(ciphertext_file_name, "rb")
    out_file = open(decrypted_file_name, "wb")

    if not pad:
        pad = decrypt_pad(in_file, d, n, block_size)        # decrypt the pad in the file

    i_vector = ""                                           # create an empty string
    while True:
        c = in_file.read(1)
        if c == "\n":           # if we find a new line character,
            break               # break out of the function and avoid appending it
        else:
            i_vector += c       # not a newline, so append

    current_block = in_file.read(block_size)       # read a block of text of block_size size
    next_block = i_vector                          # set the next block to be the initialization vector

    while len(current_block) > 0:
        xored_current_block = xor_block(pad, current_block)                     # xor the block with the pad
        decrypted_current_block = xor_block(next_block, xored_current_block)    # decrypt by xoring with the next block
        out_file.write(decrypted_current_block)

        next_block = current_block                  # set the next block to be the block we just decrypted
        current_block = in_file.read(block_size)    # increment the current block to be the next text block

    # close both files
    in_file.close()
    out_file.close()
