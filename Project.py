import numpy as np

#G0 is the Generator Matrix, which includes 3 redundancy bits in the 4bits msg and generates the codeword

G0 = [[1, 1, 0, 1],
     [1, 0, 1, 1],
     [1, 0, 0, 0],
     [0, 1, 1, 1],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]]

#H0 that detects if a bit in the codeword has an error

H0 = [[1, 0, 1, 0, 1, 0, 1],
     [0, 1, 1, 0, 0, 1, 1],
     [0, 0, 0, 1, 1, 1, 1]]

#RO is the matrix that receives the codeword that needs to be decoded back into the original 4 bits message

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
    arr = list(map(int,(word_test)))
    for n in arr:
        if not n in range(0,2):
            raise TypeError("The word has to be an input of 4 bits in binary")
        else:
            word = np.array(arr)
    return word

# Multiplication of G matrix and the original word to generate the codeword.

def hamming_encode(word):
    nw = word_to_array(word)
    codeword = np.remainder(np.matmul(G,nw),2)
    return codeword

#This function changes one bit in the codeword

def msg_errors(codeword,pos_error):
    if pos_error > 6:
        raise TypeError("This is a vector with only 7 bits. Select a position between 0-6")
    else:
        codeword[pos_error] = not codeword[pos_error]
    return codeword

# Fuction changes the binary array position into a decimal integer value.

def bin_to_dec(paritybits):
    pos = ''.join(reversed([str(elem) for elem in paritybits])) # The value is reversed to be interpreted in n bits binary
    paritybits = int(pos,2)
    return paritybits-1 #It is decreased by one, because Python counts positions from 0.

# The codeword is multiplied by the Parity Check Matrix to detect if a bit has an error and return in which position the bit was changed

def hamming_detect_errors(cw):
    parity_bits = np.remainder(np.matmul(H, cw), 2)
    pos_to_fix = bin_to_dec(parity_bits)
    return pos_to_fix

# The codeword is transformed into the original message

def hamming_decode(cw):
    check_errors = hamming_detect_errors(cw)
    if check_errors > 0:
        print(f'...Correcting error in position {check_errors}...')
        cw[check_errors] = not cw[check_errors]
        decode_word_correct = np.remainder(np.matmul(R, cw), 2)
        return decode_word_correct
    else:
        decode_word = np.remainder(np.matmul(R, cw), 2)
        return decode_word

# Fuction checks if the original word and the decoded word are the same

def check_decoding(oword,dw):
    decodeword =''.join([str(elem) for elem in dw])
    if oword == decodeword:
            print('Word correctly decoded')
    else:
        print('Word incorrectly decoded')

# Fuction to test the coding and encoding functions.

def Testing_coding(word_test,bit_to_change):
    print(f'Original message: {word_test}')
    encode = hamming_encode(word_test)
    print('-' * 20)
    print(f'Codeword with 3 redundancy bits: {encode}')
    corrupted = msg_errors(encode, bit_to_change)
    print(f'Codeword is corrupted in one bit: {corrupted}')
    detect_errors = hamming_detect_errors(corrupted)
    print(f'The codeword has an error in this position: {detect_errors}')
    decoding = hamming_decode(corrupted)
    print(f'Word decoded: {decoding}')
    print('-' * 20)
    check_msg = check_decoding(word_test,decoding)


#Change the test parameters here
"""In word_to_test introduce only a combination of 4 binary digits"""
word_test = '1111'
"""To change a bit in the codeword, give a position"""
position_to_change = 3
hammingcodetest = Testing_coding(word_test,position_to_change)


