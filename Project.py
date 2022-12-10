import numpy as np

# G0 is the Generator Matrix, which includes 3 redundancy bits in the 4bits msg and generates the codeword

G0 = [[1, 1, 0, 1],
      [1, 0, 1, 1],
      [1, 0, 0, 0],
      [0, 1, 1, 1],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]]

# H0 that detects if a bit in the codeword has an error

H0 = [[1, 0, 1, 0, 1, 0, 1],
      [0, 1, 1, 0, 0, 1, 1],
      [0, 0, 0, 1, 1, 1, 1]]

# RO is the matrix that receives the codeword that needs to be decoded back into the original 4 bits message

R0 = [[0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 1]]

# The matrixes are converted into array objects for easy operation.

G = np.array(G0)
H = np.array(H0)
R = np.array(R0)

"""Fuctions section"""


# The word is going to be considered a string to easily enter and change the values even with 0's at the beginning

def word_to_array(word_test):
    arr = list(map(int, (word_test)))
    for n in arr:
        if not n in range(0, 2):
            raise TypeError("The word has to be an input of 4 bits in binary")
        else:
            word = np.array(arr)
    return word


# Multiplication of G matrix and the original word to generate the codeword.

def hamming_encode(word):
    nw = word_to_array(word)
    codeword = np.remainder(np.matmul(G, nw), 2)
    return codeword


# This function changes one bit in the codeword

def msg_errors(codeword, pos_error):
    if pos_error > 6:
        raise TypeError("This is a vector with only 7 bits. Select a position between 0-6")
    else:
        codeword[pos_error] = not codeword[pos_error]
    return codeword


# Fuction changes the binary array position into a decimal integer value.

def bin_to_dec(paritybits):
    pos = ''.join(
        reversed([str(elem) for elem in paritybits]))  # The value is reversed to be interpreted in n bits binary
    paritybits = int(pos, 2)
    return paritybits - 1  # It is decreased by one, because Python counts positions from 0.


# The codeword is multiplied by the Parity Check Matrix to detect if a bit has an error and return in which position the bit was changed

def hamming_detect_errors(cw):
    parity_bits = np.remainder(np.matmul(H, cw), 2)
    pos_to_fix = bin_to_dec(parity_bits)
    return pos_to_fix


# The codeword is transformed into the original message

def hamming_decode(cw):
    pos_in_error = hamming_detect_errors(cw)  # 0
    if pos_in_error >= 0 and pos_in_error < 7:
        print(f'...Correcting error in position {pos_in_error}...')
        cw[pos_in_error] = not cw[pos_in_error]
        decode_word_correct = np.remainder(np.matmul(R, cw), 2)
        return decode_word_correct
    elif pos_in_error == -1:
        decode_word = np.remainder(np.matmul(R, cw), 2)
        return decode_word
    else:
        print('Something unexpected happened')


# Fuction checks if the original word and the decoded word are the same

def check_decoding(oword, dw):
    decodeword = ''.join([str(elem) for elem in dw])
    if oword == decodeword:
        return 0
    return -1


def test_codeword(word_test, bit_to_change):
    """
    This function takes a codeword, and corrupts a bit, specified by bit_to_change.
    If bit_to_change == -1, then we do not corrupt the codeword.

    The steps taken in this function are,
    (i)   Encode the word, i.e. change a 4-bit number to a 7-bit number
    (ii)  Corrupt a bit, in the position specified in bit_to_change (from 0-6), handled in msg_errors
    (iii) Detect whether there are errors using, hamming_detect_errors
    (iv)  Decode the word, by first detecting errors and their position if any, and then correcting the error,
          and returning the decoded codeword, i.e. from a 7-bit to 4-bit number
    (v)   Return a 0 if the original codeword matches the decoded codeword, else return -1
    """

    encode = hamming_encode(word_test)
    if bit_to_change != -1:
        corrupted = msg_errors(encode, bit_to_change)
    else:
        corrupted = encode
    detect_errors = hamming_detect_errors(corrupted)
    decoding = hamming_decode(corrupted)
    return check_decoding(word_test, decoding)


# Multiple Tests
# Fuction to test the coding and encoding functions.
possible_words = ['0000', '0001', '0010', '0011',
                  '0100', '0101', '0110', '0111',
                  '1000', '1001', '1010', '1011',
                  '1100', '1101', '1110', '1111']
bits_to_corrupt = range(-1, 7)

# All Combinations
for bit in bits_to_corrupt:
    if bit >= 0:
        print(f'Corrupting Bit {bit}')
    else:
        print(f'Not corrupting the original codeword')
    for word_to_test in possible_words:
        if test_codeword(word_to_test, bit) == 0:
            print(f'PASS: {word_to_test} correctly decoded')
        else:
            print(f'FAIL: {word_to_test} incorrectly decoded')
        print('-' * 20)
