# CS 1 Lab Assignment 5
# write functions to generate a random pad and to use it to encrypt a file
# author Ian Marx, 4 March 2016

# import the checkpoint functions, mod_exp, and randint (the latter to generate a random pad)
from random import randint
from checkpoint import *
from mod_exp import modular_exponentiation
from nonRecModXP import modXP

# define block size, my section leader's e and n values, and my e, d, and n values
BLOCK_SIZE = 16
e_lily = 5
n_lily = 645752195807787303145200358918085370001646941448440791183451603156773072170820962439802979922365737
e_key = 5
d_key = 423373754142276580220485879021423673212098671225290325821671703647655188149692674292370093017182893
n_key = 1058434385355691450551214697553559183030246678063330795205116915534886751904144766262010692314523041


def generate_pad(block_size):
    pad = ""
    while len(pad) <= block_size:      # until the pad is as long as block_size,
        char = chr(randint(0, 255))    # generate a random ASCII character
        pad += char                    # concatenate it to the pad
    return pad


def encrypt_file(plaintext_file_name, ciphertext_file_name, e, n, block_size):

    in_file = open(plaintext_file_name, "r")                # open plaintext for reading
    out_file = open(ciphertext_file_name, "wb")             # open a new file for writing cipher-text

    pad = generate_pad(block_size)                          # generate a random pad
    pad_long = string_to_long(pad)                          # turn it into a long int
    encrypted_pad = modXP(pad_long, e, n)  # encrypt it with modular exponentiation

    out_file.write(str(encrypted_pad) + "\n")               # write the pad and a newline character into the new file

    block = in_file.read(block_size)                        # assign a block of text of size block_size
    while len(block) > 0:
        encrypted_line = xor_block(pad, block)              # xor each block w/ the pad to encrypt
        out_file.write(encrypted_line)
        block = in_file.read(block_size)                    # increment the block of text

    # close both files
    in_file.close()
    out_file.close()
