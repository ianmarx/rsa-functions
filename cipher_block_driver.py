# CS 1 Lab Assignment 5
# make a driver to text cipher block chaining
# author Ian Marx, date 5 March 2016

from cipher_block_chaining import *     # import the cipher block chaining functions

# encrypt and decrypt the second plaintext file using cipher block chaining
encrypt_cipher_block("plaintext2.txt", "cipher_block_chain.txt", e_key, n_key, BLOCK_SIZE)
decrypt_cipher_block("cipher_block_chain.txt", "plain_cipher_block.txt", d_key, n_key, BLOCK_SIZE)