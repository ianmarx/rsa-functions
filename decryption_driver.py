# CS 1 Lab Assignment 5
# write a driver to decrypt both cipher-text files and the video
# author Ian Marx, date 4 March 2016

# import the decryption functions
from decryption_functions import *


decrypt_file("ciphertext1.txt", "plaintext1.txt", d_key, n_key, BLOCK_SIZE)  # decrypt the first cipher-text file
decrypt_file("ciphertext2.txt", "plaintext2.txt", d_key, n_key, BLOCK_SIZE)  # decrypt the second cipher-text file


video_pad_file = open("pad.txt", "rb")                                                          # open pad.txt
video_pad = decrypt_pad(video_pad_file, d_key, n_key, BLOCK_SIZE)                               # decrypt the video pad
decrypt_file("encrypted-video", "decrypted-video-1.mp4", d_key, n_key, BLOCK_SIZE, video_pad)   # decrypt the vid file
video_pad_file.close()                                                                          # close pad.txt
