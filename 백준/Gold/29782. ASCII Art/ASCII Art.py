import sys

inputf = sys.stdin.readline

NUMBER_OF_ALPHABET = 26
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

T = int(inputf())
for i in range(1,T+1):
    N = int(inputf())

    repeat = 1
    total = 0

    while 1:
        number_of_chars = repeat * NUMBER_OF_ALPHABET
        if N <= number_of_chars:
            char_order = (N-1) // repeat
            print("Case #" + str(i) + ": " + ALPHABET[char_order])
            break
        else:
            N -= number_of_chars
            repeat +=1