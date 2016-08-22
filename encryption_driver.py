# CS 1 Lab Assignment 5
# write a driver to test the encryption and decryption functions on both plaintext files
# author Ian Marx, date 4 March 2016

# import the encryption and decryption functions
from encryption_functions import *
from decryption_functions import *

e_gen = 65537
n_gen = 11446213495949797116506912540657976412326489792001317543207804888401631746001522249106577369368376053134540383403131866673073016813759933873047996613914283966653620438628322840073120472280339280415629825134692985033795856821556206861691484627444251528948567927331277332522141912466001616385148244792262647765606857297088583240678094066602126655932101731303335171708845344389051258713974050084219994300171682160706774811164347290116235394306194310663211092782881545717606226300072637235958874714252644007752196813394869192040283437985345030335696543391349997059846893842973760551477672935590178899936256167205578638857
d_gen = 6194581690866951556041124463922015157733737277304465120809533908812259864918778569835544595217320930963820106482479836537536868644436537140993123638590594988010903912557324175530058393134245900755017145091738877171348573321130896210849956158600374036479359861552798334221818657420146563467177898687641661823746615567707526908336965099358176551205535565454194135457962661400544057764576801198669375058738530462192712016509579084697781001964045702290457517894802607332772435384657490188008188904705166093220292754745030995083935372059031702653091980133123536993799992677612979383345345972207427851971217394479108220657


# test encrypting and decrypting the first plaintext file
#encrypt_file("plaintext2.txt", "summerCT2.txt", e_gen, n_gen, BLOCK_SIZE)
decrypt_file("summerCT2.txt", "summerPT2.txt", d_gen, n_gen, BLOCK_SIZE)

# test encrypting and decrypting the second plaintext file
#encrypt_file("plaintext2.txt", "ciphertext2_test_RSA.txt", e_gen, n_gen, BLOCK_SIZE)
#decrypt_file("ciphertext2_test_RSA.txt", "plaintext2_test_RSA.txt", d_gen, n_gen, BLOCK_SIZE)

# encrypt the second plaintext file for my section leader to decrypt
#encrypt_file("plaintext2.txt", "ciphertext2_lily.txt", e_lily, n_lily, BLOCK_SIZE)



