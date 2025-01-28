# This is a pytest script to test multibit_negative() and
# multibit_subtractor() functions from assignment 2.  These functions
# should be imported from the solution file.

from phys305_hw1.a2 import multibit_negative, multibit_subtractor

# -----------------------------------------------------------------------------
# Helper functions to convert between integers and binary lists:
# * int2list: Converts a Python integer to a list of 0s and 1s with a
#             specified number of bits, where the least significant bit (LSB)
#             is at the beginning of the list.
# * list2int: Converts a list of 0s and 1s back to a Python integer, assuming
#             the least significant bit (LSB) is at the beginning of the list.

def int2list(a, nbits=4):
    return [int(c) for c in bin(a)[2:].zfill(nbits)[::-1]]

def list2int(A, nbits=None):
    if nbits is None: nbits = len(A)
    a = int(''.join(str(c) for c in A[::-1]), 2)
    return a if a < 2**(nbits-1) else a - 2**nbits

# -----------------------------------------------------------------------------
# Test functions for multibit_negative() and multibit_subtractor().
# These functions use the helper functions for cleaner test code.

def test_negative():
    for a in range(0, 16):
        A = int2list(a, nbits=5)

        C = multibit_negative(A)
        c = list2int(C)

        print(C, "->", c)
        assert c == -a

def test_subtractor():
    for a in range(0, 8):
        for b in range(0, 8):
            A = int2list(a)
            B = int2list(b)

            C = multibit_subtractor(A, B)
            c = list2int(C)

            print(C, "->", c)
            assert c == a - b
